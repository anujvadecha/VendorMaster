<template>
  <div class="">
    <div v-if="confirmed.length>0 || waiting.length>0">
  <div v-for="order in waiting" :key="order.order_id">
    <OrderItem :order="order"></OrderItem>
  </div>
  <div v-for="order in confirmed" :key="order.order_id">
    <OrderItem :order="order"></OrderItem>
  </div>
    </div>
    <div v-else>
    No executed orders
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
