<template>
<div>
<div class="window-height window-width row justify-center items-center" style="">
    <div class="column q-pa-lg">
          <q-card-section style="">
            <div class="row">
            <q-img
            :src="imageSrc"
            transition="scale-transition"
            width="50px"
            />
             <strong class="text-h6 q-ml-md q-my-md">Zlato</strong>
            </div>
          </q-card-section>
          <q-separator color="orange" size="5px"></q-separator>
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
            <q-btn @click="login_action()" unelevated size="lg" color="primary" class="full-width text-white" label="Sign In" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-sm">
            <p class="text-grey-6"> Forgot your password? </p>
            <p>Not a registered user ?<router-link to="/register">Register</router-link></p>
          </q-card-section>

    </div>
    </div>
</div>
</template>

<script>
import { Notify } from 'quasar'

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      imageSrc: '/logo.png'
    }
  },
  methods: {
    login_action: function () {
      console.log(this.email + this.password)
      this.connect_jwt()
    },
    connect_websocket: function () {
      const store = this.$store
      document.cookie = 'authorization=' + this.$q.localStorage.getItem('token') + ';'
      const url = 'ws://' + '127.0.0.1:8000' + '/ws/' + 'ticker' + '/' + '?' + this.$q.localStorage.getItem('token')
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
      const router = this.$router
      // router.push('Home')
      console.log(store)
      var axios = require('axios')
      var data = { username: this.email, password: this.password }
      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/login/',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      }
      const quasar_q = this.$q
      axios(config)
        .then(function (response) {
          console.log(quasar_q.localStorage.getItem('token'))
          store.dispatch('set_token', response.data.key)
          console.log('before checking' + quasar_q.localStorage.getItem('token'))
          quasar_q.localStorage.set('token', response.data.key)
          console.log('pushing to home')
          router.push('Home')
        }).catch(function (error) {
          console.log(error)
          Notify.create({
            message: error.toString(),
            position: 'top',
            timeout: 5000
          })
        })
    }
  }
}
</script>

<style scoped>
.q-card {
  width: 360px;
}
</style>
