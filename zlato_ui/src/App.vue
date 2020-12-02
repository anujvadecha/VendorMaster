<template>
  <v-app>
<!--    <v-system-bar-->
<!--  height="33"-->
<!--  color="blue"-->
<!--    > Prices Gold:50999 </v-system-bar>-->
    <v-app-bar app color="orange"  dark >
      <div class="d-flex align-center">
        <v-img
          alt="Zlato Logo"
          class="shrink mr-2"
          contain
          src="logo.png"
          transition="scale-transition"
          width="40"
        />
        <v-card-text
          alt="Zlato"
          class="shrink mt-1 show-sm-and-down"
          contain
          min-width="100"
          width="100"
        ><h1>Zlato</h1></v-card-text>
      </div>
      <v-spacer></v-spacer>
      <router-link  to="/"><v-btn  text><span class="mr-2">Home</span></v-btn></router-link>
      <router-link to="/orders"><v-btn text><span class="mr-2">Orders</span></v-btn></router-link>
      <router-link to="/favourites"><v-btn text><span class="mr-2">Favourites</span></v-btn></router-link>
      <router-link to="/account"><v-btn  text><span class="mr-2">Account</span></v-btn></router-link>
      </v-app-bar>

      <v-main >
        <v-container >
          <router-view />
        </v-container>
      </v-main>
    <v-footer app>
      Built with love and dedication from DeltaCap Bullion
    </v-footer>

  </v-app>
</template>
<script>
// import Vue from 'vue'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)

export default {
  name: "App",

  components: {
  },

  data: () => ({
    //
  })
};
</script>
