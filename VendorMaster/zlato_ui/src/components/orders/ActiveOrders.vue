<template>
  <v-container>
    <div
      v-bind:key="active_order.order_id"
      v-for="active_order in active_orders"
    >
      <ActiveOrderItem v-bind:active_order="active_order" />
    </div>
  </v-container>
</template>

<script>
import ActiveOrderItem from "./ActiveOrderItem";

export default {
  name: "ActiveOrders",
  props: ["active_orders"],
  components: {
    ActiveOrderItem
  }
};
</script>

<style scoped></style>
