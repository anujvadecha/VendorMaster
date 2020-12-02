<template>
  <div class="home">
    <v-card>
      <v-card-title>
        Ticker Prices
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-chip-group
          mandatory
          active-class="primary--text"
        >
        <v-chip class="ma-2">Gold 999</v-chip>
        <v-chip class="ma-2">Gold 999 1kg</v-chip>
        <v-chip class="ma-2">Gold 995</v-chip>
        <v-chip class="ma-2">Gold 995 1kg</v-chip>
      </v-chip-group>
      <v-data-table
        :headers="headers"
        :items="desserts"
        :search="search"
      >
      <template v-slot:item.bid="{ item }">
        <div
          dark
          @click="sheet = !sheet"
        >
          {{ item.bid }}
        </div>
      </template>
         <template v-slot:item.ask="{ item }">
        <div
          dark
          @click="sheet = !sheet"
        >
          {{ item.ask }}
        </div>
      </template>
      </v-data-table>
    </v-card>
    <v-bottom-sheet v-model="sheet" inset>
      <v-sheet
        class="text-center"
        height="400px"
      >
        <v-btn
          class="mt-6"
          text
          color="red"
          @click="sheet = !sheet"
        >
          close
        </v-btn>
        <div class="my-3">
          Order Page
        </div>
      </v-sheet>
    </v-bottom-sheet>
  </div>


</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  data() {
    return {
      sheet: false,
      items: ["gold999", "gold 999 1kg", "gold 995", "gold 995 1kg"],
      search: "",
      headers: [
        { text: "Vendor", align: "start",  value: "vendor"},
        { text: "Symbol", value: "symbol" },
        { text: "Bid", value: "bid" },
        { text: "Ask", value: "ask" },
        { text: "High", value: "high" },
        { text: "Low", value: "low" }
      ],
      desserts: [
        {
          vendor: "Arihant",
          symbol: "Gold 999 with Gst/TCS",
          bid: 6.0,
          ask: 24,
          high: 4.0,
          low: 1
        },
          {
          vendor: "Arihant",
          symbol: "Gold 999 Imported",
          bid: 6.0,
          ask: 24,
          high: 4.0,
          low: 1
        }
      ]
    };
  },
  components: {
    // HelloWorld
  }
};
</script>
