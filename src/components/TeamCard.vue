<template>
  <div @click="showModal = true">
    <n-card
      :style="cssVars"
      :title="team.teamName"
      header-style="font-weight: bolder;"
    >
      <template #cover>
        <!-- <img src='../assets/BOS.svg'> -->
        <img :src="getIconUrl()" />
      </template>
      <div v-if="standing">
        {{ standing.win + "-" + standing.loss }}
      </div>
    </n-card>
    <n-modal
      style="overflow-y: auto"
      v-model:show="showModal"
      :title="team.teamName"
    >
      <n-card size="huge">
        <ScheduleTable :schedule="schedule" :name="team.abbreviation" />
      </n-card>
    </n-modal>
  </div>
</template>

<script>
import { NModal, NCard } from "naive-ui";
import ScheduleTable from "./ScheduleTable.vue";

export default {
  name: "TeamCard",
  components: {
    NCard,
    NModal,
    ScheduleTable,
  },
  props: {
    team: Object,
    standing: Object,
    color: String,
    schedule: Array,
  },
  computed: {
    cssVars() {
      return {
        "max-width": "350px",
        "max-height": "350px",
        "font-weight": "bold",
        "border-bottom": "10px solid " + this.color,
      };
    },
  },
  methods: {
    getIconUrl() {
      return require(`../assets/${this.team.abbreviation}.svg`);
    },
  },
  data() {
    return {
      showModal: false,
    };
  },
};
</script>

<style scoped>
.n-modal {
  max-height: 800px;
  max-width: 60%;
  border: 0ch;
}
#header-style {
  font-weight: bold;
}
</style>
