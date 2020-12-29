<template>
  <div v-if="orders.length>0">
  <q-table
      grid
      card-class="bg-primary text-white"
      :title="title"
      :data='orders'
      row-key="name"
      :filter="filter"
      hide-header
      hide-no-data
      >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
      <template v-slot:item="props">
      <div class="q-pa-xs col-xs-12 col-sm-12 col-md-6">
          <q-card>
            <OrderItem :order="props.row"></OrderItem>
          </q-card>
      </div>
      </template>
    </q-table>
    </div>
  <div v-else>
    <div class="row align-middle">
    <div class="center">
      <q-img class="q-ml-lg" width="200px" src="/Human.png"></q-img>
    </div>
      <q-card class="q-ma-md">
      <div class="text-h6 font-bold q-ma-lg">No {{title }} orders</div>
      <div class=" q-ma-lg">To place an order. Please go to <q-btn @click="$router.push('Home')">Home</q-btn></div>
      </q-card>
    </div>
  </div>
</template>

<script>
import OrderItem from 'components/OrderItem'
export default {
  name: 'OrderItemTable',
  components: { OrderItem },
  props: ['orders', 'title'],
  data: function () {
    return {
      filter: ''
    }
  }
}
</script>

<style scoped>

</style>
