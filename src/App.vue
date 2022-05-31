<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
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
</style>
