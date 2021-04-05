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
    bottom_best_limit_sheet: false,
    order_details_bottom_sheet: false,
    order_details_selected: undefined,
    snackbar_message: '',
    snackbar: false,
    token: '',
    order_item: null,
    user_details: null,
    gold_ask: 0,
    gold_low: 0,
    gold_high: 0,
    silver_ask: 0,
    silver_low: 0,
    silver_high: 0,
    dollar: 0,
    dollar_low: 0,
    dollar_high: 0,
    gold_comex: 0,
    gold_comex_low: 0,
    gold_comex_high: 0,
    selected_filters: {
      delivery_to: ''
    },
    orders: null,
    active_orders: [],
    executed_orders_waiting: [],
    executed_orders_confirmed: [],
    closed_orders: [],
    orders_to_rate: []
  },

  mutations: {
    push_instruments (state, instruments) {
      state.instruments = instruments
    },
    update_prices (state, tick) {
      state.gold_comex = tick.gold_comex.ask
      state.gold_ask = tick.gold_tick.ask
      state.silver_ask = tick.silver_tick.ask
      state.dollar = tick.dollar.ask
      state.gold_comex_high = tick.gold_comex.high
      state.gold_comex_low = tick.gold_comex.low
      state.gold_low = tick.gold_tick.low
      state.gold_high = tick.gold_tick.high
      state.silver_high = tick.silver_tick.high
      state.silver_low = tick.silver_tick.low
      state.dollar_high = tick.dollar.high
      state.dollar_low = tick.dollar.low
      state.instruments = state.instruments.map(function (instrument) {
        instrument.old_bid = instrument.bid
        instrument.old_ask = instrument.ask
        instrument.old_high = instrument.high
        instrument.old_low = instrument.low
        if (instrument.source_symbol === 'gold_fut') {
          instrument.bid = tick.gold_tick.bid + instrument.buy_premium
          instrument.ask = tick.gold_tick.ask + instrument.sell_premium
        } else if (instrument.source_symbol === 'gold_bank') {
          instrument.bid =
            parseInt((tick.gold_comex.ask * tick.dollar.ask * 31.1035 * 1.12875) /
              0.999 / 100) +
            instrument.buy_premium
          instrument.ask =
            parseInt((tick.gold_comex.ask * tick.dollar.ask * 31.1035 * 1.12875) /
              0.999 / 100) +
            instrument.sell_premium
        }
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
    },
    set_best_limit_sheet (state, boolean) {
      state.bottom_best_limit_sheet = boolean
    },
    set_order_details (state, details) {
      state.order_details_selected = details
    },
    set_orders (state, orders) {
      new Promise(function (resolve) {
        state.orders = orders.map(order => {
          order.instrument = state.instruments.find(
            instrument => instrument.instrument_id === order.instrument_id
          )
          return order
        })
        resolve()
      }).then(() => {
        state.orders.sort((a, b) => {
          return new Date(b.created_at) - new Date(a.created_at)
        })
      }).then(() => {
        state.active_orders = state.orders.filter(order => {
          return order.status === 'WAITING_FOR_LIMIT'
        })
        state.executed_orders_waiting = state.orders.filter(order => {
          return order.status === 'OPEN'
        })
        state.executed_orders_waiting.sort((a, b) => {
          return new Date(b.created_at) - new Date(a.created_at)
        })
        state.executed_orders_confirmed = state.orders.filter(order => {
          return order.status === 'EXECUTED'
        })
        state.closed_orders = state.orders.filter(order => {
          return order.status === 'CLOSED'
        })
        state.orders_to_rate = state.orders.filter(order => {
          return order.status === 'CLOSED' && order.is_rated === false
        })
      })
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
    set_best_limit_sheet ({ commit }, boolean) {
      commit('set_best_limit_sheet', boolean)
    },
    set_order_item ({ commit }, selected_item_order) {
      commit('set_selected', selected_item_order)
    },
    show_snackbar ({ commit }, message) {
      commit('show_snackbar', message)
    },
    set_token ({ commit }, token) {
      commit('set_token', token)
    },
    set_order_details ({ commit }, details) {
      commit('set_order_details', details)
    },
    set_orders ({ commit }, orders) {
      commit('set_orders', orders)
    }
  },
  modules: {},
  getters: {
    get_instruments: state => {
      return state.instruments
    },
    get_filtered_instruments: state => {
      var filtered_instruments = {}
      if (state.selected_filters.delivery_to.length > 0) {
        filtered_instruments = state.instruments.filter(
          instrument => new Date(instrument.delivery_to) >= new Date(state.selected_filters.delivery_to)
        )
      } else {
        filtered_instruments = state.instruments
      }
      return filtered_instruments
    },
    get_instrument: state => instrument_id => {
      return state.instruments.find(
        instrument => instrument.instrument_id === instrument_id
      )
    },
    get_all_vendors: state => {
      return state.vendors
    },
    get_vendor_instruments: state => vendor_id => {
      var vendor_object = {}
      vendor_object.instruments = state.instruments.filter(
        instrument => instrument.vendor_id === vendor_id
      )
      vendor_object.vendor = state.vendors.find(
        vendor => vendor.vendor_id === vendor_id
      )
      return vendor_object
    },
    get_favourite_instruments: state => {
      // TODO
    },
    get_order_item: state => {
      return state.order_item
    },
    get_sheet: state => {
      return state.bottom_sheet
    },
    get_vendor_from_id: state => vendor_id => {
      const vendor = state.vendors.find(
        vendor => vendor.vendor_id === vendor_id
      )
      return vendor
    },
    get_best_limit_sheet: state => {
      return state.bottom_best_limit_sheet
    }
  }
})
