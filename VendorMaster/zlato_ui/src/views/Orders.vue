<template>
  <div class="orders">
    <!--    <v-container fluid>-->
    <v-card>
      <v-card-title>Orders</v-card-title>
      <v-tabs horizontal>
        <v-tab>
          Executed
        </v-tab>
        <v-tab>
          Open
        </v-tab>
        <v-tab>
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
    <!--    </v-container>-->
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
        this.orders.map(order => {
          order.instrument = this.$store.getters.get_instrument(
            order.instrument_id
          );
        });
      })
      .then(() => {
        this.orders.sort((a, b) => {
          // console.log(new Date(a.created_at) - new Date(b.created_at));
          return new Date(b.created_at) - new Date(a.created_at);
        });
      })
      .then(() => {
        this.active_orders = this.orders.filter(order => {
          return order.status === "WAITING_FOR_LIMIT";
        });
        this.executed_orders_waiting = this.orders.filter(order => {
          return order.status === "OPEN";
        });
        // for(let i=0; i<this.executed_orders_waiting.length; i++) {
        //   console.log(this.executed_orders_waiting[i]);
        // }
        this.executed_orders_waiting.sort((a, b) => {
          // console.log(new Date(a.created_at) - new Date(b.created_at));
          return new Date(b.created_at) - new Date(a.created_at);
        });
        // for(let i=0; i<this.executed_orders_waiting.length; i++) {
        //   console.log(this.executed_orders_waiting[i]);
        // }
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
