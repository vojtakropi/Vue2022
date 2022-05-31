import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/home",
      name: "home",
      component: Home
    },
    {
      path: "/",
      name: "login",
      component: () => import("./views/Login.vue")
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("./views/Signup.vue")
    },
    {
      path: "/scoreboard",
      name: "scoreboard",
      component: () => import("./views/Scoreboard.vue")
    },
  ]
});
