<template>
  <div>
    <span :key="game.gameId" v-for="game in reversedSchedule">
      <v-list-item>
        <v-list-item-content
          @click="print"
          class="center"
          style="font-size: 20px; font-weight: bold"
        >
          <div class="center">
            <div v-html="generateGameString(game)"></div>
            <img :src="getIconUrl(game.hTeam.teamId)" /> &emsp;
            <span
              :style="[
                Number(game.hTeam.score) < Number(game.vTeam.score)
                  ? 'font-weight:normal;'
                  : 'font-weight:bold',
              ]"
            >
              {{ game.hTeam.score }}
            </span>
            <p>Vs.</p>
            <img :src="getIconUrl(game.vTeam.teamId)" /> &emsp;
            <span
              :style="[
                Number(game.hTeam.score) > Number(game.vTeam.score)
                  ? 'font-weight:normal;'
                  : 'font-weight:bold',
              ]"
            >
              {{ game.vTeam.score }}
            </span>
            <br />
          </div>
          <n-divider />
        </v-list-item-content>
      </v-list-item>
    </span>
  </div>
</template>

<script>
import { NDivider } from "naive-ui";
import TeamsData from "../localData/teams.json";

const gameType = ["Preseason", "Regular Season", "", "Post Season", "Play-In"];
const roundType = [
  "Playoffs Round 1",
  "Conference Semifinals",
  "Conference Finals",
  "NBA Finals",
];
export default {
  name: "ScheduleTable",
  components: {
    NDivider,
  },
  props: {
    schedule: Array,
    name: String,
  },
  data() {
    return {
      translationTable: TeamsData,
    };
  },
  computed: {
    reversedSchedule() {
      return this.schedule.slice().reverse();
    },
  },
  methods: {
    print() {
      console.log(this.schedule);
    },
    getIconUrl(teamId) {
      let tricode = this.translationTable.filter(
        (team) => team.teamId == teamId
      )[0].abbreviation;
      return require(`../assets/${tricode}.svg`);
    },
    generateGameString(game) {
      let playoffString = "";
      let playoff = game.playoffs;
      if (playoff) {
        playoffString = `${roundType[playoff.roundNum - 1]} <br> 
                Game: #${playoff.gameNumInSeries} <br> ${
          playoff.seriesSummaryText
        } <br> 
                `;
      }
      return (
        gameType[game.seasonStageId - 1] +
        "<br>" +
        playoffString +
        "<br>" +
        game.startTimeUTC.substring(0, 10) +
        "<br><br>"
      );
    },
  },
};
</script>

<style scoped>
.center {
  margin: auto;
  display: inline-block;
}

img {
  width: 164px;
  height: 164px;
  vertical-align: middle;
}
</style>
