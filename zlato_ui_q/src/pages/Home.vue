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
  <TopVendors class="mobile-hide"  :vendors="vendors_computed"></TopVendors>
  <TickerPriceTable title="Ticker prices" :instruments_to_render="instruments_to_render"></TickerPriceTable>
  <MobileMarketing></MobileMarketing>
  </div>
</template>
<script>
import TopVendors from 'components/home/TopVendors'
import TickerPriceTable from 'components/TickerPriceTable'
import { add_to_favourites, remove_from_favourites } from 'src/common/api_calls'
import MobileMarketing from 'components/MobileMarketing'
// import { add_to_favourites, remove_from_favourites } from '@/common/api_calls'

export default {
  name: 'Home',
  components: { MobileMarketing, TickerPriceTable, TopVendors },
  data () {
    return {
      slide: 'gold 999',
      g99instruments: [],
      g991instruments: [],
      g95instruments: [],
      g951instruments: [],
      tab: 'All',
      headers: [
        { name: 'Vendor', align: 'start', field: 'vendor', label: 'Vendor' },
        { name: 'Symbol', align: 'start', field: 'name', label: 'Symbol' },
        { name: 'Bid', align: 'start', field: 'bid', filterable: true, label: 'Bid' },
        { name: 'Ask', align: 'start', field: 'ask', filterable: true, label: 'Ask' },
        { name: 'High', align: 'start', field: 'high', filterable: true, label: 'High' },
        { name: 'Low', align: 'start', field: 'low', filterable: true, label: 'Low' },
        { name: 'favourite', align: 'start', field: 'is_favourite', label: '' }
      ]
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
          console.log(res)
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
    }
  },
  created () {
  }
}

</script>

<style scoped>

  /* .table-chips{
    background-color:"deep-purple-7";
    color: "white";
  } */

</style>
