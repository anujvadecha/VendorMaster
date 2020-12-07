<template>
  <div>
    <v-card elevation="2px" class="ma-2" outlined>
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
      <su-switch
        v-model="order"
        state-on-label="Sell"
        state-off-label="Buy"
        state-on="SELL"
        state-off="BUY"
      >
      </su-switch>
    </v-card>
    <v-card tile>
      <v-container fluid>
        <v-row no-gutters>
          <v-col cols="12" class="text-right">
            <!--            <v-btn outlined :color="get_color()">{{ side }}</v-btn>-->
            <v-btn dark elevation="0px" class="ml-2" color="orange"
              >Place</v-btn
            >
            <v-btn outlined @click="set_sheet()" class="ml-2" color="orange"
              >Cancel</v-btn
            >
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import { Switch } from "slim-ui";
export default {
  name: "OrderFormBottom",
  props: ["type", "item", "side"],
  data() {
    return {
      order: "BUY"
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
    }
  },
  components: {
    "su-switch": Switch
  },
  created() {
    console.log(this.item);
  }
};
</script>

<style scoped></style>
