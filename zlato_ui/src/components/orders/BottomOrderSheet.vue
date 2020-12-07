<template>
  <v-bottom-sheet v-model="get_set_sheet" inset>
    <v-sheet style="max-width: 700px">
      <v-card dark tile color="#FF8F00">
        <v-container fluid>
          <div v-if="selected_item">
            <v-row>
              <v-col v-if="selected_item">
                <!--              <v-if></v-if>-->
                <span class="font-weight-bold">{{ selected_item.vendor }}</span>
                <span class="ml-2">{{ selected_item.name }}</span>
                <!--              {{selected_item }}-->
              </v-col>
              <!--              <v-col>-->
              <!--                <v-switch-->
              <!--                  style="height: 10px"-->
              <!--                  :label="side"-->
              <!--                  color="primary"-->
              <!--                ></v-switch>-->
              <!--              </v-col>-->
              <v-col class="text-right">
                <span class="ml-2">Bid: {{ selected_item.bid }}</span>
                <span class="ml-2">Ask: {{ selected_item.ask }}</span>
                <!--                <v-btn @click="close_sheet()">Cancel</v-btn>-->
              </v-col>
            </v-row>
          </div>
        </v-container>
      </v-card>
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
  </v-bottom-sheet>
</template>

<script>
import OrderFormBottom from "@/components/orders/OrderFormBottom";
export default {
  name: "BottomOrderSheet",
  components: { OrderFormBottom },
  props: ["selected_item"],
  data() {
    return { side: "BUY" };
  },
  computed: {
    get_set_sheet: function() {
      return this.$store.getters.get_sheet;
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
