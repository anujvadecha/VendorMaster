<template>
  <div>
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
        :pagination="pagination"
      >
        <template v-slot:top-right>
          <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search"/>
            </template>
          </q-input>
        </template>
        <template v-slot:item="props">
          <div class="q-pa-xs col-xs-12 col-sm-12 col-md-6">
            <OrderItem :order="props.row"></OrderItem>
          </div>
        </template>
      </q-table>
    </div>
    <div v-else>
      <div v-if="show_illustration">
      <div class="row align-middle">
        <div class="center">
          <q-img class="q-ml-lg" width="200px" src="/Human.png"></q-img>
        </div>
        <q-card class="q-ma-md">
          <div class="text-h6 font-bold q-ma-lg">No {{title }} orders</div>
          <div class=" q-ma-lg">To place an order. Please go to
            <q-btn @click="$router.push('Home')">Home</q-btn>
          </div>
        </q-card>
      </div>
        </div>
    </div>
    <div v-if="best_limit_orders.length>0">
      <q-table
        grid
        card-class="bg-primary text-white"
        :title="title"
        :data='best_limit_orders'
        row-key="name"
        :filter="filter"
        hide-header
        hide-no-data
        :pagination="pagination"
      >
        <template v-slot:top-right>
          <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search"/>
            </template>
          </q-input>
        </template>
        <template v-slot:item="props">
          <div class="q-pa-xs col-xs-12 col-sm-12 col-md-6">
            <BestLimitOrderItem :order="props.row"></BestLimitOrderItem>
          </div>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
import OrderItem from 'components/OrderItem'
import BestLimitOrderItem from 'components/BestLimitOrderItem'

export default {
  name: 'OrderItemTable',
  components: { BestLimitOrderItem, OrderItem },
  props: ['orders', 'best_limit_orders', 'title', 'show_illustration'],
  data: function () {
    return {
      filter: '',
      pagination: {
        rowsPerPage: 0
      }
    }
  },
  created () {
    if (this.best_limit_orders === undefined) {
      this.best_limit_orders = []
    }
  }
}
</script>

<style scoped>

</style>
