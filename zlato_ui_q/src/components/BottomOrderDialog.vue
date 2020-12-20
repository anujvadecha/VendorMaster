<template>
<q-dialog style="width: 50%" v-model="this.get_set_sheet" @hide="set_sheet_close()"  persistent position="bottom">
    <q-card class="" style="">
      <q-card-section class="bg-primary" style=" color: white" >
      <div class="q-pa-md">
        <span class="text-h6">{{order_item.vendor}}</span>
        <span class="q-ml-md font-bold">{{order_item.name}}</span>
        <div class="row">
          <span class=" text-right q-ml-sm">B:{{order_item.bid}}</span>
          <span class="text-right q-ml-sm">A:{{order_item.ask}}</span>
        </div>
      </div>
        </q-card-section>
    <q-tabs
          v-model="tab"
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="MARKET" label="MARKET" />
          <q-tab name="LIMIT" label="LIMIT" />
    </q-tabs>
      <q-separator></q-separator>
        <q-tab-panels swipeable v-model="tab" animated>
          <q-tab-panel name="MARKET">
          <div class="row">
            <q-input class="" type="number" standout="text-white" v-model="quantity" label="Quantity"
            :rules="quantity_rules"
            />
            <q-input  class="q-ml-lg" type="number" readonly v-model="price" :label="order_item.ask.toString()" />
          </div>
          </q-tab-panel>
          <q-tab-panel name="LIMIT">
            <div class="row">
            <q-input type="number"  standout="text-white" v-model="quantity" label="Quantity"
            :rules="quantity_rules"/>
            <q-input type="number" class="q-ml-md"  v-model="price" :label="order_item.ask.toString()" />
          </div>
          </q-tab-panel>
        </q-tab-panels>
    <q-card-section style="background-color: white" >
      <q-btn class="btn-primary" @click="place_order()">Buy</q-btn>
      <q-btn class="q-ml-md btn-danger" @click="set_sheet_close()">Close</q-btn>
    </q-card-section>
    </q-card>
</q-dialog>
</template>

<script>
import { place_order } from 'src/common/api_calls'
const linksData = [
  {
    title: 'Home',
    caption: 'HomePage',
    icon: 'mdi-home',
    link: 'https://quasar.dev'
  },
  {
    title: 'Orders',
    caption: 'See your orders',
    icon: 'mdi-bag-checked',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Favourites',
    caption: 'See your favourites and compare',
    icon: 'mdi-heart',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Account',
    caption: 'Settings for your account',
    icon: 'mdi-account',
    link: 'https://forum.quasar.dev'
  }
]

export default {
  name: 'BottomOrderDialog',
  computed: {
    get_set_sheet: function () {
      return this.$store.getters.get_sheet
    },
    order_item: function () {
      return this.$store.getters.get_order_item
    }
  },
  methods: {
    set_sheet_close: function () {
      this.$store.state.bottom_sheet = false
    },
    place_order: function () {
      console.log('placing order for ' + this.order_item.instrument_id + this.quantity + this.price + this.tab + 'BUY')
      this.$store.state.bottom_sheet = false
      if (this.tab === 'MARKET') {
        var order = {
          side: 'BUY',
          instrument_id: this.order_item.instrument_id,
          quantity: this.quantity,
          price: this.order_item.ask,
          type: this.tab,
          status: 'OPEN'
        }
      } else {
        order = {
          side: 'BUY',
          instrument_id: this.order_item.instrument_id,
          quantity: this.quantity,
          price: this.price,
          type: this.tab,
          status: 'WAITING_FOR_LIMIT'
        }
      }
      place_order(order).then(res => {
        console.log(res)
        const notif = this.$q.notify({
          spinner: true,
          group: false,
          message: 'Please wait...',
          timeout: 2000,
          position: 'top-right',
          color: 'primary'
        })
        if (res.order_id) {
          notif({
            spinner: false,
            html: true,
            message: '<h6> Order has been placed </h6>',
            caption: 'Please check orders for details',
            position: 'top-right',
            color: 'positive'
          })
        } else {
          notif({
            spinner: false,
            html: true,
            message: 'Order could not be placed due to :',
            caption: '<h6>' + res + '<h6>',
            position: 'top-right',
            color: 'negative',
            timeout: 10000
          })
          // TODO DO SOMETHING BITCHES WE GOT BUSINESS
        }
      })
    }
  },
  data () {
    return {
      tab: 'MARKET',
      quantity: 0,
      price: '',
      imageSrc: '/logo.png',
      leftDrawerOpen: false,
      essentialLinks: linksData,
      quantity_rules: [
        val => !!val || '* Required',
        val => parseInt(val) % 100 === 0 || 'Should be multiple of 100gms'
      ]
    }
  }
}
</script>

<style scoped>

</style>
