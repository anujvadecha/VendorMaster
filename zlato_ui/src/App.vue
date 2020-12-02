<template>
  <v-app>
<!--    <v-system-bar-->
<!--  height="33"-->
<!--  color="blue"-->
<!--    > Prices Gold:50999 </v-system-bar>-->
    <v-app-bar app color="blue"  dark >
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

      <v-main style="background-color:whitesmoke">
        <v-container style="background-color:white;">
          <router-view />
        </v-container>
      </v-main>
<!--    <v-footer app>-->
<!--  </v-footer>-->
  </v-app>
</template>
<script>

export default {
  name: "App",

  components: {
  },

  data: () => ({
    //
  })
};
</script>
