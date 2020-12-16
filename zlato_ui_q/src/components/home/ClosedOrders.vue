<template>
  <div class="row">
    <div v-for="order in closed" :key="order.order_id">
      <OrderItem :order="order"></OrderItem>
    </div>
  </div>
</template>

<script>
import OrderItem from 'components/OrderItem'
export default {
  name: 'ClosedOrders',
  components: { OrderItem },
  props: ['closed']
}
</script>

<style scoped>

</style>
