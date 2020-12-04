<template>
  <v-card flat outlined class="ma-1">
    <v-container>
      <v-row no-gutters justify="justify-end">
        <v-col class="col-6">#TR1234</v-col>
        <v-col class="col-6" color="black"
          ><v-chip dark small color="light-blue">Waiting for payment</v-chip>
          <!--          <v-chip dark small color="light-blue ml-2">OTP : 7869</v-chip>-->
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="col-8">
          <span class="font-weight-bold" style="color: darkblue">Arihant</span>
          <span class="font-italic ml-2">Gold 999</span>
        </v-col>
        <v-col class="col-4">50600</v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="col-6">Delivery 3-12th nov</v-col>
        <v-col class="col-6">
          <span class="ml-2">12:31:02</span>
          <v-chip dark class="ml-2" small color="orange">BUY</v-chip>
          <span class="ml-2">200</span>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "ExecutedOrderItem"
};
</script>

<style scoped></style>
