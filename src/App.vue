<template>
  <div id="app">
    <div id="nav">
      <router-link style="size: 15px;" to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">Signup</router-link>
    </div>
    <router-view/>
  </div>
</template>

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
