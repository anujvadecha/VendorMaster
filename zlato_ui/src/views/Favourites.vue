<template>
  <div class="Favourites">
    <h2>Favourites</h2>

    <v-data-table
      :headers="headers"
      :items="favourite_items"
      loading-text="Loading text.....Please wait"
    >
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "Favourites",
  data() {
    return {
      favourite_items: [],
      headers: [
        { text: "", sortable: false },
        { text: "Vendor", align: "start", value: "vendor" },
        { text: "Symbol", value: "name" },
        { text: "Bid", value: "bid", filterable: false },
        { text: "Ask", value: "ask", filterable: false },
        { text: "High", value: "high", filterable: false },
        { text: "Low", value: "low", filterable: false },
        { text: "", value: "favourites" }
      ]
    };
  },
  created() {
    this.favourite_items = this.$store.state.instruments.filter(instrument => {
      return instrument.is_favourite === true;
    });
    console.log(this.favourite_items);
  }
};
</script>

<style scoped>
.Favourites {
  color: black;
}
</style>
