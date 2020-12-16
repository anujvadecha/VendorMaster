<template>
<q-table
      title="Ticker Prices"
      :data="instruments_to_render"
      :columns="headers"
      row-key="name"
      bordered flat
    >
      <template v-slot:header="props">
        <q-tr class="text-left"  :props="props">
          <q-th  v-if="!$q.platform.is.mobile">
            Vendor
          </q-th>
          <q-th >
            Symbol
          </q-th>
          <q-th>
            Bid
          </q-th>
          <q-th>
            Ask
          </q-th>
          <q-th v-if="!$q.platform.is.mobile">
            High
          </q-th>
          <q-th v-if="!$q.platform.is.mobile">
            Low
          </q-th>
          <q-th>
            Favourite
          </q-th>
          <q-th>
          </q-th>
        </q-tr>
      </template>
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td class="vendor_link" @click="open_vendor_dialog(props.row.vendor_id)" v-if="!$q.platform.is.mobile" key="Vendor" :props="props">
            {{ props.row.vendor }}
          </q-td>
          <q-td @click="open_vendor_dialog(props.row.vendor_id)" key="Symbol" :props="props">
            <div v-if="$q.platform.is.mobile">
              <div class="col">
                <div class="row vendor_link" >
                   <span style="font-size:small"> {{ props.row.vendor }}</span>
                </div>
                <div class="row">
                  <span style="font-size:small">{{props.row.name}}</span>
                </div>
              </div>
            </div>
            <div v-else>
              {{ props.row.name }}
            </div>
          </q-td>
          <q-td @click="open_order_sheet(props.row)" key="Bid" :props="props">
            <div v-if="$q.platform.is.mobile">
              <div class="col">
                <div class="row">
                   <span style="font-size:large"> {{ props.row.bid }}</span>
                </div>
                <div class="row">
                  <span style="font-size:small">L:{{props.row.low}}</span>
                </div>
              </div>
            </div>
            <div v-else>
              {{ props.row.bid }}
            </div>
          </q-td>
          <q-td @click="open_order_sheet(props.row)" key="Ask" :props="props">
            <div v-if="$q.platform.is.mobile">
              <div class="col">
                <div class="row">
                   <span style="font-size:large"> {{ props.row.ask }}</span>
                </div>
                <div class="row">
                  <span style="font-size:small">H:{{props.row.high}}</span>
                </div>
              </div>
            </div>
            <div v-else>
              {{ props.row.ask }}
              </div>
          </q-td>
          <q-td v-if="!$q.platform.is.mobile" key="High" :props="props">
              {{ props.row.high }}
          </q-td>
          <q-td v-if="!$q.platform.is.mobile" key="Low" :props="props">
              {{ props.row.low }}
          </q-td>
          <q-td @click ="toggleFavourite(props.row)" key='favourite' :props="props">
            <div v-if="props.row.is_favourite">
              <q-icon size="sm" name="mdi-star"/>
            </div>
            <div v-else>
              <q-icon size="sm" name="mdi-star-outline"/>
            </div>
          </q-td>
        </q-tr>
      </template>
    </q-table>
</template>

<script>
import { add_to_favourites, remove_from_favourites } from 'src/common/api_calls'

export default {
  name: 'TickerPriceTable',
  props: ['instruments_to_render'],
  data () {
    return {
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
  methods: {
    toggleFavourite: function (item) {
      console.log(item)
      item.is_favourite = !item.is_favourite
      if (item.is_favourite === false) {
        remove_from_favourites(item.instrument_id).then(res => {
          console.log(res)
        })
        // this.errorToast(
        //   'Removed ' + item.vendor + ' ' + item.name + ' from favourites'
        // )
      } else {
        add_to_favourites(item).then(res => {
          console.log(res)
        })
        // this.successToast(
        //   'Added ' + item.vendor + ' ' + item.name + ' from favourites'
        // )
      }
    },
    open_order_sheet: function (item) {
      console.log('open order sheet called')
      this.$store.dispatch('set_order_item', item)
      this.$store.dispatch('set_sheet', true)
    },
    open_vendor_dialog: function (vendor_id) {
      console.log('open vendor called')
      var selected_vendor_item = this.$store.getters.get_vendor_instruments(
        vendor_id
      )
      this.$router.push({
        name: 'Vendor',
        params: {
          vendor_object: selected_vendor_item
        }
      })
    }
  }

}
</script>

<style scoped>
  .vendor_link{
    color: darkblue;
  }
</style>
