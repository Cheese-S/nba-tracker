<template>
  <div class="home" v-if="schedule">
    <section>
      <h3>Western Conference</h3>
      <Teams
        :teams="west.teams"
        :schedule="west.schedules"
        :standings="west.standings"
      />
    </section>
    <section>
      <h3>Eastern Conference</h3>
      <Teams
        :teams="east.teams"
        :schedule="east.schedules"
        :standings="east.standings"
      />
    </section>
  </div>
</template>

<script>
import Teams from "../components/Teams.vue";
import TeamsData from "../localData/teams.json";

export default {
  name: "Home",
  components: {
    Teams,
  },
  computed: {
    west() {
      let teams = TeamsData.filter((team) => team.conference == "west");
      let standings = [];
      let schedules = [];
      teams.forEach((team) => {
        standings.push(
          ...this.standings.filter((standing) => standing.teamId == team.teamId)
        );
        schedules.push([team.teamId, this.schedule.get(team.teamId)]);
      });
      return {
        teams: teams,
        standings: standings,
        schedules: schedules,
      };
    },
    east() {
      let teams = TeamsData.filter((team) => team.conference == "east");
      let standings = [];
      let schedules = [];
      teams.forEach((team) => {
        standings.push(
          ...this.standings.filter((standing) => standing.teamId == team.teamId)
        );
        schedules.push([team.teamId, this.schedule.get(team.teamId)]);
      });
      return {
        teams: teams,
        standings: standings,
        schedules: schedules,
      };
    },
  },
  data() {
    return {
      standings: [],
      schedule: null,
    };
  },
  async created() {
    const NBA = require("nba");
    let response = await NBA.data.standings();
    this.standings = response.league.standard.teams;
    response = await NBA.data.schedule(new Date().getFullYear() - 1);
    console.log(response);
    let schedule = response.league.standard;
    let scheduleMap = new Map();
    for (const team of TeamsData) {
      scheduleMap.set(team.teamId, []);
    }

    for (const game of schedule) {
      if (scheduleMap.get(Number(game.hTeam.teamId))) {
        scheduleMap.get(Number(game.hTeam.teamId)).push(game);
        scheduleMap.get(Number(game.vTeam.teamId)).push(game);
      }
    }
    this.schedule = scheduleMap;
  },
};
</script>

<style scoped>
.home {
  padding: 20px;
}
section {
  padding: 10px;
}
h3 {
  font-size: 20px;
}
</style>
