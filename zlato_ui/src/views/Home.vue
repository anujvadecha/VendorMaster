<template>
  <div class="home">
    <v-img
      alt="Zlato Marketing"
      class=" mr-2"
      contain
      src="@/assets/marketing.png"
      transition="scale-transition"
      max-height="150px"
    />

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
      <v-chip-group mandatory active-class="primary--text">
        <v-chip class="ma-2">Gold 999</v-chip>
        <v-chip class="ma-2">Gold 999 1kg</v-chip>
        <v-chip class="ma-2">Gold 995</v-chip>
        <v-chip class="ma-2">Gold 995 1kg</v-chip>
      </v-chip-group>
      <v-data-table
        :headers="headers"
        :items="instruments_to_render"
        :search="search"
        loading-text="Loading... Please wait"
      >
        <template v-slot:item.vendor="{ item }">
          <div dark @click="open_vendor_dialog(item)" style="color:slateblue;">
            {{ item.vendor }}
          </div>
        </template>
        <template v-slot:item.bid="{ item }">
          <div dark @click="open_order_sheet(item)">
            {{ item.bid }}
          </div>
        </template>
        <template v-slot:item.ask="{ item }">
          <div dark @click="open_order_sheet(item)">
            {{ item.ask }}
          </div>
        </template>
      </v-data-table>
    </v-card>
    <v-btn @click="get_api">Close</v-btn>
    <v-bottom-sheet v-model="sheet" inset>
      <v-sheet class="text-center" height="400px">
        <v-btn class="mt-6" text color="red" @click="sheet = !sheet">
          close
        </v-btn>
        <div class="my-3">
          Order Page
          {{ selected_item }}
        </div>
      </v-sheet>
    </v-bottom-sheet>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <!--        {{ selected_vendor_item.vendor.name }}-->
        <!--        <v-divider></v-divider>-->
        {{ selected_vendor_item }}
        <v-btn color="blue darken-1" text @click="dialog = false">
          Close
        </v-btn>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
// @ is an alias to /src

import { apiService } from "@/common/api.service";

export default {
  name: "Home",
  data() {
    return {
      selected_item: null,
      selected_vendor_item: null,
      dialog: false,
      sheet: false,
      items: ["gold999", "gold 999 1kg", "gold 995", "gold 995 1kg"],
      search: "",
      headers: [
        { text: "Vendor", align: "start", value: "vendor" },
        { text: "Symbol", value: "name" },
        { text: "Bid", value: "bid", filterable: false },
        { text: "Ask", value: "ask", filterable: false },
        { text: "High", value: "high", filterable: false },
        { text: "Low", value: "low", filterable: false }
      ],
      instruments: this.$store.getters.get_instruments
    };
  },
  computed: {
    instruments_to_render: function() {
      return this.$store.getters.get_instruments;
    }
  },
  methods: {
    open_order_sheet: function(item) {
      console.log(item);
      this.selected_item = item;
      this.sheet = !this.sheet;
    },
    open_vendor_dialog: function(item) {
      console.log(this.$store);
      console.log(item);
      this.selected_vendor_item = this.$store.getters.get_vendor_instruments(
        item.vendor_id
      );
      this.dialog = !this.dialog;
    },
    get_api() {
      let endpoint = window.location.host + "/order/api/orderDetails";
      apiService(endpoint).then(response => {
        console.log(response);
      });
    }
  }
};
</script>
