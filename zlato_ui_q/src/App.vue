<template>
  <div id="q-app">
    {{state_get}}
    <MainLayout></MainLayout>
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
    }
  },
  methods: {
    set_token: function (token) {
      // console.log('setting token' + token)
      this.$store.state.token = token
    }
  },
  created () {
    const store = this.$store
    function connect_jwt () {
      var axios = require('axios')
      var data = JSON.stringify({ username: 'deltacapbullion', password: 'Abfc1234!' })
      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/login/',
        headers: {
          'Content-Type': 'application/json',
          Cookie: 'csrftoken=qY3htpK0KxfhuDlT7E47PB3qqrxG7rkF5EHi7YcvteLej7mJYd3Tx6pReQTwsoGP; sessionid=hcvf8yblipbwwzdjp2aw8djgu4ovr4g4'
        },
        data: data
      }
      axios(config)
        .then(function (response) {
          store.dispatch('set_token', response.data.key)
          console.log(JSON.stringify(response.data))
        })
        .catch(function (error) {
          console.log(error)
        })
    }

    function connect_websocket () {
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
          connect_jwt()
          connect_websocket()
        }, 2000)
      }
    }
    connect_jwt()
    connect_websocket()
  }
}
</script>
