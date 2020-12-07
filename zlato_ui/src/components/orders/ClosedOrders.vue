<template>
  <v-container>
    <div v-for="closed_order in closed_orders" :key="closed_order.order_id">
      <ClosedOrder v-bind:closed_order="closed_order" />
    </div>
  </v-container>
</template>
<script>
import ClosedOrder from "@/components/orders/ClosedOrder";
export default {
  components: { ClosedOrder },
  name: "ClosedOrders",
  props: ["closed_orders"]
};
</script>

<style scoped></style>
