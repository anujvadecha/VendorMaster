<template>
  <div>
    <v-card elevation="2px" class="ma-2" outlined>
      <v-row>
        <v-col>
          <v-text-field
            v-model="quantity"
            placeholder="Quantity"
            label="Quantity in gms"
            type="number"
            class="ml-2 "
            outlined
          ></v-text-field>
        </v-col>
        <v-col>
          <div v-if="market">
            <v-text-field
              disabled
              :placeholder="item.bid"
              label="Price"
              type="number"
              class="ml-2"
              outlined
            ></v-text-field>
          </div>
          <div v-if="!market">
            <v-text-field
              :placeholder="item.bid"
              label="Price"
              v-model="price"
              type="number"
              class="ml-2"
              outlined
            ></v-text-field>
          </div>
        </v-col>
      </v-row>
      <!--      <v-tabs color="orange" vertical>-->
      <!--        <v-tab>BUY</v-tab>-->
      <!--        <v-tab>SELL</v-tab>-->
      <!--        <v-tab-item>-->
      <!--          <div v-if="market">-->
      <!--            BUY FORM-->
      <!--          </div>-->
      <!--          <div v-else>-->
      <!--            BUY LIMIT FORM-->
      <!--          </div>-->
      <!--        </v-tab-item>-->
      <!--        <v-tab-item>-->
      <!--          <div v-if="market">-->
      <!--            SELL FORM-->
      <!--          </div>-->
      <!--          <div v-else>-->
      <!--            SELL LIMIT FORM-->
      <!--          </div>-->
      <!--        </v-tab-item>-->
      <!--      </v-tabs>-->
    </v-card>
    <v-card tile>
      <v-container fluid>
        <v-row no-gutters>
          <v-col cols="12" class="text-right">
            <!--            <v-btn outlined :color="get_color()">{{ side }}</v-btn>-->
            <v-btn dark elevation="0px" class="ml-2" color="blue">Place</v-btn>
            <v-btn outlined @click="set_sheet()" class="ml-2" color="blue"
              >Cancel</v-btn
            >
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
// import { Switch } from "slim-ui";
export default {
  name: "OrderFormBottom",
  props: ["type", "item", "side"],
  data() {
    return {
      order: "BUY",
      quantity: 0,
      price: 0
    };
  },
  computed: {
    market: function() {
      if (this.type == "MARKET") return true;
      else return false;
    }
  },
  methods: {
    set_sheet: function() {
      this.$store.dispatch("set_sheet", false);
    },
    increment() {
      this.quantity = parseInt(this.quantity, 10) + 1;
    },
    decrement() {
      this.quantity = parseInt(this.quantity, 10) - 1;
    }
  },
  components: {},
  created() {
    console.log(this.item);
  }
};
</script>

<style scoped></style>
