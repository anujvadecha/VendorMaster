<template>
  <div>
    <div class="q-ml-md q-mr-md q-mt-md row text-h6" style="">
      <div class="col">
        <div v-if="title==null">
            Watchlist
        </div>
      <div v-else>
        {{title}}
      </div>
      </div>
      <div class="row justify-center">
<!--      <div class="row">-->
      <q-input v-if="search_selected" clearable @clear="search_selected=false" class="q-ml-sm" outlined dense debounce="300" v-model="filter" placeholder="Search" />
      <q-btn v-if="!search_selected" class="q-ml-sm" style="max-height:36px" dense icon="mdi-magnify" text-color='dark' color="white" @click="search_selected=true" />
      <q-btn class="q-ml-sm" style="max-height:36px" dense icon="mdi-filter" text-color='dark' color="white" @click="openFilterDrawer()" />
<!--      </div>-->
      </div>
    </div>
<!--      <div class="row q-ml-md">-->
<!--          Please click on Bid/Ask to place orders-->
<!--      </div>-->
    <div>
      <q-tabs
        v-model="tab"
        no-caps
        dense
        style="width: available">
        <div v-for="type in types" :key="type">
          <q-tab :name="type" :label="type" on/>
        </div>
      </q-tabs>
      </div>
       <q-card v-if="render_best && instruments_to_render.length>0"  square  bordered flat class="bg-light-blue-2 row q-pa-sm" style="" >
         <div style="" class="col-3 vendor_link" @click="open_vendor_dialog(lowest.vendor_id)" v-if="!$q.platform.is.mobile"  >
            Best : {{ lowest.vendor }}
          </div>
            <div class="col-6" v-if="$q.platform.is.mobile" @click="open_vendor_dialog(lowest.vendor_id)">
              <div class="q-pl-md ">
                <div class="row vendor_link" >
                   <span style="font-size:small">Best: {{ lowest.vendor }}</span>
                </div>
                <div class="row">
                  <span style="font-size:small">{{lowest.name}}</span>
                </div>
              </div>
            </div>
            <div v-else class="col" @click="open_vendor_dialog(lowest.vendor_id)" >
              {{ lowest.name }}
            </div>

          <div class="col" @click="open_order_sheet(lowest)"  >
            <div v-if="$q.platform.is.mobile">
                <div class="row">
                   <span style="font-size:large"> {{ lowest.bid }}</span>
                </div>
                <div class="row">
                  <span style="font-size:small">L:{{lowest.low}}</span>
              </div>
            </div>
            <div v-else >
              <div class="col">
              {{ lowest.bid }}
                </div>
            </div>
          </div>
          <div class="col" @click="open_order_sheet(lowest)" >
            <div v-if="$q.platform.is.mobile">
                <div class="row">
                   <span style="font-size:large"> {{ lowest.ask }}</span>
                </div>
                <div class="row">
                  <span style="font-size:small">H:{{lowest.high}}</span>
                </div>
            </div>
            <div v-else>
              {{ lowest.ask }}
              </div>
          </div>
          <div class="col" v-if="!$q.platform.is.mobile"  >
              {{ lowest.high }}
          </div>
          <div class="col" v-if="!$q.platform.is.mobile"  >
              {{ lowest.low }}
          </div>
<!--         <div class="col">Lowest</div>-->

<!--          <div class="col" @click ="toggleFavourite(lowest)" key='favourite' >-->
<!--            <div v-if="lowest.is_favourite">-->
<!--              <q-icon size="sm" name="mdi-star"/>-->
<!--            </div>-->
<!--            <div v-else>-->
<!--              <q-icon size="sm" name="mdi-star-outline"/>-->
<!--            </div>-->
<!--          </div>-->
        </q-card>
  <q-table
      style="max-height: 600px"
      class=""
      title="Ticker Prices"
      :data="data_render"
      :columns="headers"
      :filter="filter"
      row-key="instrument_id"
      bordered flat
      v-touch-swipe.mouse.horizontal="handleSwipe"
      :pagination="pagination"
      virtual-scroll
      hide-bottom
    >
    <template v-slot:top>

    </template>
