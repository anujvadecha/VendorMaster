<template>
  <v-app-bar app light elevation="1">
    <div class="d-flex align-center">
      <v-img
        alt="Zlato Logo"
        class=" mr-2"
        contain
        src="@/assets/logo.png"
        transition="scale-transition"
        width="80"
      />
      <v-card-text
        alt="Zlato"
        class="shrink mt-1 show-sm-and-down"
        contain
        min-width="100"
        width="100"
        ><h2>Zlato</h2></v-card-text
      >
    </div>
    <v-spacer></v-spacer>
    <NavBarButton link="/" title="home" icon="mdi-home" />
    <NavBarButton link="/orders" title="orders" icon="mdi-bag-checked" />
    <NavBarButton link="/favourites" title="Favourites" icon="mdi-heart" />
    <NavBarButton link="/account" icon="mdi-account" title="Account" />
  </v-app-bar>
</template>

<script>
import NavBarButton from "./NavBarButton";
export default {
  name: "NavBar",
  components: { NavBarButton }
};
</script>

<style scoped></style>
