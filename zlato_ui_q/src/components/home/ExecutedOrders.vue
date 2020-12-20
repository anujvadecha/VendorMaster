<template>
  <div>
    <div class="">
      <OrderItemTable :orders="confirmed" title="Confirmed"></OrderItemTable>
      <OrderItemTable :orders="waiting" title="Waiting"></OrderItemTable>
    </div>
  </div>
</template>

<script>
import OrderItemTable from 'components/OrderItemTable'
export default {
  name: 'ExecutedOrders',
  props: ['confirmed', 'waiting'],
  components: { OrderItemTable },
  created () {
  }
}
</script>

<style scoped>

</style>
