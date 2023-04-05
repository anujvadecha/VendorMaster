<template>
  <router-link :to="link" style="text-decoration:none; ">
    <v-btn text class="">
      <v-icon left style="color:dimgrey">{{ icon }}</v-icon>
      <span class="hidden-sm-and-down" style="color:dimgrey">
        {{ title }}
        </span>
      </v-btn>
  </router-link>
</template>

<script>
export default {
  name: "NavBarButton",
  props: ["link", "title", "icon"]
};
</script>

<style scoped></style>
