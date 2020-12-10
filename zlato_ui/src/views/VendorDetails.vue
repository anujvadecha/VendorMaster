<template>
  <div>
    <v-container>
      <v-card height="100%" width="100%">
        <v-list-item
          v-bind:style="{
            'background-image':
              'url(' + vendor_object.vendor.theme.background_image + ')',
            backgroundSize: '100%',
            height: '30%',
            'max-height': '200px',
            backgroundColor: vendor_object.vendor.theme.css_header__color
          }"
          three-line
        >
          <v-list-item-content>
            <div class="overline mb-4"></div>
            <v-list-item-title
              v-bind:style="{
                color: vendor_object.vendor.theme.css_header_text_color
              }"
              class="headline mb-1 font-weight-bold"
            >
              {{ vendor_object.vendor.name }}
            </v-list-item-title>
            <v-list-item-subtitle
              v-bind:style="{
                color: vendor_object.vendor.theme.css_header_text_color
              }"
              >{{ vendor_object.vendor.email }}</v-list-item-subtitle
            >
          </v-list-item-content>
          <v-list-item-avatar tile size="80">
            <img
              max-height="150"
              max-width="250"
              :src="vendor_object.vendor.theme.logo"
            />
          </v-list-item-avatar>
        </v-list-item>

        <v-card tile>
          <v-card-title>Symbols</v-card-title>
          <v-card-subtitle
            >Please click on bid or ask to place order</v-card-subtitle
          >
          <v-data-table
            :headers="headers"
            :items="vendor_object.instruments"
            loading-text="Loading... Please wait"
            hide-default-footer
          >
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
        <v-card tile>
          <v-card-title>Messages</v-card-title>
          <v-card-text>
            {{ vendor_object.vendor.vendor_details.messages }}
          </v-card-text>
        </v-card>
        <v-card tile>
          <v-card-title>Company Info</v-card-title>
          <v-tabs>
            <v-tab>About us</v-tab>
            <v-tab>Contact Details</v-tab>
            <v-tab>Delivery charges</v-tab>
            <v-tab-item>
              <v-card tile flat class="ma-2">
                <span
                  v-html="vendor_object.vendor.vendor_details.about_us"
                ></span>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card tile flat class="ma-2">
                <span
                  v-html="vendor_object.vendor.vendor_details.contact_details"
                ></span>
              </v-card>
            </v-tab-item>
            <v-tab-item class="ma-2">
              <v-card tile flat>
                <span
                  v-html="vendor_object.vendor.vendor_details.delivery_charges"
                ></span>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-card>
        <v-card tile>
          <v-card-title>Ratings</v-card-title>
        </v-card>
      </v-card>
    </v-container>
    <BottomOrderSheet :selected_item="selected_item"></BottomOrderSheet>
  </div>
</template>

<script>
import BottomOrderSheet from "@/components/orders/BottomOrderSheet";

export default {
  name: "VendorDetails",
  props: ["vendor_object", "vendor"],
  components: { BottomOrderSheet },
  data() {
    return {
      headers: [
        { text: "Symbol", value: "name" },
        { text: "Bid", value: "bid", filterable: false },
        { text: "Ask", value: "ask", filterable: false },
        { text: "High", value: "high", filterable: false },
        { text: "Low", value: "low", filterable: false }
      ],
      selected_item: null
    };
  },
  methods: {
    open_order_sheet: function(item) {
      this.$store.dispatch("set_sheet", true);
      this.selected_item = item;
    }
  }
};
</script>

<style scoped></style>
