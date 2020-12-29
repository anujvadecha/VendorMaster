<template>
  <OrderItemTable :orders="pending" ></OrderItemTable>
</template>

<script>
import OrderItemTable from 'components/OrderItemTable'
export default {
  name: 'PendingOrders',
  components: { OrderItemTable },
  props: ['pending']
}
</script>
