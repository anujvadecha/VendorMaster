<template>
  <div class="q-ma-sm">
    <q-card square style="min-width: 400px" class="my-card" flat bordered>
      <q-card-actions align="right" class="">
        <div v-if="order.status==='EXECUTED'">
          <q-chip outline  color="green" dense >Payment confirmed</q-chip>
          <q-chip outline color="blue" dense >OTP:{{order.otp}}</q-chip>
        </div>
        <div v-if="order.status==='OPEN'">
          <q-chip outline  color="blue" dense >Waiting for payment</q-chip>
        </div>
        <div v-if="order.status==='WAITING_FOR_LIMIT'">
          <q-chip outline  color="blue" dense >Limit Order waiting</q-chip>
          <q-btn @click="cancel_limit_order()" outline  color="black" dense >CANCEL</q-btn>
        </div>
        <div v-if="order.status==='CLOSED'">
          <q-chip outline  color="green" dense >Closed</q-chip>
        </div>
        </q-card-actions>
      <q-separator/>
      <div class="row q-ma-sm">
          <div class="col">
            <span style=" font-weight: bold;color:darkblue;font-size: large">{{order.instrument.vendor}}</span>
            <span class="font-bold q-ml-xs-sm " style="font-size: large"> {{order.instrument.name}}</span>
          </div>
          <div class="col">
            <div class="text-right align-right">
                <div class="col text-right">Price:{{order.price}}</div>
            </div>
          </div>
      </div>
      <div class="row q-ma-sm">
        <div class="col"><q-chip dense outline color="orange">{{order.side}} </q-chip> {{order.quantity}}
            </div>
                <span class="q-ml-sm" style="color: grey"> B:{{order.instrument.bid}} A:{{order.instrument.ask}}</span>
      </div>
    </q-card>
  </div>
</template>

<script>
import { cancel_order } from 'src/common/api_calls'
export default {
  name: 'OrderItem',
  props: ['order'],
  methods: {
    cancel_limit_order () {
      console.log('limit order cancellation request for' + this.order)
      cancel_order({ order_id: this.order.order_id })
    }
  }
}
</script>

<style scoped>

</style>