<!--    <template v-slot:top-row style="">-->
<!--        <q-tr  class="col-span-full bg-light-blue-2 " style="" >-->
<!--            <q-td style="" class="vendor_link" @click="open_vendor_dialog(lowest.vendor_id)" v-if="!$q.platform.is.mobile" key="Vendor" >-->
<!--            {{ lowest.vendor }}-->
<!--            </q-td>-->
<!--            <q-td @click="open_vendor_dialog(lowest.vendor_id)" key="Symbol" >-->
<!--            <div v-if="$q.platform.is.mobile">-->
<!--              <div class="col">-->
<!--                <div class="row vendor_link" >-->
<!--                   <span style="font-size:small"> {{ lowest.vendor }}</span>-->
<!--                </div>-->
<!--                <div class="row">-->
<!--                  <span style="font-size:small">{{lowest.name}}</span>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div v-else>-->
<!--              {{ lowest.name }}-->
<!--            </div>-->
<!--          </q-td>-->
<!--          <q-td @click="open_order_sheet(lowest)" key="Bid" >-->
<!--            <div v-if="$q.platform.is.mobile">-->
<!--              <div class="col">-->
<!--                <div class="row">-->
<!--                   <span style="font-size:large"> {{ lowest.bid }}</span>-->
<!--                </div>-->
<!--                <div class="row">-->
<!--                  <span style="font-size:small">L:{{lowest.low}}</span>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div v-else>-->
<!--              {{ lowest.bid }}-->
<!--            </div>-->
<!--          </q-td>-->
<!--          <q-td @click="open_order_sheet(lowest)" key="Ask" >-->
<!--            <div v-if="$q.platform.is.mobile">-->
<!--              <div class="col">-->
<!--                <div class="row">-->
<!--                   <span style="font-size:large"> {{ lowest.ask }}</span>-->
<!--                </div>-->
<!--                <div class="row">-->
<!--                  <span style="font-size:small">H:{{lowest.high}}</span>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div v-else>-->
<!--              {{ lowest.ask }}-->
<!--              </div>-->
<!--          </q-td>-->
<!--          <q-td v-if="!$q.platform.is.mobile" key="High" >-->
<!--              {{ lowest.high }}-->
<!--          </q-td>-->
<!--          <q-td v-if="!$q.platform.is.mobile" key="Low" >-->
<!--              {{ lowest.low }}-->
<!--          </q-td>-->
<!--          <q-td @click ="toggleFavourite(lowest)" key='favourite' >-->
<!--            <div v-if="lowest.is_favourite">-->
<!--              <q-icon size="sm" name="mdi-star"/>-->
<!--            </div>-->
<!--            <div v-else>-->
<!--              <q-icon size="sm" name="mdi-star-outline"/>-->
<!--            </div>-->
<!--          </q-td>-->
<!--        </q-tr>-->
<!--    </template>-->
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
          </q-th>
          <q-th>
          </q-th>
        </q-tr>
      </template>
<!---->
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
     <q-dialog v-model="filterDialog">
    <q-card>
      <q-card-section class="row items-center q-pb-none">
        <div class="text-h6">Filters</div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </q-card-section>

      <q-card-section horizontal>
        <q-card-section>
          <div class="text-h6">Delivery From</div>
        </q-card-section>

        <q-separator vertical />

        <q-card-section>
          <div class="q-pa-md">
            <div class="q-pb-sm">
            </div>
            <q-date v-model="selected.delivery_from" />
          </div>
        </q-card-section>
      </q-card-section>

      <!-- <q-separator horizontal />

        <q-card-section>
          <div class="text-h6">Delivery Till</div>
        </q-card-section> -->

      <!-- <q-card-section>
        <div class="text-h6">Delivery Till</div> -->
        <!-- <div class="q-pa-md">
          <div class="q-pb-sm">
          </div>
          <q-date v-model="selected.delivery_to" />
        </div> -->
      <!-- </q-card-section> -->

      <!-- <q-btn label='Apply Filters' @click="applyFilter" /> -->
    </q-card>
  </q-dialog>

    </div>
</template>

<script>
import { add_to_favourites, remove_from_favourites } from 'src/common/api_calls'
import { Notify } from 'quasar'

