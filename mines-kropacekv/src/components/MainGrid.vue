<template>
  <v-container>
    <v-row no-gutters v-for="(row, row_idx) in 8" :key="row_idx" justify="center">
      <template v-for="(col, col_idx) in 8">
        <v-hover v-slot:default="{ hover }" :key="col_idx">
          <v-col>
            <v-card
              :class="[{'on-hover': hover}, 
              'square-card', 
              'flex-center']"
              elevation="4"
              outlined
            ></v-card>
          </v-col>
        </v-hover>
      </template>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";
export default {
  methods: {
    ...mapActions({
      setPattern: "mainGrid/setPattern"
    })
  },
  created() {
    this.setPattern();
  }
};
</script>
<style lang="scss" scoped>
.square-card {
  height: 2rem;
  width: 2rem;
}
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.col {
  flex-grow: 0;
}
.on-hover {
  cursor: pointer;
  background-color: rgba(0, 0, 0, 0.01) !important;
}
</style>