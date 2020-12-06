<template>
  <v-app>
    <!--    <v-system-bar-->
    <!--  height="33"-->
    <!--  color="blue"-->
    <!--    > Prices Gold:50999 </v-system-bar>-->

    <NavBar> </NavBar>
    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
    <v-footer app>
      Built with love and dedication from DeltaCap Bullion
    </v-footer>
  </v-app>
</template>
<script>
// import Vue from 'vue'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)
import store from "@/store";
import NavBar from "./components/NavBar/NavBar";
export default {
  name: "App",

  components: { NavBar },

  data: () => ({
    //
  }),
  created() {
    function connect() {
      const url = "ws://" + window.location.host + "/ws/" + "ticker" + "/";
      const symbolsocket = new WebSocket(url);
      symbolsocket.onopen = function() {
        symbolsocket.send(
          JSON.stringify({
            type: "ticker_request",
            message: "Please send all symbols"
          })
        );
        symbolsocket.send(
          JSON.stringify({
            type: "vendor_request",
            message: "Please send all vendors"
          })
        );
      };
      symbolsocket.onmessage = function(event) {
        var message = JSON.parse(event.data);
        if (message["instruments"]) {
          var instruments = JSON.parse(message["instruments"]);
          console.log(instruments);
          // var favourites = JSON.parse(message["favourites"]);
          // TODO
          // for instrument in instrument instrument.favourite=True when favourites has it
          instruments.map(instrument => {
            instrument.is_favourite = false;
          });
          store.dispatch("push_instruments", instruments);
        }
        if (message["gold_tick"]) {
          store.dispatch("update_prices", message);
        }
        if (message["instrument_update"]) {
          console.log(message);
          var to_update = JSON.parse(message["instrument_update"]);
          console.log(to_update);
          store.dispatch("update_instrument", to_update);
        }
        if (message["vendors"]) {
          console.log(message["vendors"]);
          store.dispatch("push_vendors", message["vendors"]);
        }
      };
      symbolsocket.onclose = function(event) {
        console.log(event);
        setTimeout(function() {
          connect();
        }, 2000);
      };
    }
    connect();
  }
};
</script>
