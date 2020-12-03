import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    instruments: []
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

    update_instrument(state, instrument) {
      for (var i = 0; i < state.instruments.length; i++) {
        if (state.instruments[i].instrument_id == instrument.instrument_id) {
          instrument.bid = instrument.buy_premium + 40000;
          instrument.ask = instrument.sell_premium + 50000;
          instrument.high = instrument.buy_premium + 40000;
          instrument.low = instrument.sell_premium + 50000;
          state.instruments[i] = instrument;
          console.log("updating instrument");
        }
      }
    }
    // update_prices(state,tick)
    // {
    //   state.instruments.map()
    // }
  },
  actions: {
    push_instruments({ commit }, instruments) {
      instruments = instruments.map(function(instrument) {
        instrument.bid = instrument.buy_premium + 40000;
        instrument.ask = instrument.sell_premium + 50000;
        instrument.high = instrument.buy_premium + 40000;
        instrument.low = instrument.sell_premium + 50000;
        return instrument;
      });
      commit("push_instruments", instruments);
    },
    update_prices({ commit }, tick) {
      commit("update_prices", tick);
    },
    update_instrument({ commit }, instrument) {
      commit("update_instrument", instrument);
    }
  },
  modules: {},
  getters: {
    get_instruments: state => {
      return state.instruments;
    },
    get_vendor_instruments: state => vendor_id => {
      return state.instruments.filter(
        instrument => instrument.vendor_id == vendor_id
      );
    }
  }
});
