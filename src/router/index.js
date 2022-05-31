import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

import views from "../views/home";

const routes = [{
    component: views,
    name: "home",
    path: "/home"
},
];

export default new VueRouter[{
    routes
}];