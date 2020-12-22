<template>
  <div>
  <div v-if="waiting.length>0 || confirmed.length>0">
    <div class="">
      <OrderItemTable :orders="confirmed" title="Confirmed"></OrderItemTable>
      <OrderItemTable :orders="waiting" title="Waiting"></OrderItemTable>
    </div>
  </div>
    <div v-else>
<div class="row align-middle">
    <div class="center">
      <q-img class="q-ml-lg" width="200px" src="/Human.png"></q-img>
    </div>
      <q-card class="q-ma-md">
      <div class="text-h6 font-bold q-ma-lg">No Executed orders</div>
      <div class=" q-ma-lg">To place an order. Please go to  <q-btn @click="$router.push('Home')">Home</q-btn></div>
      </q-card>
    </div>
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
    console.log(this.waiting.length)
    console.log(this.confirmed.length)
  }
}
</script>

<style scoped>

</style>
