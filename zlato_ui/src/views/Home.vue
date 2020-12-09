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
        <v-chip @click="changeSearchValue('')" class="ma-2">All</v-chip>
        <v-chip @click="changeSearchValue('gold 999')" class="ma-2"
          >Gold 999</v-chip
        >
        <v-chip @click="changeSearchValue('gold 999 1kg')" class="ma-2"
          >Gold 999 1kg</v-chip
        >
        <v-chip @click="changeSearchValue('gold 995')" class="ma-2"
          >Gold 995</v-chip
        >
        <v-chip @click="changeSearchValue('gold 995 1kg')" class="ma-2"
          >Gold 995 1kg</v-chip
        >
      </v-chip-group>
      <v-data-table
        :headers="headers"
        :items="instruments_to_render"
        loading-text="Loading... Please wait"
        :search="search"
        :custom-filter="customFilter"
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
        <template v-slot:item.is_favourite="{ item }">
          <div v-on:mouseover="showStar" v-on:mouseleave="hideStar">
            <div dark @click="toggleFavourite(item)">
              <v-icon v-if="item.is_favourite">
                <!-- && isVisible">-->
                mdi-star
              </v-icon>
              <v-icon v-else-if="!item.is_favourite">
                mdi-star-outline
              </v-icon>
            </div>
          </div>
        </template>
      </v-data-table>
    </v-card>
    <BottomOrderSheet :selected_item="selected_item"></BottomOrderSheet>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
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
import { add_to_favourites, remove_from_favourites } from "@/common/api_calls";
import BottomOrderSheet from "@/components/orders/BottomOrderSheet";

export default {
  name: "Home",
  components: { BottomOrderSheet },
  data() {
    return {
      isVisible: false,
      selected_item: null,
      selected_vendor_item: null,
      dialog: false,
      sheet: false,
      items: ["gold999", "gold 999 1kg", "gold 995", "gold 995 1kg"],
      headers: [
        { text: "Vendor", align: "start", value: "vendor" },
        { text: "Symbol", value: "name" },
        { text: "Bid", value: "bid", filterable: false },
        { text: "Ask", value: "ask", filterable: false },
        { text: "High", value: "high", filterable: false },
        { text: "Low", value: "low", filterable: false },
        { text: "", value: "is_favourite" }
      ],
      instruments: this.$store.getters.get_instruments,
      selectedInstruments: [],
      search: ""
    };
  },
  computed: {
    instruments_to_render: function() {
      return this.$store.getters.get_instruments;
    },
    bottom_sheet: function() {
      return this.$store.getters.get_sheet;
    }
  },
  methods: {
    changeSearchValue(text) {
      this.search = text;
    },
    successToast: function(message) {
      this.$toast.success({
        message: message,
        orientation: this.$toast.TOP_RIGHT,
        duration: 2000
      });
    },
    errorToast: function(message) {
      this.$toast.error({
        message: message,
        orientation: this.$toast.TOP_RIGHT,
        duration: 2000
      });
    },
    customFilter(value, search, item) {
      // search = "/^" + search + "$/";
      let isSymbolType = search === item.type;
      return isSymbolType;
    },
    showStar: function() {
      this.isVisible = true;
    },
    hideStar: function() {
      this.isVisible = false;
    },
    open_order_sheet: function(item) {
      this.$store.dispatch("set_sheet", true);
      this.selected_item = item;
    },
    open_vendor_dialog: function(item) {
      console.log(this.$store);
      console.log(item);
      this.selected_vendor_item = this.$store.getters.get_vendor_instruments(
        item.vendor_id
      );

      this.$router.push({
        name: "Vendor",
        params: {
          vendor: this.selected_vendor_item.vendor.name,
          vendor_object: this.selected_vendor_item
        }
      });
      // this.dialog = !this.dialog;
    },
    get_api() {
      let endpoint = window.location.host + "/order/api/orderDetails";
      apiService(endpoint).then(response => {
        console.log(response);
      });
    },
    toggleFavourite(item) {
      item.is_favourite = !item.is_favourite;
      if (item.is_favourite === false) {
        remove_from_favourites(item.instrument_id).then(res => {
          console.log(res);
        });
        this.errorToast(
          "Removed " + item.vendor + " " + item.name + " from favourites"
        );
      } else {
        add_to_favourites(item).then(res => {
          console.log(res);
        });
        this.successToast(
          "Added " + item.vendor + " " + item.name + " from favourites"
        );
      }
    }
  }
};
</script>
