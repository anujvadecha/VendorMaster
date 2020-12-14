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
    snackbar: false
  },

  mutations: {
    push_instruments(state, instruments) {
      state.instruments = instruments;
    },
    update_prices(state, tick) {
      state.instruments = state.instruments.map(function(instrument) {
        instrument.bid = tick.gold_tick.bid + instrument.buy_premium;
        instrument.ask = tick.gold_tick.ask + instrument.sell_premium;
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
        if (state.instruments[i].instrument_id == instrument.instrument_id) {
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
    }
  },
  actions: {
    push_instruments({ commit }, instruments) {
      // instruments = instruments.map(function(instrument) {
      //   return instrument;
      // });
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
      console.log(vendor_id);
      console.log(state.vendors);
      vendor_object.vendor = state.vendors.find(
        vendor => vendor.vendor_id === vendor_id
      );
      return vendor_object;
    },
    get_favourite_instruments: state => {
      //TODO
      console.log(state);
    },
    get_sheet: state => {
      return state.bottom_sheet;
    }
  }
});
