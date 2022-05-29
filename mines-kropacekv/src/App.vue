<template>
  <v-app>
    <v-content>
      <main-grid/>
    </v-content>
  </v-app>
</template>

<script>
import MainGrid from './components/MainGrid.vue'

export default {
  name: 'App',

  components: {
    MainGrid,
  },

  data: () => ({
    //
  }),
};
</script>
