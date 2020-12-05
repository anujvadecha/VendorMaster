import Home from "@/views/Home.vue";
import Orders from "@/views/Orders.vue";
import Account from "@/views/Account.vue";
import Vue from "vue";
import VueRouter from "vue-router";
import Favourites from "@/views/Favourites";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/orders",
    name: "Orders",
    component: Orders
  },
  {
    path: "/account",
    name: "Account",
    component: Account
  },
  {
    path: "/favourites",
    name: "Favourites",
    component: Favourites
  }
];

const router = new VueRouter({
  mode: "history",
  routes
})

export default router;