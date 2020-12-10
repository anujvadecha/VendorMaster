<template>
  <v-dialog max-width="700px" persistent v-model="get_set_sheet" inset>
    <v-sheet v-model="get_set_sheet" style>
      <v-card dark tile color="light-blue">
        <v-container fluid>
          <div v-if="selected_item">
            <v-row>
              <v-col v-if="selected_item">
                <span class="font-weight-bold">{{ selected_item.vendor }}</span>
                <span class="ml-2">{{ selected_item.name }}</span>
              </v-col>
              <!--              <v-col>-->

              <!--              </v-col>-->

              <v-col class="text-right">
                <span class="ml-2">Bid: {{ selected_item.bid }}</span>
                <span class="ml-2">Ask: {{ selected_item.ask }}</span>

                <!--                <v-btn @click="close_sheet()">Cancel</v-btn>-->
              </v-col>
            </v-row>
            <v-row no-gutters>
              <!--              <v-switch-->
              <!--                v-model="order_switch"-->
              <!--                style=""-->
              <!--                :label="get_order_side"-->
              <!--                color="white"-->
              <!--                dark-->
              <!--              ></v-switch>-->
              <!--              <su-switch-->
              <!--                class="mt-2 text-right"-->
              <!--                v-model="order"-->
              <!--                state-on-label="Sell"-->
              <!--                state-off-label="Buy"-->
              <!--                state-on="SELL"-->
              <!--                state-off="BUY"-->
              <!--                style="color: white"-->
              <!--              >-->
              <!--              </su-switch>-->
            </v-row>
          </div>
        </v-container>
      </v-card>
      <v-card> </v-card>
      <v-card>
        <v-tabs>
          <v-tab>Market</v-tab>
          <v-tab>Limit</v-tab>
          <v-tab-item>
            <OrderFormBottom
              type="MARKET"
              :item="selected_item"
              :side="side"
            ></OrderFormBottom>
          </v-tab-item>
          <v-tab-item>
            <OrderFormBottom
              type="LIMIT"
              :side="side"
              :item="selected_item"
            ></OrderFormBottom>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-sheet>
  </v-dialog>
</template>

<script>
import OrderFormBottom from "@/components/orders/OrderFormBottom";
// import { Switch } from "slim-ui";
export default {
  name: "BottomOrderSheet",
  components: { OrderFormBottom },
  props: ["selected_item"],
  data() {
    return { side: "BUY", order: "BUY", order_switch: false };
  },
  computed: {
    get_set_sheet: function() {
      return this.$store.getters.get_sheet;
    },
    get_order_side: function() {
      if (this.order_switch == false) {
        return "SELL";
      } else {
        return "BUY";
      }
    }
  },
  methods: {
    close_sheet: function() {
      this.$store.dispatch("set_sheet", false);
    }
  }
};
</script>

<style scoped></style>
