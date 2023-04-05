<template>
  <div>
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
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text class="" v-bind="attrs" v-on="on">
            <v-icon left style="color:dimgrey">mdi-account</v-icon>
            <span class="hidden-sm-and-down" style="color:dimgrey"
              >Account</span
            >
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in items" :key="index">
            <v-list-item-title @click="selectedAction(item.title)">{{
              item.title
            }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <template v-slot:extension>
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
  components: { NavBarButton },
  data() {
    return {
      items: [{ title: "Reset password" }, { title: "Logout" }],
      selected: null
    };
  },
  methods: {
    selectedAction(event) {
      this.selected = event;
      switch (this.selected) {
        case "Logout": {
          console.log(this.selected);
          window.location = "/accounts/logout/";
          break;
        }
        case "Reset password": {
          window.location = "/accounts/password_reset/";
          break;
        }
      }
    }
  }
};
</script>

<style scoped></style>
