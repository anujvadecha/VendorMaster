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
            <!--          <div dark @click="B">-->
            {{ item.ask }}
          </div>
        </template>
        <template v-slot:item.is_favourite="{ item }">
          <div dark @click="toggleFavourite(item)">
            <v-icon v-if="item.is_favourite">
              mdi-star
            </v-icon>
            <v-icon v-else>
              mdi-star-outline
            </v-icon>
          </div>
        </template>
      </v-data-table>
    </v-card>
    <!--    <v-btn @click="get_api">Close</v-btn>-->
    <!--    <v-bottom-sheet v-model="sheet" inset>-->
    <!--      <v-sheet>-->
    <!--        <v-card dark tile color="blue">-->
    <!--          <v-container fluid>-->
    <!--            <v-row no-gutters>-->
    <!--              <v-col class="text-right">-->
    <!--                Place order-->
    <!--              </v-col>-->
    <!--            </v-row>-->
    <!--            <div v-if="selected_item">-->
    <!--              <v-row>-->
    <!--                <v-col v-if="selected_item">-->
    <!--                  &lt;!&ndash;              <v-if></v-if>&ndash;&gt;-->
    <!--                  <span class="font-weight-bold">{{-->
    <!--                    selected_item.vendor-->
    <!--                  }}</span>-->
    <!--                  <span class="ml-2">{{ selected_item.name }}</span>-->
    <!--                  &lt;!&ndash;              {{selected_item }}&ndash;&gt;-->
    <!--                </v-col>-->
    <!--                <v-col class="text-right">-->
    <!--                  <span class="ml-2">Bid: {{ selected_item.bid }}</span>-->
    <!--                  <span class="ml-2">Ask: {{ selected_item.ask }}</span>-->
    <!--                </v-col>-->
    <!--              </v-row>-->
    <!--            </div>-->
    <!--          </v-container>-->
    <!--        </v-card>-->
    <!--        <v-card height="200px">-->
    <!--          <v-tabs>-->
    <!--            <v-tab>Buy</v-tab>-->
    <!--            <v-tab>Sell</v-tab>-->
    <!--            <v-tab-item>-->
    <!--              <v-card tile>-->
    <!--                <v-container fluid>-->
    <!--                  <v-col class="text-right">-->
    <!--                    <v-btn outlined color="blue">Buy</v-btn>-->
    <!--                    <v-btn outlined class="ml-2" color="blue">Cancel</v-btn>-->
    <!--                  </v-col>-->
    <!--                </v-container>-->
    <!--              </v-card>-->
    <!--            </v-tab-item>-->
    <!--            <v-tab-item>-->
    <!--              <v-card tile>-->
    <!--                <v-container fluid>-->
    <!--                  <v-col class="text-right">-->
    <!--                    <v-btn outlined color="blue">Sell</v-btn>-->
    <!--                    <v-btn outlined class="ml-2" color="blue">Cancel</v-btn>-->
    <!--                  </v-col>-->
    <!--                </v-container>-->
    <!--              </v-card>-->
    <!--            </v-tab-item>-->
    <!--          </v-tabs>-->
    <!--        </v-card>-->
    <!--      </v-sheet>-->
    <!--    </v-bottom-sheet>-->
    <BottomOrderSheet :selected_item="selected_item"></BottomOrderSheet>
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
import { add_to_favourites, remove_from_favourites } from "@/common/api_calls";
import BottomOrderSheet from "@/components/orders/BottomOrderSheet";

export default {
  name: "Home",
  components: { BottomOrderSheet },
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
        { text: "Low", value: "low", filterable: false },
        { text: "", value: "is_favourite" }
      ],
      instruments: this.$store.getters.get_instruments
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
      this.dialog = !this.dialog;
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
        this.$store.dispatch(
          "show_snackbar",
          "Removed " + item.vendor + " " + item.name + " from favourites"
        );
      } else {
        add_to_favourites(item).then(res => {
          console.log(res);
        });
        this.$store.dispatch(
          "show_snackbar",
          "Added " + item.vendor + " " + item.name + " to favourites"
        );
      }
    }
  }
};
</script>
