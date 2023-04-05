<template>
  <v-card flat outlined class="ma-1" style="max-width: 700px">
    <v-container style="">
      <v-row no-gutters class="mb-2">
        <v-col class="col-6">{{ executed_waiting.order_id }}</v-col>
        <v-col class="col-6 text-right" color="black"
          ><v-chip outlined dark small color="light-blue"
            >Waiting for payment</v-chip
          >
          <!--          <v-chip dark small color="light-blue ml-2">OTP : 7869</v-chip>-->
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row class="mt-2" no-gutters>
        <v-col class="col-8">
          <span class="font-weight-bold" style="color: darkblue">{{
            executed_waiting.instrument.vendor
          }}</span>
          <span class="font-weight-bold ml-2">{{
            executed_waiting.instrument.name
          }}</span>
          <span style="color:darkgrey">
            &nbsp;&nbsp;B: {{ executed_waiting.instrument.bid }}&nbsp; A:
            {{ executed_waiting.instrument.ask }}
          </span>
        </v-col>
        <v-col class="col-4 text-right">{{ executed_waiting.price }}</v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="">Delivery 3-12th nov</v-col>
        <v-col class="text-right">
          <v-icon small>mdi-clock</v-icon>
          <span class="ml-2">12:31:02</span>
          <v-chip dark class="ml-2" small color="orange">{{
            executed_waiting.side
          }}</v-chip>
          <span class="ml-2">{{ executed_waiting.quantity }}</span>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "ExecutedOrderItem",
  props: ["executed_waiting"]
};
</script>

<style scoped></style>
