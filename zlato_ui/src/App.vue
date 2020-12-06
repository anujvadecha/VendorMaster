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
          let favourites = JSON.parse(message["favourites"]);
          favourites = favourites.map(favourite => {
            return favourite.instrument_id;
          })

          // TODO
          // for instrument in instrument instrument.favourite=True when favourites has it
          instruments.map(instrument => {
            for(let i=0; i<favourites.length; i++) {
              if(favourites[i] === instrument.instrument_id) {
                instrument.is_favourite= true;
              }
              else {
               instrument.is_favourite = false;
            }
            }

          });
          console.log(favourites);
          console.log(instruments);
          store.dispatch("push_instruments", instruments);
        }
        if (message["gold_tick"]) {
          store.dispatch("update_prices", message);
        }
        if (message["instrument_update"]) {
          console.log("instrument_update received");
          console.log(message);
          var to_update = JSON.parse(message["instrument_update"]);
          console.log(to_update);
          store.dispatch("update_instrument", to_update);
        }
        if (message["vendors"]) {
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
