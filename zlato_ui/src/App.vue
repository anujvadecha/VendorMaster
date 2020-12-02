<template>
  <v-app>
    <!--    <v-system-bar-->
    <!--  height="33"-->
    <!--  color="blue"-->
    <!--    > Prices Gold:50999 </v-system-bar>-->
    <NavBar></NavBar>
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
    const url = "ws://" + window.location.host + "/ws/" + "ticker" + "/";
    const symbolsocket = new WebSocket(url);
    symbolsocket.onopen = function() {
      symbolsocket.send(
        JSON.stringify({
          type: "ticker_request",
          message: "Please send all symbols"
        })
      );
    };
    symbolsocket.onmessage = function(event) {
      var message = JSON.parse(event.data);
      if (message["instruments"]) {
        var instruments = JSON.parse(message["instruments"]);
        console.log("instruments received" + instruments);
        store.dispatch("push_instruments", instruments);
      }
      if (message["gold_tick"]) {
        console.log(message["gold_tick"]);
        store.dispatch("update_prices", message);
      }
    };
  }
};
</script>
