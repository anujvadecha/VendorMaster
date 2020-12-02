import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    instruments:[]
  },
  mutations: {
    push_instruments(state,instruments){
      state.instruments.push(instruments)
    }
  },
  actions: {
    push_instruments({commit}, instruments){
      commit("push_instruments",instruments)
    }
  },
  modules: {

  }
})
