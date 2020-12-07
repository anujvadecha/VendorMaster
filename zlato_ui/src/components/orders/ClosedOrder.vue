<template>
  <v-card flat outlined class="ma-1" style="max-width: 700px">
    <v-container style="">
      <v-row no-gutters class="mb-2">
        <v-col class="col-6">{{ closed_order.order_id }}</v-col>
        <v-col class="col-6 text-right" color="black"
          ><v-chip outlined dark small color="green">
            <v-icon>mdi-tick</v-icon>
            Complete</v-chip
          >
          <!--          <v-chip dark small color="light-blue ml-2">OTP : 7869</v-chip>-->
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row no-gutters>
        <v-col class="col-8">
          <span class="font-weight-bold" style="color: darkblue">{{
            closed_order.instrument.vendor
          }}</span>
          <span class="font-weight-bold ml-2">{{
            closed_order.instrument.name
          }}</span>
          <span style="color:darkgrey">
            &nbsp;&nbsp;B: {{ closed_order.instrument.bid }}&nbsp; A:
            {{ closed_order.instrument.ask }}
          </span>
        </v-col>
        <v-col class="col-4 text-right">{{ closed_order.price }}</v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="col-6">Delivery 3-12th nov</v-col>
        <v-col class="col-6 text-right">
          <v-icon small>mdi-clock</v-icon>
          <span class="ml-2">12:31:02</span>
          <v-chip dark class="ml-2" small color="orange">{{
            closed_order.side
          }}</v-chip>
          <span class="ml-2">{{ closed_order.quantity }}</span>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "ClosedOrder",
  props: ["closed_order"]
};
</script>

<style scoped></style>
