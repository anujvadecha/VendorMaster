<template>
  <v-card flat outlined class="ma-1" style="max-width: 700px">
    <v-container style="">
      <v-row no-gutters class="mb-2">
        <v-col class="col-6">{{ active_order.order_id }}</v-col>
        <v-col class="col-6 text-right" color="black"
          ><v-chip outlined dark small color="light-blue"
            >Waiting for limit</v-chip
          >
          <!--          <v-chip dark small color="light-blue ml-2">OTP : 7869</v-chip>-->
          <v-btn outlined small class="ml-2">Cancel</v-btn>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row no-gutters>
        <v-col class="col-8">
          <span class="font-weight-bold" style="color: darkblue">{{
            active_order.instrument.vendor
          }}</span>
          <span class="font-weight-bold ml-2">{{
            active_order.instrument.name
          }}</span>
          <span style="color:darkgrey">
            &nbsp;&nbsp;B: {{ active_order.instrument.bid }}&nbsp; A:
            {{ active_order.instrument.ask }}
          </span>
        </v-col>
        <v-col class="col-4 text-right">{{ active_order.price }}</v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="col-6">Delivery 3-12th nov</v-col>
        <v-col class="col-6 text-right">
          <v-icon small>mdi-clock</v-icon>
          <span class="ml-2">12:31:02</span>
          <v-chip dark class="ml-2" small color="orange">{{
            active_order.side
          }}</v-chip>
          <span class="ml-2">{{ active_order.quantity }}</span>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "ActiveOrderItem",
  props: ["active_order"],
  data() {
    return {
      instruments: "",
      instrument_name: ""
    };
  },
  methods: {},
  created() {}
};
</script>
