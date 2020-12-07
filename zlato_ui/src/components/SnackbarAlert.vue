<template>
  <v-snackbar vertical right color="orange" v-model="snackbar" :timeout="20000">
    {{ message }}
    <template v-slot:action="{ attrs }">
      <v-btn color="white" text v-bind="attrs" @click="close_snackbar()">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  name: "SnackbarAlert",
  computed: {
    snackbar: function() {
      return this.$store.state.snackbar;
    },
    message: function() {
      return this.$store.state.snackbar_message;
    }
  },
  methods: {
    close_snackbar: function() {
      this.$store.state.snackbar = false;
    }
  }
};
</script>

<style scoped></style>
