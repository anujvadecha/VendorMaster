<template>
  <div class="Favourites">
    <!-- <v-data-table
      :headers="headers"
      :items="favourite_items"
      loading-text="Loading text.....Please wait"
    >
    </v-data-table> -->
    <v-card>
      <v-card-title>Favourites</v-card-title>
      <v-data-table
        :headers="headers"
        :items="favourite_items"
        hide-default-footer
        disable-sort
      >
        <template v-slot:body="props">
          <draggable :list="props.items" tag="tbody">
            <tr v-for="(user, index) in props.items" :key="index">
              <td>
                <v-icon>
                  mdi-arrow-all
                </v-icon>
              </td>
              <td>{{ user.vendor }}</td>
              <td>{{ user.name }}</td>
              <td>{{ user.bid }}</td>
              <td>{{ user.ask }}</td>
              <td>{{ user.high }}</td>
              <td>{{ user.low }}</td>
            </tr>
          </draggable>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  name: "Favourites",
  components: {
    draggable
  },
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
        { text: "Low", value: "low", filterable: false }
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
