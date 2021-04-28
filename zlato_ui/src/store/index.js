import Vue from "vue";
import Vuex from "vuex";
// import { version } from "vuex/dist/vuex";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    instruments: [],
    vendors: [],
    bottom_sheet: false,
    snackbar_message: "",
    snackbar: false,
    is_activated: false,
    requested_registration: false,
    rightDrawerOpen: false
  },
  mutations: {
    push_instruments(state, instruments) {
      state.instruments = instruments;
    },
    update_prices(state, tick) {
      state.instruments = state.instruments.map(function(instrument) {
        if (instrument.source_symbol === "gold_fut") {
          console.log("updating gold fut rate");
          instrument.bid = tick.gold_tick.bid + instrument.buy_premium;
          instrument.ask = tick.gold_tick.ask + instrument.sell_premium;
        } else if (instrument.source_symbol === "gold_bank") {
          console.log("updating gold bank rate");
          instrument.bid =
            (((tick.gold_comex.ask + instrument.vendor.gold_premium) *
              instrument.vendor.gold_conv *
              (tick.dollar.ask + instrument.vendor.gold_dollar_premium) +
              instrument.vendor.gold_custom) *
              (1 + instrument.vendor.gold_tax / 100)) /
            +instrument.buy_premium;
          instrument.ask =
            (((tick.gold_comex.ask + instrument.vendor.gold_premium) *
              instrument.vendor.gold_conv *
              (tick.dollar.ask + instrument.vendor.gold_dollar_premium) +
              instrument.vendor.gold_custom) *
              (1 + instrument.vendor.gold_tax / 100)) /
            instrument.sell_premium;
        }
        instrument.high = Math.max(
          instrument.bid,
          instrument.high,
          instrument.ask
        );
        instrument.low = Math.min(
          instrument.bid,
          instrument.low,
          instrument.ask
        );

        return instrument;
      });
    },
    set_sheet(state, boolean) {
      state.bottom_sheet = boolean;
    },
    update_instrument(state, instrument) {
      for (var i = 0; i < state.instruments.length; i++) {
        if (state.instruments[i].instrument_id === instrument.instrument_id) {
          state.instruments[i] = instrument;
          console.log("updating instrument");
        }
      }
    },
    show_snackbar(state, message) {
      state.snackbar = true;
      state.snackbar_message = message;
    },
    push_vendors(state, vendors) {
      state.vendors = vendors;
    },
    is_activated(state, boolean) {
      state.is_activated = boolean;
    }
  },
  actions: {
    push_instruments({ commit }, instruments) {
      commit("push_instruments", instruments);
    },
    update_prices({ commit }, tick) {
      commit("update_prices", tick);
    },
    update_instrument({ commit }, instrument) {
      commit("update_instrument", instrument);
    },
    push_vendors({ commit }, vendors) {
      commit("push_vendors", vendors);
    },
    set_sheet({ commit }, boolean) {
      commit("set_sheet", boolean);
    },
    show_snackbar({ commit }, message) {
      commit("show_snackbar", message);
    },
    setactivated({ commit }, boolean) {
      commit("is_activated", boolean);
    }
  },
  modules: {},
  getters: {
    get_instruments: state => {
      return state.instruments;
    },
    get_instrument: state => instrument_id => {
      return state.instruments.find(
        instrument => instrument.instrument_id === instrument_id
      );
    },
    get_all_vendors: state => {
      // console.log("get all vendors");
      return state.vendors;
    },
    get_vendor_instruments: state => vendor_id => {
      var vendor_object = {};
      vendor_object.instruments = state.instruments.filter(
        instrument => instrument.vendor_id === vendor_id
      );
      vendor_object.vendor = state.vendors.find(
        vendor => vendor.vendor_id === vendor_id
      );
      return vendor_object;
    },
    get_favourite_instruments: state => {
      console.log(state);
    },
    get_sheet: state => {
      return state.bottom_sheet;
    },
    get_is_activated: state => {
      return state.is_activated;
    }
  }
});
