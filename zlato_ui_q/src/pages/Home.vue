<template>
  <div>
  <div class="">
    <div v-if="logged_in">
  <q-card square v-if="!$store.state.is_activated" class="" >
    <div class="q-pa-sm bg-primary">
      <div class="text-white" style="font-weight: bold">
      <div v-if="$store.state.requested_registration">We will register this account as soon as possible</div>
      <div v-else><q-btn  @click="$router.push('Registration')" class="text-black bg-white"> Activate </q-btn> &nbsp; your account to place orders</div>
     </div>
    </div>
    </q-card>
    </div>
  </div>
<!--  <q-btn @click="filter_dialog">Filters</q-btn>-->
    <div v-if="orders_to_rate.length > 0">
      <div v-for="order in orders_to_rate" :key="order.order_id">
        <Rating v-bind:data="[order, true]" />
      </div>
    </div>
    <q-dialog style="" v-model="filter"  persistent>
    <q-card class="" style="">
<!--      <q-card-section class="bg-primary text-h6" style=" color: white" >-->
<!--        Filters-->
<!--      </q-card-section>-->
      <q-card-section>

      </q-card-section>
       <q-card-section style="background-color: white" >
      <q-btn class="q-ml-md btn-danger" @click="filter=false">Close</q-btn>
      <q-btn class="q-ml-md btn-primary" color="primary" @click="setFilters">Apply Filters</q-btn>
    </q-card-section>
    </q-card>
  </q-dialog>
  <TickerPriceTable :render_best="true" title="Bullion prices" :instruments_to_render="instruments_to_render"></TickerPriceTable>
    <TopVendors class="mobile-hide"  :vendors="vendors_computed"></TopVendors>
    <div class="row">
    <MobileMarketing></MobileMarketing>
      </div>
  </div>

</template>
<script>
import TopVendors from 'components/home/TopVendors'
import TickerPriceTable from 'components/TickerPriceTable'
import { add_to_favourites, remove_from_favourites, get_orders } from 'src/common/api_calls'
import MobileMarketing from 'components/MobileMarketing'
// import { add_to_favourites, remove_from_favourites } from '@/common/api_calls'
import Rating from 'components/Rating'

export default {
  name: 'Home',
  components: { MobileMarketing, TickerPriceTable, TopVendors, Rating },
  data () {
    return {
      slide: 'gold 999',
      tab: 'All',
      filter: false,
      headers: [
        { name: 'Vendor', align: 'start', field: 'vendor', label: 'Vendor' },
        { name: 'Symbol', align: 'start', field: 'name', label: 'Symbol' },
        { name: 'Bid', align: 'start', field: 'bid', filterable: true, label: 'Bid' },
        { name: 'Ask', align: 'start', field: 'ask', filterable: true, label: 'Ask' },
        { name: 'High', align: 'start', field: 'high', filterable: true, label: 'High' },
        { name: 'Low', align: 'start', field: 'low', filterable: true, label: 'Low' },
        { name: 'favourite', align: 'start', field: 'is_favourite', label: '' }
      ],
      orders_to_rate: [],
      orders: []
    }
  },
  computed: {
    instruments_to_render: function () {
      return this.$store.getters.get_instruments
    },
    bottom_sheet: function () {
      return this.$store.getters.get_sheet
    },
    vendors_computed: function () {
      return this.$store.getters.get_all_vendors
    },
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        return false
      } else {
        return true
      }
    }
  },
  methods: {
    setFilters: function () {},
    toggleFavourite: function (item) {
      item.is_favourite = !item.is_favourite
      if (item.is_favourite === false) {
        remove_from_favourites(item.instrument_id).then(res => {
          this.$q.notify({
            message: 'Removed ' + item.vendor + ' ' + item.name + ' from favourites',
            timeout: 2000,
            position: 'top-right',
            color: 'primary'
          })
        })
      } else {
        add_to_favourites(item).then(res => {
          this.$q.notify({
            message: 'Added ' + item.vendor + ' ' + item.name + ' from favourites',
            timeout: 2000,
            position: 'top-right',
            color: 'primary'
          })
        })
      }
    },
    open_order_sheet: function (item) {
      console.log('open order sheet called')
      this.$store.dispatch('set_order_item', item)
      this.$store.dispatch('set_sheet', true)
    },
    filter_dialog () {
      this.filter = !this.filter
    },
    get_orders () {
      return get_orders().then(res => {
        this.orders = res
        console.log('Inside get_orders')
      })
        .then(() => {
          this.orders = this.orders.map(order => {
            order.instrument_id = this.$store.getters.get_instrument(
              order.instrument_id
            )
            return order
          })
        })
        .then(() => {
          this.orders_to_rate = this.orders.filter(order => {
            return order.status === 'CLOSED' && order.is_rated === false
          })
        })
    }
  },
  created () {
    this.get_orders()
  }
}

</script>

<style scoped>

  /* .table-chips{
    background-color:"deep-purple-7";
    color: "white";
  } */

</style>
