<template>
  <div>
  <div id="q-app">
    <q-layout class="" view="lHh Lpr fFf">
      <q-header class="bg-white text-dark" style="" elevated bordered  >
      <q-toolbar style="" class="shadow-2">
<!--        <q-btn class="mobile-only" flat dense round icon="menu" aria-label="Menu" @click="leftDrawerOpen = !leftDrawerOpen"/>-->
        <q-toolbar-title class="font-bold">
          <q-img
            :src="imageSrc"
            transition="scale-transition"
            width="40px"
            />
          <span v-if="currentRouteName==='Home'||''||'/'">
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
    <q-drawer v-model="leftDrawerOpen" show-if-above bordered content-class="bg-grey-1">
      <q-img class="absolute-top" src="https://source.unsplash.com/featured?nature,water" style="height: 150px;">
          <div class="absolute-bottom ">
<!--            <q-avatar size="56px" class="q-mb-sm">-->
<!--              <img src="https://cdn.quasar.dev/img/boy-avatar.png">-->
<!--            </q-avatar>-->
            <div class="text-weight-bold">Zlato</div>
            <div>Mumbai</div>
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
<!--      <q-tree-->
<!--          :nodes="account_actions"-->
<!--          node-key="label"-->
<!--          default-expand-all>-->
<!--          <template v-slot:default-header="prop">-->
<!--            <div class="row items-center">-->
<!--              <q-icon :name="prop.node.icon || 'share'" color="orange" size="28px" class="q-mr-sm" />-->
<!--              <div class="text-weight-bold text-primary">{{ prop.node.label }}</div>-->
<!--            </div>-->
<!--          </template>-->
<!--      </q-tree>-->
      </q-list>
      </q-scroll-area>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
    <q-footer v-if="$q.platform.is.mobile"  class=" bg-white text-white">
      <q-toolbar class="justify-evenly shadow-2">
        <q-btn flat >
          <router-link class="text-primary" to="Home" style="text-decoration: None;">
          <q-icon class="lt-md" size="lg" name="mdi-home" ></q-icon>
          </router-link>
        </q-btn>
        <q-btn flat>
          <router-link class="text-primary" to="Orders" style="text-decoration: None;">
          <q-icon class="lt-md" size="lg" name="mdi-bag-checked" ></q-icon>
           </router-link>
        </q-btn>
        <q-btn flat>
          <router-link class="text-primary" to="Favourites" style="text-decoration: None;">
          <q-icon class="lt-md" size="lg" name="mdi-heart"></q-icon>
            </router-link></q-btn>
        <q-btn flat>
          <router-link class="text-primary" to="Account" style="text-decoration: None;">
          <q-icon class="lt-md"  size="lg" name="mdi-account"></q-icon>
        </router-link>
        </q-btn>
      </q-toolbar>
    </q-footer>
  </q-layout>
    <BottomOrderDialog></BottomOrderDialog>
    <BestLimitBottomOrderDialog></BestLimitBottomOrderDialog>

  </div>

</div>
</template>
<script>
import BottomOrderDialog from 'components/BottomOrderDialog'
// import { NotifySuccess } from 'src/common/api_calls'
// import MainLayout from 'layouts/MainLayout'

import EssentialLink from 'components/EssentialLink.vue'
import { Notify } from 'quasar'
import { base_websocket_url, get_user_details } from 'src/common/api_calls'
import BestLimitBottomOrderDialog from 'components/BestLimitBottomOrderDialog'
const linksData = [
  {
    title: 'Home',
    icon: 'mdi-home',
    link: 'https://quasar.dev'
  },
  {
    title: 'Orders',
    icon: 'mdi-bag-checked',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Favourites',
    icon: 'mdi-heart',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Account',
    icon: 'mdi-account',
    link: 'https://forum.quasar.dev'
  }
  // {
  //   title: 'Margins',
  //   icon: 'mdi-account',
  //   link: 'https://forum.quasar.dev'
  // }
]

const account_details_tree = [
  {
    label: 'Account details',
    header: 'root',
    icon: 'mdi-account',
    children: [
      {
        title: 'Margin',
        link: 'https://forum.quasar.dev',
        label: 'Good food',
        icon: 'mdi-account',
        header: 'generic'
      }
    ]
  }
]
// const account_actions_list = [
//   {
//     title: 'Margin',
//     icon: 'mdi-account',
//     link: 'https://forum.quasar.dev'
//   },
//   {
//     title: 'Logout',
//     icon: 'mdi-account',
//     link: 'https://forum.quasar.dev'
//   }
// ]
// import { base_url } from 'common/api_calls'
export default {
  name: 'Main',
  components: { BestLimitBottomOrderDialog, EssentialLink, BottomOrderDialog },
  computed: {
    is_activated: function () {
      return !this.$store.getters.get_is_activated
    },
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        console.log('returning false')
        return false
      } else {
        console.log('returning true')
        return true
      }
    },
    currentRouteName: function () {
      return this.$route.name
    }
  },
  methods: {
    login_action: function () {
      console.log(this.email + this.password)
      this.connect_jwt()
    },
    connect_websocket: function () {
      const connecter = this.connect_websocket
      const store = this.$store
      document.cookie = 'authorization=' + this.$q.localStorage.getItem('token') + ';'
      const url = 'ws://' + base_websocket_url + '/ws/' + 'ticker' + '/' + '?' + this.$q.localStorage.getItem('token')
      const symbolsocket = new WebSocket(url)
      symbolsocket.onopen = function () {
        Notify.create({
          message: 'Connected to high speed market data ',
          position: 'top-right',
          timeout: 1000
        })
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
          if (message.favourites) {
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
          }
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
          const order = JSON.parse(message.order_update)
          Notify.create({
            message: 'order update recieved ' + order.status,
            position: 'top-right'
          })
        }
      }
      symbolsocket.onclose = function (event) {
        console.log(event)
        setTimeout(function () {
          console.log('websocket disconnected reconnecting ')
          connecter()
        }, 2000)
      }
    },
    connect_jwt: function () {
      const store = this.$store
      const router = this.$router
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
          console.log('pushing to home')
          router.push('/')
          connect()
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    get_user_details () {

    }
  },
  data () {
    return {
      email: '',
      password: ',',
      essentialLinks: linksData,
      imageSrc: '/logo.png',
      leftDrawerOpen: false,
      account_actions: account_details_tree
    }
  },
  created () {
    this.$router.push('Home')
    // if (this.logged_in) {
    this.connect_websocket()
    const store = this.$store
    if (this.logged_in) {
      get_user_details().then(
        res => {
          console.log(res)
          store.state.is_activated = res.is_activated
          store.state.requested_registration = res.requested_registration
          // store.dispatch('setactivated', res.is_activated)
        }
      )
    } else {
      if (this.$q.is.mobile) {
        this.$router.push()
      }
    }
    // } else {
    //   this.$router.push('Home')
    // }
  }

}
</script>