export default {
  name: 'TickerPriceTable',
  props: ['instruments_to_render', 'title', 'render_best'],
  computed: {
    data_render: function () {
      var instruments_to_render = this.instruments_to_render
      let type = ''
      // if (this.selected.delivery_from) {
      //   instruments_to_render = instruments_to_render.filter(instrument => {
      //     return new Date(instrument.delivery_from) >= new Date(this.selected.delivery_from)
      //   })
      // }
      // if (this.selected.delivery_to) {
      //   instruments_to_render = instruments_to_render.filter(instrument => {
      //     return new Date(instrument.delivery_to) <= new Date(this.selected.delivery_to)
      //   })
      // }
      if (this.tab !== 'All') {
        type = this.tab
        return instruments_to_render.filter(instrument => {
          return instrument.type === type
        })
      } else {
        return instruments_to_render
      }
    },
    lowest: function () {
      let type = ''
      var instruments = []
      if (this.tab !== 'All') {
        type = this.tab
        instruments = this.instruments_to_render.filter(instrument => {
          return instrument.type === type
        })
      } else {
        instruments = this.instruments_to_render
      }
      // console.log(type)
      // console.log(instruments)
      // return this.instruments_to_render.filter(e => e.ask === Math.min(...this.instruments_to_render.map(f => f.ask)))[0]
      return instruments.filter(e => e.ask === Math.min(...instruments.map(f => f.ask)))[0]
    }
  },
  data () {
    return {
      pagination: {
        rowsPerPage: 0
      },
      search_selected: false,
      filter: '',
      tab: 'All',
      tabIndex: 0,
      filterDialog: false,
      types: ['All', 'Gold 999', 'Gold 999 1kg', 'Gold 995', 'Gold 995 1kg'],
      headers: [
        { name: 'Vendor', align: 'start', field: 'vendor', label: 'Vendor' },
        { name: 'Symbol', align: 'start', field: 'name', label: 'Symbol' },
        { name: 'Bid', align: 'start', field: 'bid', filterable: true, label: 'Bid', sortable: true },
        { name: 'Ask', align: 'start', field: 'ask', filterable: true, label: 'Ask', sortable: true },
        { name: 'High', align: 'start', field: 'high', filterable: true, label: 'High', sortable: true },
        { name: 'Low', align: 'start', field: 'low', filterable: true, label: 'Low', sortable: true },
        { name: 'favourite', align: 'start', field: 'is_favourite', label: '' }
      ],
      selected: {
        delivery_from: null,
        delivery_to: null
      }
    }
  },
  methods: {
    openFilterDrawer () {
      this.$store.state.rightDrawerOpen = !this.$store.state.rightDrawerOpen
    },
    handleSwipe ({ evt, ...info }) {
      console.log(info)
      if (info.direction === 'right') {
        this.tabIndex = Math.max(0, this.tabIndex - 1)
        this.tab = this.types[Math.min(this.tabIndex, this.types.length - 1)]
        // TODO WRITE LOGIC HERE
      } else if (info.direction === 'left') {
        this.tabIndex = Math.min(this.types.length - 1, this.tabIndex + 1)
        if (this.tabIndex < 0) { this.tabIndex = 0 }
        this.tab = this.types[Math.max(this.tabIndex, 0)]
        // TODO WRITE LOGIC HERE
      }
    },
    toggleFavourite: function (item) {
      console.log(item)
      item.is_favourite = !item.is_favourite
      if (item.is_favourite === false) {
        remove_from_favourites(item.instrument_id).then(res => {
          console.log(res)
          Notify.create({
            message: 'Removed from favourites ',
            position: 'top-right'
          })
        })
      } else {
        add_to_favourites(item).then(res => {
          Notify.create({
            message: 'Added to favourites ',
            position: 'top-right'
          })
        })
      }
    },
    open_order_sheet: function (item) {
      this.$store.dispatch('set_order_item', item)
      this.$store.dispatch('set_sheet', true)
    },
    open_vendor_dialog: function (vendor_id) {
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
  },
  created () {

  }
}
</script>

<style scoped>
  .vendor_link{
    color: darkblue;
  }
</style>
