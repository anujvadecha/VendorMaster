<template>
  <div>
    <v-container style="">
      <!--      {{ executed_orders_waiting }}-->
      <!--      {{ // executed_orders_confirmed }}}-->
      <div
        v-for="executed_waiting in executed_orders_waiting"
        :key="executed_waiting.order_id"
      >
        <ExecutedOrderItemWaiting
          v-bind:executed_waiting="executed_waiting"
        ></ExecutedOrderItemWaiting>
      </div>
      <div
        v-for="executed_confirmed in executed_orders_confirmed"
        :key="executed_confirmed.order_id"
      >
        <ExecutedOrderItemConfirmed
          v-bind:executed_confirmed="executed_confirmed"
        ></ExecutedOrderItemConfirmed>
      </div>
    </v-container>
    <div class="text-xs-center">
      <v-dialog v-model="dialog" width="500">
        <!--        <template v-slot:activator="{ on }">-->
        <!--          <v-btn color="red lighten-2" dark v-on="on">-->
        <!--            Check status-->
        <!--          </v-btn>-->
        <!--        </template>-->

        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title>
            Order has been confirmed Waiting for payment
          </v-card-title>

          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
import ExecutedOrderItemConfirmed from "@/components/orders/ExecutedOrderItemConfirmed";
import ExecutedOrderItemWaiting from "@/components/orders/ExecutedOrderItemWaiting";
// import ExecutedOrderItemWaiting from "@/components/orders/ExecutedOrderItemWaiting";

export default {
  name: "ExecutedOrders",
  props: ["executed_orders_confirmed", "executed_orders_waiting"],
  components: { ExecutedOrderItemConfirmed, ExecutedOrderItemWaiting },
  data() {
    return {
      dialog: false
    };
  }
};
</script>
