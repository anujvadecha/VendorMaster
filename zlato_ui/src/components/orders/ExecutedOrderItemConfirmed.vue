<template>
  <v-card flat outlined class="ma-1" style="max-width: 700px">
    <!--    <div class="d-flex flex-no-wrap justify-space-between"></div>-->
    <v-container class="">
      <!--      <v-row no-gutters>-->
      <!--        <v-col>-->
      <!--          .col-->
      <!--        </v-col>-->
      <!--        <v-spacer></v-spacer>-->
      <!--        <v-col>-->
      <!--          .col-->
      <!--        </v-col>-->
      <!--      </v-row>-->
      <v-row no-gutters class="mb-2">
        <v-col class="">{{ executed_confirmed.order_id }}</v-col>
        <!--        <v-spacer></v-spacer>-->
        <v-col class="text-right"
          ><v-chip outlined dark small color="green">Order confirmed</v-chip>
          <v-chip outlined dark small color="light-blue ml-2"
            >OTP :{{ executed_confirmed.otp }}</v-chip
          >
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row class="mt-2" no-gutters>
        <v-col class="">
          <span class="font-weight-bold" style="color: darkblue">{{
            executed_confirmed.instrument.vendor
          }}</span>
          <span class="font-weight-bold ml-2">{{
            executed_confirmed.instrument.name
          }}</span>
          <span style="color:darkgrey">
            &nbsp;&nbsp;B: {{ executed_confirmed.instrument.bid }}&nbsp; A:
            {{ executed_confirmed.instrument.ask }}
          </span>
        </v-col>
        <v-col class="text-right">{{ executed_confirmed.price }}</v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="">Delivery 3-12th nov</v-col>
        <v-spacer></v-spacer>
        <v-col class="text-right">
          <v-icon small>mdi-clock</v-icon>
          <span class="ml-2">12:31:02</span>
          <v-chip dark class="ml-2" small color="orange">{{
            executed_confirmed.side
          }}</v-chip>
          <span class="ml-2">{{ executed_confirmed.quantity }}</span>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "ExecutedOrderItemConfirmed",
  props: ["executed_confirmed"],
  created() {
    console.log(this.executed_confirmed);
  }
};
</script>

<style scoped></style>
