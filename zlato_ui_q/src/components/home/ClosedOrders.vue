<template>
  <OrderItemTable :show_illustration="true" :orders="closed"></OrderItemTable>
</template>

<script>
import OrderItemTable from 'components/OrderItemTable'
export default {
  name: 'ClosedOrders',
  components: { OrderItemTable },
  props: ['closed']
}
</script>

<style scoped>

</style>
