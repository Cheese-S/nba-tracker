<template>
  <div>
    <div class="cards" :key="team.teamId" v-for="team in teams">
      <TeamCard
        :team="team"
        :standing="getStanding(team.teamId)"
        :color="getColor(team.abbreviation)"
        :schedule="getSchedule(team.teamId)"
      />
    </div>
  </div>
</template>

<script>
import TeamCard from "./TeamCard";

import { getMainColor } from "nba-color";

export default {
  name: "Teams",
  props: {
    teams: Array,
    schedule: Array,
    standings: Array,
  },
  components: {
    TeamCard,
  },

  methods: {
    getStanding(id) {
      return this.standings.filter((standing) => standing.teamId == id)[0];
    },
    getColor(tricode) {
      return getMainColor(tricode).hex;
    },
    getSchedule(id) {
      console.log("This is the id" + id);
      for (let i = 0; i < this.schedule.length; i++) {
        if (this.schedule[i][0] === id) {
          console.log(1);
          return this.schedule[i][1];
        }
      }
    },
  },
};
</script>

<style scoped>
.cards {
  display: inline-block;
  padding: 10px;
}
</style>
