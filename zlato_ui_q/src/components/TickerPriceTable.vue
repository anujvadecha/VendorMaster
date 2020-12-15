<template>
<q-table
      title="Ticker Prices"
      :data="instruments_to_render"
      :columns="headers"
      row-key="name"
      bordered flat
    >
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th>
            Vendor
          </q-th>
          <q-th>
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
          <q-td key="Vendor" :props="props">
            {{ props.row.vendor }}
          </q-td>
          <q-td key="Symbol" :props="props">
              {{ props.row.name }}
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
      console.log('toggle fav for item' + item)
      item.is_favourite = !item.is_favourite
      // if (item.is_favourite === false) {
      //   remove_from_favourites(item.instrument_id).then(res => {
      //     console.log(res)
      //   })
      //   this.errorToast(
      //     'Removed ' + item.vendor + ' ' + item.name + ' from favourites'
      //   )
      // } else {
      //   add_to_favourites(item).then(res => {
      //     console.log(res)
      //   })
      //   this.successToast(
      //     'Added ' + item.vendor + ' ' + item.name + ' from favourites'
      //   )
    },
    open_order_sheet: function (item) {
      console.log('open order sheet called')
      this.$store.dispatch('set_order_item', item)
      this.$store.dispatch('set_sheet', true)
    }
  }
}
</script>

<style scoped>

</style>
