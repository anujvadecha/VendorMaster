<template>
  <div id="q-app">
    <q-layout view="lHh Lpr lFf">
      <q-header class="bg-white text-dark" style="" elevated bordered  >
      <q-toolbar style="" class="shadow-2">
        <q-btn class="mobile-only" flat dense round icon="menu" aria-label="Menu" @click="leftDrawerOpen = !leftDrawerOpen"/>
        <q-toolbar-title class="font-bold">
          <span v-if="currentRouteName==='Home'||''||'/'">
            <q-img
            :src="imageSrc"
            transition="scale-transition"
            width="40px"
            />
            <span class="font-bold text-h6">Zlato</span>
          </span>
          <span v-else>
            {{currentRouteName}}
          </span>
        </q-toolbar-title>
        <div>
        <span class="color:grey mobile-hide">
        <q-btn flat >
          <router-link class="text-primary" to="Home" style="text-decoration: None;">
          <q-icon class="lt-md" size="md" name="mdi-home" ></q-icon>
         </router-link>
        </q-btn>
        <q-btn flat>
          <router-link class="text-primary" to="Orders" style="text-decoration: None;">
          <q-icon class="lt-md" size="md" name="mdi-bag-checked" ></q-icon>
           </router-link>
        </q-btn>
        <q-btn flat>
          <router-link class="text-primary" to="Favourites" style="text-decoration: None;">
          <q-icon class="lt-md" size="md" name="mdi-heart"></q-icon>
            </router-link></q-btn>
        <q-btn flat>
          <router-link class="text-primary" to="Account" style="text-decoration: None;">
          <q-icon class="lt-md"  size="md" name="mdi-account"></q-icon>
        </router-link></q-btn>
        <q-btn-dropdown
          flat
          class="lt-md text-primary"
          label="Account">
          <div class="q-pa-md">
            <div class="justify-center full-height full-width text-center">
              <q-avatar size="72px">
                <img src="https://cdn.quasar.dev/img/boy-avatar.png">
              </q-avatar>
              <div class="text-subtitle1 q-mt-md q-mb-xs">John Doe</div>
              <q-btn
                @click="logout()"
                color="primary"
                label="Logout"
                size="sm"
                v-close-popup
              />
            </div>
          </div>
        </q-btn-dropdown>
          </span>
        </div>
      </q-toolbar>
      <q-toolbar class="text-dark bg-white" inset style="font-weight: bold">
      <q-space></q-space>
<!--        <q-icon name="mdi-gold"></q-icon>-->
        <span class="" style="">Gold : 1270</span>
        <q-space></q-space>
<!--        <q-icon name="mdi-silverware-clean"></q-icon>-->
        <span>Silver: 128392</span>
        <q-space></q-space>
<!--        <q-icon name="mdi-gold"></q-icon>-->
        <span>Dollar: 78.9</span>
        <q-space></q-space>
      </q-toolbar>
    </q-header>
<!--    <span class="mobile-only ">-->
    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-img class="absolute-top" src="https://images.livemint.com/img/2020/05/02/600x338/73342ce6-87d6-11ea-9881-602785b14c14_1587970192680_1588398410207.jpg" style="height: 150px;">
          <div class="absolute-bottom bg-transparent">
            <q-avatar size="56px" class="q-mb-sm">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
            <div class="text-weight-bold">Deltacap devs</div>
            <div>@deltacap devs</div>
          </div>
        </q-img>
      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">
      <q-list>
<!--        <q-item-label-->
<!--          header-->
<!--          class="text-grey-8"-->
<!--        >-->
<!--          Links-->
<!--        </q-item-label>-->
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
      </q-scroll-area>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
    <BottomOrderDialog></BottomOrderDialog>
  </div>
</template>
<script>
import BottomOrderDialog from 'components/BottomOrderDialog'
import { NotifySuccess } from 'src/common/api_calls'
// import MainLayout from 'layouts/MainLayout'

import EssentialLink from 'components/EssentialLink.vue'
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
  },
  {
    title: 'Margins',
    caption: 'Margins for you',
    icon: 'mdi-account'
  }
]

// import { base_url } from 'common/api_calls'
export default {
  name: 'App',
  components: { EssentialLink, BottomOrderDialog },
  computed: {
    state_get: function () {
      console.log(this.$store.state)
      return ''
    },
    logged_in: function () {
      console.log('logged in is' + this.$q.localStorage.getItem('token'))
      const token = this.$q.localStorage.getItem('token')
      console.log(token)
      if (token === '' || token === null || token === 'null') {
        console.log('returning false')
        return false
      } else {
        console.log('returning true')
        return true
      }
    }
  },
  methods: {
    logout () {
      console.log('logout called')
      this.$q.localStorage.set('token', '')
      this.$router.push({
        name: 'Login'
      })
    },
    set_token: function (token) {
      // console.log('setting token' + token)
      this.$store.state.token = token
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
          NotifySuccess({ message: 'this is order update' })
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
      var data = { username: this.email, password: this.password }
      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/login/',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      }
      const connect = this.connect_websocket
      const quasar_q = this.$q
      axios(config)
        .then(function (response) {
          console.log(quasar_q.localStorage.getItem('token'))
          store.dispatch('set_token', response.data.key)
          console.log('before checking' + quasar_q.localStorage.getItem('token'))
          quasar_q.localStorage.set('token', response.data.key)
          connect()
        })
        .catch(function (error) {
          quasar_q.$q.notify(error)
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
      password: ',',
      essentialLinks: linksData,
      imageSrc: '/logo.png',
      leftDrawerOpen: false
    }
  },
  created () {
    // this.connect_websocket()
    this.$q.localStorage.set('token', '')
    if (this.logged_in) {
      console.log('logged in')
    } else {
      this.$router.push('Login')
    }
  }
}
</script>
