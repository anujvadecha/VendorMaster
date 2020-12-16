<template>
  <div id="q-app">
    {{state_get}}
    <div v-if="logged_in">
      <MainLayout></MainLayout>
    </div>
    <div v-else
    class="window-height window-width row justify-center items-center"
       style=""
    >
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width:300px;height:485px;">
          <q-card-section class="bg-deep-purple-7">
            <h4 class="text-h5 text-white q-my-md">Zlato</h4>
            <div class="absolute-bottom-right q-pr-md" style="transform: translateY(50%);">
              <q-btn fab icon="add" color="purple-4" />
            </div>
          </q-card-section>
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl">
              <q-input square clearable v-model="email" type="email" label="Email">
                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>
              <q-input square clearable v-model="password" type="password" label="Password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-lg">
            <q-btn @click="login_action()" unelevated size="lg" color="purple-4" class="full-width text-white" label="Sign In" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-sm">
            <p class="text-grey-6">Forgot your password?</p>
          </q-card-section>
        </q-card>
      </div>
    </div>
    </div>
    <BottomOrderDialog></BottomOrderDialog>
  </div>
</template>
<script>
import MainLayout from 'layouts/MainLayout'
import BottomOrderDialog from 'components/BottomOrderDialog'
// import { base_url } from 'common/api_calls'
export default {
  name: 'App',
  base_url: '127.0.0.1:8000',
  components: { BottomOrderDialog, MainLayout },
  computed: {
    state_get: function () {
      console.log(this.$store.state)
      return ''
    },
    logged_in: function () {
      return this.$store.state.token !== ''
    }
  },
  methods: {
    set_token: function (token) {
      // console.log('setting token' + token)
      this.$store.state.token = token
    },
    connect_websocket: function () {
      const store = this.$store
      document.cookie = 'authorization=' + store.state.token + ';'
      const url = 'ws://' + '127.0.0.1:8000' + '/ws/' + 'ticker' + '/' + '?' + store.state.token
      const symbolsocket = new WebSocket(url)
      symbolsocket.onopen = function () {
        symbolsocket.send(
          JSON.stringify({
            type: 'ticker_request',
            message: 'Please send all symbols'
          })
        )
        symbolsocket.send(
          JSON.stringify({
            type: 'vendor_request',
            message: 'Please send all vendors'
          })
        )
      }
      symbolsocket.onmessage = function (event) {
        var message = JSON.parse(event.data)
        if (message.instruments) {
          var instruments = JSON.parse(message.instruments)
          let favourites = JSON.parse(message.favourites)
          favourites = favourites.map(favourite => {
            return favourite.instrument_id
          })
          instruments = instruments.map(instrument => {
            instrument.is_favourite = false
            return instrument
          })
          for (let i = 0; i < instruments.length; i++) {
            for (let j = 0; j < favourites.length; j++) {
              if (favourites[j] === instruments[i].instrument_id) {
                console.log('setting instrument')
                instruments[i].is_favourite = true
              }
            }
          }
          console.log(favourites)
          console.log(instruments)
          store.dispatch('push_instruments', instruments)
        }
        if (message.gold_tick) {
          store.dispatch('update_prices', message)
        }
        if (message.instrument_update) {
          console.log('instrument_update received')
          console.log(message)
          var to_update = JSON.parse(message.instrument_update)
          console.log(to_update)
          store.dispatch('update_instrument', to_update)
        }
        if (message.vendors) {
          console.log(message.vendors)
          var vendors = message.vendors.map(vendor => {
            vendor.theme = JSON.parse(vendor.theme)[0]
            vendor.vendor_details = JSON.parse(vendor.vendor_details)[0]
            return vendor
          })
          store.dispatch('push_vendors', vendors)
        }
        if (message.order_update) {
          console.log(message)
        }
      }
      symbolsocket.onclose = function (event) {
        console.log(event)
        setTimeout(function () {
          this.connect_jwt()
        }, 2000)
      }
    },
    connect_jwt: function () {
      const store = this.$store
      var axios = require('axios')
      var data = JSON.stringify({ username: this.email, password: this.password })
      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/login/',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      }
      const connect = this.connect_websocket
      axios(config)
        .then(function (response) {
          store.dispatch('set_token', response.data.key)
          console.log(JSON.stringify(response.data))
          connect()
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    login_action: function () {
      console.log(this.email + this.password)
      this.connect_jwt()
    }
  },
  data () {
    return {
      email: '',
      password: ''
    }
  },
  created () {

  }
}
</script>
