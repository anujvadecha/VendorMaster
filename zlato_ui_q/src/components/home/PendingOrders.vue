<template>
  <div class="row">
    <div v-for="order in pending" :key="order.order_id">
      <OrderItem :order="order"></OrderItem>
    </div>
  </div>
</template>

<script>
import OrderItem from 'components/OrderItem'
export default {
  name: 'PendingOrders',
  components: { OrderItem },
  props: ['pending']
}
</script>

<style scoped>

</style>
