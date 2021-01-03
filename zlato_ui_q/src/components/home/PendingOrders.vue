<template>
  <div>
  <OrderItemTable :orders="pending_orders" :show_illustration="true" title="Pending limit"></OrderItemTable>
  <OrderItemTable :orders="[]" :show_illustration="false" title="Pending Best limit" :best_limit_orders="best_limit"></OrderItemTable>
</div>
</template>

<script>
import OrderItemTable from 'components/OrderItemTable'
export default {
  name: 'PendingOrders',
  components: { OrderItemTable },
  props: ['pending'],
  data: function () {
    return {
      pending_orders: [],
      best_limit: []
    }
  },
  created () {
    var best_limit_map = {}
    this.pending.map(pending => {
      if (pending.type === 'BEST_LIMIT') {
        if (pending.best_limit_id in best_limit_map) {
          best_limit_map[pending.best_limit_id].push(pending)
        } else {
          best_limit_map[pending.best_limit_id] = []
          best_limit_map[pending.best_limit_id].push(pending)
        }
      } else {
        this.pending_orders.push(pending)
      }
    })
    for (var key in best_limit_map) {
      var item = { best_limit_id: key, orders: best_limit_map[key] }
      this.best_limit.push(item)
    }
    // this.best_limit = best_limit_map
    // console.log(best_limit_map)
  }
}
</script>
