<template>
  <div class="home">
<!--     <v-parallax-->
<!--    height="300"-->
<!--    src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"-->
<!--  ></v-parallax>-->
    <v-navigation-drawer permanent>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Ticker prices
          </v-list-item-title>
          <v-list-item-subtitle>
            Click on item price to place Order
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

<!--    <img alt="Vue logo" src="../assets/logo.png" />-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App" />-->
    </v-navigation-drawer>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  data(){
    return{
      items:["gold 999","gold 999 1kg",
      "gold 995","gold 995 1kg"]
    }
  },
  components: {
    // HelloWorld
  }
};
</script>
