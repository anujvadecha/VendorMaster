import Vue from 'vue'
import Vuex from 'vuex'

// import example from './module-example'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */
//
// export default function (/* { ssrContext } */) {
//   const Store = new Vuex.Store({
//     modules: {
//     },
//
//     // enable strict mode (adds overhead!)
//     // for dev mode only
//     strict: process.env.DEBUGGING
//   })
//
//   return Store
// }
export default new Vuex.Store({
  state: {
    instruments: [],
    vendors: [],
    bottom_sheet: false,
    snackbar_message: '',
    snackbar: false,
    token: '',
    base_url: '127.0.0.1:8000',
    order_item: null
  },

  mutations: {
    push_instruments (state, instruments) {
      state.instruments = instruments
    },
    update_prices (state, tick) {
      state.instruments = state.instruments.map(function (instrument) {
        instrument.bid = tick.gold_tick.bid + instrument.buy_premium
        instrument.ask = tick.gold_tick.ask + instrument.sell_premium
        instrument.high = Math.max(
          instrument.bid,
          instrument.high,
          instrument.ask
        )
        instrument.low = Math.min(
          instrument.bid,
          instrument.low,
          instrument.ask
        )
        return instrument
      })
    },
    set_token (state, token) {
      state.token = token
    },
    set_sheet (state, boolean) {
      state.bottom_sheet = boolean
    },
    update_instrument (state, instrument) {
      for (var i = 0; i < state.instruments.length; i++) {
        if (state.instruments[i].instrument_id === instrument.instrument_id) {
          state.instruments[i] = instrument
          console.log('updating instrument')
        }
      }
    },
    show_snackbar (state, message) {
      state.snackbar = true
      state.snackbar_message = message
    },
    push_vendors (state, vendors) {
      state.vendors = vendors
    },
    set_selected (state, item) {
      state.order_item = item
    }
  },
  actions: {
    push_instruments ({ commit }, instruments) {
      // instruments = instruments.map(function(instrument) {
      //   return instrument;
      // });
      commit('push_instruments', instruments)
    },
    update_prices ({ commit }, tick) {
      commit('update_prices', tick)
    },
    update_instrument ({ commit }, instrument) {
      commit('update_instrument', instrument)
    },
    push_vendors ({ commit }, vendors) {
      commit('push_vendors', vendors)
    },
    set_sheet ({ commit }, boolean) {
      commit('set_sheet', boolean)
    },
    set_order_item ({ commit }, selected_item_order) {
      commit('set_selected', selected_item_order)
    },
    show_snackbar ({ commit }, message) {
      commit('show_snackbar', message)
    },
    set_token ({ commit }, token) {
      commit('set_token', token)
    }
  },
  modules: {},
  getters: {
    get_instruments: state => {
      return state.instruments
    },
    get_instrument: state => instrument_id => {
      return state.instruments.find(
        instrument => instrument.instrument_id === instrument_id
      )
    },
    get_all_vendors: state => {
      // console.log("get all vendors");
      return state.vendors
    },
    get_vendor_instruments: state => vendor_id => {
      var vendor_object = {}
      vendor_object.instruments = state.instruments.filter(
        instrument => instrument.vendor_id === vendor_id
      )
      console.log(vendor_id)
      console.log(state.vendors)
      vendor_object.vendor = state.vendors.find(
        vendor => vendor.vendor_id === vendor_id
      )
      return vendor_object
    },
    get_favourite_instruments: state => {
      // TODO
      console.log(state)
    },
    get_order_item: state => {
      return state.order_item
    },
    get_sheet: state => {
      return state.bottom_sheet
    }
  }
})