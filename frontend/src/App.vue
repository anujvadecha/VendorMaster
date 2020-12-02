<template>
  <div>
    <v-card
  elevation="2"
>Hello world</v-card>
<!--    <v-app-bar></v-app-bar>-->
      <b-navbar toggleable="lg" type="dark" variant="warning">
      <b-navbar-brand href="/">Zlato</b-navbar-brand>
        <b-navbar-nav class="ml-auto" right>
          <b-nav-item ><router-link to="/">Home</router-link></b-nav-item>
          <b-nav-item><router-link to="/orders">Orders</router-link></b-nav-item>
          <b-nav-item><router-link to="/favourites">Favourites</router-link></b-nav-item>
          <b-nav-item><router-link to="/account">Account</router-link></b-nav-item>
        </b-navbar-nav>
      </b-navbar>
    <router-view />
 </div>
</template>
<script>
import Vue from 'vue'
// import "materialize-css"; // It installs the JS asset only
// import "materialize-css/dist/css/materialize.min.css";
import 'vuesax/dist/vuesax.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vuetify/src/stylus/app.styl';
import './plugins/vuetify';
import 'vuetify/dist/vuetify.min.css';
import '../stylus/main.styl';
import Vuetify from "vuetify";
Vue.use(Vuetify)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
export default {
  name: "App",

};
</script>
<style>
</style>