<template>
  <div class="row">
  <div v-for="order in waiting" :key="order.order_id">
    <OrderItem :order="order"></OrderItem>
  </div>
  <div v-for="order in confirmed" :key="order.order_id">
    <OrderItem :order="order"></OrderItem>
  </div>
    </div>

</template>

<script>
import OrderItem from 'components/OrderItem'
export default {
  name: 'ExecutedOrders',
  props: ['confirmed', 'waiting'],
  components: { OrderItem },
  created () {
  }
}
</script>

<style scoped>

</style>
