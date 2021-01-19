<template>
<div>
  <q-pull-to-refresh @refresh="refresher">
    <div v-if="orders_to_rate.length > 0">
      <div v-for="order in orders_to_rate" :key="order.order_id">
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
            <ExecutedOrders :waiting="executed_orders_waiting" :confirmed="executed_orders_confirmed"></ExecutedOrders>
          </q-tab-panel>
          <q-tab-panel name="pending">
            <PendingOrders :pending="active_orders" :refresh="this.get_orders"></PendingOrders>
          </q-tab-panel>
          <q-tab-panel name="closed">
            <ClosedOrders :closed="closed_orders"></ClosedOrders>
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
import { get_orders } from 'src/common/api_calls'
import Rating from 'components/Rating'

export default {
  name: 'Orders',
  components: { ClosedOrders, PendingOrders, ExecutedOrders, Rating },
  data () {
    return {
      tab: 'executed',
      orders: [],
      active_orders: [],
      executed_orders_confirmed: [],
      executed_orders_waiting: [],
      closed_orders: [],
      orders_to_rate: []
    }
  },
  methods: {
    refresher (done) {
      this.get_orders().then(done())
    },
    get_orders () {
      return get_orders().then(res => {
        // this.executed_orders_confirmed.length = 0
        // this.executed_orders_waiting.length = 0
        // this.closed_orders.length = 0
        // this.active_orders.length = 0
        // this.orders.length = 0
        this.orders = res
        console.log(res)
      })
        .then(() => {
          this.orders = this.orders.map(order => {
            order.instrument = this.$store.getters.get_instrument(
              order.instrument_id
            )
            console.log(order.instrument)
            return order
          })
        })
        .then(() => {
          this.orders.sort((a, b) => {
          // console.log(new Date(a.created_at) - new Date(b.created_at));
            return new Date(b.created_at) - new Date(a.created_at)
          })
        })
        .then(() => {
          console.log('Timestamp : ')
          console.log(this.orders)
        })
        .then(() => {
          this.active_orders = this.orders.filter(order => {
            return order.status === 'WAITING_FOR_LIMIT'
          })
          this.executed_orders_waiting = this.orders.filter(order => {
            return order.status === 'OPEN'
          })
          this.executed_orders_waiting.sort((a, b) => {
            return new Date(b.created_at) - new Date(a.created_at)
          })
          this.executed_orders_confirmed = this.orders.filter(order => {
            return order.status === 'EXECUTED'
          })
          this.closed_orders = this.orders.filter(order => {
            return order.status === 'CLOSED'
          })
          this.orders_to_rate = this.orders.filter(order => {
            console.log(order.status)
            console.log(order.is_rated)
            return order.status === 'CLOSED' && order.is_rated === false
          })
          console.log(this.orders_to_rate)
        })
    }
  },
  created () {
    this.get_orders()
  }

}
</script>

<style scoped>

</style>
