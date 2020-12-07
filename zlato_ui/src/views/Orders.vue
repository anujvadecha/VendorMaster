<template>
  <div class="orders">
    <v-card>
      <v-card-title>Orders</v-card-title>
      <v-tabs horizontal>
        <v-tab>
          <!--          <v-icon left>mdi-circle</v-icon>-->
          Executed
        </v-tab>
        <v-tab>
          <!--          <v-icon>mdi-</v-icon>-->
          Open
        </v-tab>
        <v-tab>
          <!--          <v-icon>mdi-access-point</v-icon>-->
          Previous
        </v-tab>
        <v-tab-item>
          <ExecutedOrders
            v-bind:executed_orders_confirmed="executed_orders_confirmed"
            v-bind:executed_orders_waiting="executed_orders_waiting"
          />
        </v-tab-item>
        <v-tab-item>
          <ActiveOrders v-bind:active_orders="active_orders" />
        </v-tab-item>
        <v-tab-item>
          <ClosedOrders v-bind:closed_orders="closed_orders" />
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
import ActiveOrders from "../components/orders/ActiveOrders";
import ExecutedOrders from "../components/orders/ExecutedOrders";
import ClosedOrders from "@/components/orders/ClosedOrders";
import { get_orders } from "@/common/api_calls";

export default {
  name: "Orders",
  components: {
    ActiveOrders,
    ExecutedOrders,
    ClosedOrders
  },
  data() {
    return {
      model: 1,
      orders: [],
      active_orders: [],
      executed_orders_confirmed: [],
      executed_orders_waiting: [],
      closed_orders: []
    };
  },
  created() {
    get_orders()
      .then(res => {
        this.orders = res;
      })
      .then(() => {
        console.log(this.orders);
        this.orders.map(order => {
          order.instrument = this.$store.getters.get_instrument(
            order.instrument_id
          );
        });
      })
      .then(() => {
        this.active_orders = this.orders.filter(order => {
          return order.status === "WAITING_FOR_LIMIT";
        });
        this.executed_orders_waiting = this.orders.filter(order => {
          return order.status === "OPEN";
        });
        this.executed_orders_confirmed = this.orders.filter(order => {
          return order.status === "EXECUTED";
        });
        this.closed_orders = this.orders.filter(order => {
          return order.status === "CLOSED";
        });
      });
  }
};
</script>

<style scoped>
.orders {
  color: black;
}
</style>
