<template>
  <div id="app">
    <div id="nav">
      <div v-show="!a">
      <router-link to="/">Login</router-link> |
      <router-link to="/signup">Signup</router-link>|
      <router-link to="/scoreboard">Scoreboard</router-link>|
      <router-link to="/pswchange">Changepassword</router-link>|
      </div>
    <div v-show="a">
     <button @click="logof"></button>
    </div>
    <router-link style="size: 15px;" to="/home">Home</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  data() {
    return{
      a : this.$store.state.logedin
    };
  },
  methods:{
    logof(){
       this.$store.commit("increment");
    },
  },  watch: {
    a: function(value){
      this.a = value;
    }
  }
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
#nav{
  background-color: rgb(4, 233, 92);
  overflow: hidden;
  justify-content: center;
}


</style>
