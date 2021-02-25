<template>
<div>
  <q-pull-to-refresh @refresh="refresher">
    <div v-if="$store.state.orders_to_rate.length > 0">
      <div v-for="order in $store.state.orders_to_rate" :key="order.order_id">
        <Rating v-bind:data="[order.instrument_id.vendor_id, order.instrument_id.vendor, true]" />
      </div>
    </div>
  <div class="">
    <div class="q-gutter-y-md" style="">
      <q-card flat >
        <q-tabs
          v-model="tab"
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
          stretch
        >
          <q-tab name="executed" label="Executed" />
          <q-tab name="pending" label="Pending" />
          <q-tab name="closed" label="Closed" />
        </q-tabs>
        <q-separator />
        <q-tab-panels swipeable v-model="tab" animated>
          <q-tab-panel name="executed">
            <ExecutedOrders :waiting="$store.state.executed_orders_waiting" :confirmed="$store.state.executed_orders_confirmed"></ExecutedOrders>
          </q-tab-panel>
          <q-tab-panel name="pending">
            <PendingOrders :pending="$store.state.active_orders" :refresh="this.refresher"></PendingOrders>
          </q-tab-panel>
          <q-tab-panel name="closed">
            <ClosedOrders :closed="$store.state.closed_orders"></ClosedOrders>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
  </q-pull-to-refresh>
</div>
</template>
<script>
import ExecutedOrders from 'components/home/ExecutedOrders'
import PendingOrders from 'components/home/PendingOrders'
import ClosedOrders from 'components/home/ClosedOrders'
import Rating from 'components/Rating'
import { get_orders } from 'src/common/api_calls'

export default {
  name: 'Orders',
  components: { ClosedOrders, PendingOrders, ExecutedOrders, Rating },
  data () {
    return {
      tab: 'executed'
    }
  },
  methods: {
    refresher (done) {
      get_orders().then(res => {
        this.$store.dispatch('set_orders', res)
      })
      done()
    },
    set_orders () {
      console.log('Setting orders')
    }
  },
  created () {
    this.$store.state.rightDrawerOpen = false
    get_orders().then(res => {
      store.dispatch('set_orders', res)
    })
  }

}
</script>

<style scoped>

</style>
