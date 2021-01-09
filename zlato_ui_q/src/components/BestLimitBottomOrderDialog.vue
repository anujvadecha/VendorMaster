<template>
<q-dialog  style="width: 50%" v-model="this.get_set_sheet" @hide="set_sheet_close()"  persistent position="bottom">
  <q-card class="" style="">
      <q-card-section class="bg-primary" style=" color: white" >
      <div class="q-pa-md">
        <span class="text-h6">Best limit order</span>
        <q-select
          filled
          v-model="selected"
          multiple
          :options="order_items"
          use-chips
          stack-label
          label="Multiple selection"
        />
      </div>
      </q-card-section>
      <q-separator></q-separator>
          <div class="q-ma-md row">
              <div class="col">
            <q-input type="number"  standout="text-white" v-model="quantity" label="Quantity(gms)"
            :rules="quantity_rules"/></div>
              <div class="col">
            <q-input type="number" class="q-ml-md"  v-model="price"  />
            </div>
          </div>
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
  name: 'BestLimitBottomOrderDialog',
  computed: {
    min_quantity: function () {
      var min = 100
      this.selected.forEach(selected => {
        if (parseInt(selected.value.quantity) > min) { min = parseInt(selected.value.quantity) }
      })
      console.log(min)
      return min
    },
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        return false
      } else {
        return true
      }
    },
    favourite_items: function () {
      return this.$store.state.instruments.filter(instrument => {
        return instrument.is_favourite === true
      })
    },
    get_set_sheet: function () {
      return this.$store.getters.get_best_limit_sheet
    },
    order_item: function () {
      return this.$store.getters.get_order_item
    },
    order_items: function () {
      return this.$store.state.instruments.filter(instrument => {
        return instrument.is_favourite === true
      }).map(
        instrument => {
          return {
            label: instrument.vendor + ':' + instrument.name,
            value: instrument
          }
        }
      )
    }
  },
  methods: {
    set_sheet_close: function () {
      this.$store.state.bottom_best_limit_sheet = false
    },
    place_order: function () {
      if (this.logged_in) {
        console.log('logged in hence placing order')
        console.log(this.selected)
        var order = {
          side: 'BUY',
          instrument_id: this.selected.map(selected => {
            return selected.value.instrument_id
          }),
          quantity: this.quantity,
          price: this.price,
          type: 'BEST_LIMIT',
          status: 'WAITING_FOR_LIMIT'
        }
        place_order(order).then(res => {
          console.log(res)
          const notif = this.$q.notify({
            spinner: true,
            group: false,
            message: 'Please wait...',
            timeout: 10000,
            position: 'top-right',
            color: 'primary'
          })
          if (res.order_id !== undefined) {
            notif({
              spinner: false,
              html: true,
              message: '<h6> Order has been placed </h6>',
              caption: 'Please check orders for details',
              position: 'top-right',
              color: 'positive',
              timeout: 2000
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
          }
        })
      } else {
        this.$router.push({ name: 'Login', params: { message: 'Please login to place orders' } })
      }
    }
  },
  data () {
    return {
      tab: 'MARKET',
      quantity: 100,
      price: '',
      imageSrc: '/logo.png',
      leftDrawerOpen: false,
      essentialLinks: linksData,
      quantity_rules: [
        val => !!val || '* Required',
        val => parseInt(val) % 100 === 0 || 'Should be multiple of 100gms',
        val => parseInt(val) >= this.min_quantity || 'Min Quantity for this order is' + this.min_quantity
      ],
      options: [],
      selected: []
    }
  },
  created () {
    console.log('created best limit order form bottom ')
  }
}
</script>

<style scoped>

</style>
