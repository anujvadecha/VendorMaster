<template>
  <div class="home" style="margin: 20px">
   <div>
  <b-card border-variant="warning" no-body>
    <b-card-header header-tag="nav">
      <b-card-title>Ticker prices</b-card-title>
      <b-nav card-header tabs>
        <b-nav-item onclick=""  v-for="symbol in symbolTypes" v-bind:key="symbol">{{symbol}}</b-nav-item>
      </b-nav>
    </b-card-header>
    <b-card-body class="text-center">
      <b-card-text>
<!--        Have to use https://datatables.net/examples/styling/bootstrap4.html later-->
          <ticker-list-item v-for="symbol in getEligibleSymbols" v-bind:key="symbol.instrument_id" :instrument=symbol />
      </b-card-text>
      <b-button variant="primary">Go somewhere</b-button>
    </b-card-body>
  </b-card>
  </div>
  </div>
</template>

<script>
// import {apiService} from "@/common/api.service";
import store from "@/store/index"
import TickerListItem from "@/components/home/TickerListItem";
// import TickerListItem from "@/components/home/TickerListItem";
export default {
  name: "Home",
  components: {TickerListItem},
  data(){
    return {
      symbols:[],
      selected_symbol:null
    }
  },
  methods: {

  },
  computed:{
      getEligibleSymbols:function (){
        const symbols=[]
        var symbol_to_filter = this.selected_symbol
        console.log("\"selected symbol is\""+symbol_to_filter);
        if(symbol_to_filter == null)
          return store.state.instruments
        symbol_to_filter="gold 999"
        store.state.instruments.map(function (instrument){
          if(instrument.type==symbol_to_filter)
            symbols.push(instrument)
        })
        return symbols
        },

      symbolTypes:function (){
        const symbolTypes=new Set()
        store.state.instruments.map(function (instrument){
          symbolTypes.add(instrument.type)
        })
        return symbolTypes;
      },
},



};
</script>

<style scoped>
  .home {
    color: black;
  }
</style>