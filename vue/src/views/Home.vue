<template>
  <v-app style="min-width:360px;">
    <v-content v-show="a">
      <v-row>
        <octocat />
      </v-row>
      <v-row justify="center">
        <grid-menu-left />
        <main-grid />
        <grid-menu-right />
      </v-row>
    </v-content>
  </v-app>
</template>

<script>
import GridMenuLeft from "../components/GridMenuLeft";
import MainGrid from "../components/MainGrid";
import GridMenuRight from "../components/GridMenuRight";
import Octocat from "../components/Octocat";

export default {
  name: "App",
  data(){
    return {
      a : this.$store.state.logedin
  };
  },
  components: {
    GridMenuLeft,
    MainGrid,
    GridMenuRight,
    Octocat,
  },
 methods:{
 t(){
   this.a = this.$store.state.logedin;
  }
},
};

</script>

<style lang="scss">
.container {
  width: auto;
  margin: auto 0;
}
.row {
  margin-left: 0;
  margin-right: 0;
}
</style>
