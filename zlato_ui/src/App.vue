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
    <!--    <v-footer app>-->
    <!--      Built with love and dedication from DeltaCap Bullion-->
    <!--    </v-footer>-->
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
import SlimUI from "slim-ui";
import Vue from "vue";
Vue.use(SlimUI);
export default {
  name: "App",

  components: { NavBar },

  data: () => ({
    snackbar: false
  }),
  methods: {
    successToast: function(message) {
      this.$toast.success({
        message: message,
        orientation: this.$toast.TOP_RIGHT,
        duration: 2000
      });
    }
  },
  created() {
    this.successToast(
      "Welcome to zlato . You are connected to high speed data feeds"
    );
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
          });
          instruments = instruments.map(instrument => {
            instrument.is_favourite = false;
            return instrument;
          });
          for (let i = 0; i < instruments.length; i++) {
            for (let j = 0; j < favourites.length; j++) {
              if (favourites[j] == instruments[i].instrument_id) {
                console.log("setting instrument");
                instruments[i].is_favourite = true;
              }
            }
          }
          // instruments = instruments.map(instrument => {
          //   for (let i = 0; i < favourites.length; i++) {
          //     if (favourites[i] === instrument.instrument_id) {
          //       instrument.is_favourite = true;
          //     } else {
          //       instrument.is_favourite = false;
          //     }
          //     return instrument;
          //   }
          // });
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
          console.log(message["vendors"]);
          var vendors = message["vendors"].map(vendor => {
            vendor.theme = JSON.parse(vendor.theme)[0];
            vendor.vendor_details = JSON.parse(vendor.vendor_details)[0];
            return vendor;
          });
          store.dispatch("push_vendors", vendors);
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
