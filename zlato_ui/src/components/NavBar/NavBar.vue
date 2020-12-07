<template>
  <div>
    <!--    <v-system-bar-->
    <!--      absolute-->
    <!--      fixed-->
    <!--      class="text-center"-->
    <!--      dark-->
    <!--      app-->
    <!--      color="blue"-->
    <!--      height="30%"-->
    <!--    >-->
    <!--      <v-spacer></v-spacer>-->
    <!--      <v-icon>mdi-gold</v-icon>-->
    <!--      <span>Gold : Bid 1290 Ask 1270</span>-->
    <!--      <v-spacer></v-spacer>-->
    <!--      <v-icon>mdi-silverware-clean</v-icon>-->
    <!--      <span>Silver 128392</span>-->
    <!--      <v-spacer></v-spacer>-->
    <!--      <v-icon>mdi-coin</v-icon>-->
    <!--      <span>78.9</span>-->
    <!--      <v-spacer></v-spacer>-->
    <!--    </v-system-bar>-->

    <v-app-bar app light color="white" elevation="1">
      <div class="d-flex align-center">
        <v-img
          alt="Zlato Logo"
          class=" mr-2"
          contain
          src="@/assets/logo.png"
          transition="scale-transition"
          width="50px"
        />
        <v-card-text
          alt="Zlato"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="20%"
          width="100"
          ><h2>Zlato</h2></v-card-text
        >
      </div>
      <v-spacer></v-spacer>
      <NavBarButton link="/" title="home" icon="mdi-home" />
      <NavBarButton link="/orders" title="orders" icon="mdi-bag-checked" />
      <NavBarButton link="/favourites" title="Favourites" icon="mdi-heart" />
      <NavBarButton link="/account" icon="mdi-account" title="Account" />

      <template v-slot:extension>
        <!--        <v-divider></v-divider>-->
        <v-spacer></v-spacer>
        <v-icon>mdi-gold</v-icon>
        <span>1270</span>
        <v-spacer></v-spacer>
        <v-icon>mdi-silverware-clean</v-icon>
        <span>128392</span>
        <v-spacer></v-spacer>
        <v-icon>mdi-coin</v-icon>
        <span>78.9</span>
        <v-spacer></v-spacer>
      </template>
    </v-app-bar>
  </div>
</template>

<script>
import NavBarButton from "./NavBarButton";
export default {
  name: "NavBar",
  components: { NavBarButton }
};
</script>

<style scoped></style>
