<template>
<q-dialog  style="" v-model="$store.state.order_details_bottom_sheet"  position="bottom">
  <q-card class="" style="">
      <q-card-section class="bg-white" style=" color: white" >
      <div class="q-pa-sm">
        <span class="text-h6 text-grey-10">Order details</span>
        <q-chip outline class="q-ml-lg" color="black" dense >ID : {{order.transaction_id}}</q-chip>
        <q-chip outline color="primary" dense >Price : {{order.price}}</q-chip>
<!--        <q-select-->
<!--          filled-->
<!--          v-model="selected"-->
<!--          multiple-->
<!--          :options="order_items"-->
<!--          use-chips-->
<!--          stack-label-->
<!--          label="Multiple selection"-->
<!--        />-->
      </div>
      </q-card-section>
       <q-separator></q-separator>
      <div class="row q-ma-sm">
        <div class='col q-ml-sm'>{{order.instrument.name}}</div>
        <span class=" q-ml-sm" style=""><q-chip dense outline color="orange">{{order.side}} </q-chip>{{order.quantity}}</span>
      </div>
     <q-separator> </q-separator>
      <div class="row q-ma-sm">
         <span class="q-ml-sm" style="color:grey"><q-icon name="mdi-clock"></q-icon>{{get_formated_time}}</span>
        <div v-if="order.status==='EXECUTED'">
          <q-chip v-if="order.type==='BEST_LIMIT'" outline  color="orange" dense >BEST_LIMIT</q-chip>
          <q-chip outline size="md" color="green" dense >Payment confirmed</q-chip>
          <q-chip outline color="blue" dense >OTP:{{order.otp}}</q-chip>
        </div>
        <div v-if="order.status==='OPEN'">
          <q-chip v-if="order.type==='BEST_LIMIT'" outline  color="orange" dense >BEST_LIMIT</q-chip>
          <q-chip outline color="blue" dense >Waiting for payment</q-chip>
        </div>
        <div v-if="order.status==='WAITING_FOR_LIMIT'">
          <q-chip v-if="order.type==='BEST_LIMIT'" outline  color="orange" dense >BEST_LIMIT</q-chip>
          <q-chip outline  color="blue" dense >Limit Order waiting</q-chip>
          <q-chip v-if="is_cancelled" outline  color="red" dense >Cancelled</q-chip>
          <q-btn v-else @click="cancel_limit_order()" outline  color="black" dense >CANCEL</q-btn>
        </div>
        <div v-if="order.status==='CLOSED'">
          <q-chip outline  color="green" dense >Closed</q-chip>
        </div>
      </div>
      <q-separator></q-separator>
      <div class="q-pa-sm">
        <div class="q-ma-sm" v-if="this.order.status==='OPEN'">
          Please make payment at
        </div>
        <div class="q-ma-sm" v-if="this.order.status==='EXECUTED'">
          Please collect delivery using the otp from
        </div>
        <q-card>
          <q-card-section v-bind:style="{
              backgroundColor: vendor.theme.css_header_background_color,
            }">
            <div class="row">
              <div class="col-3">
                <q-img width="80px" :src="base_url+vendor.theme.logo"/>
              </div>
              <div class="col-9">
                  <div class="q-ml-sm text-white" style="font-weight: bold">{{ vendor.name }}</div>
                  <q-separator color="white"></q-separator>
                  <div class="q-ml-sm text-white" style="">{{ vendor.vendor_details.collection_address }}</div>
                  <div class="q-ml-sm text-white" style="">Bank: {{ vendor.vendor_details.bank_details }}</div>
                  <div class="q-ml-sm text-white" style="">Call: {{ vendor.vendor_details.mobile_number_1 }} /{{ vendor.vendor_details.mobile_number_2 }} </div>
              </div>
            </div>
          </q-card-section>
       </q-card>

<!--        {{vendor}}-->
        </div>
      <q-separator></q-separator>
<!--      <q-card-section style="background-color: white" >-->
<!--      <q-btn class="bg-primary text-white">Ok</q-btn>-->
<!--      <q-btn class="q-ml-md btn-danger" @click="set_sheet_close()">Close</q-btn>-->
<!--      </q-card-section>-->
      </q-card>
</q-dialog>
</template>

<script>
import { base_url } from 'src/common/api_calls'

export default {
  name: 'OrderDetailsBottom',
  computed: {
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        return false
      } else {
        return true
      }
    },
    get_formated_time () {
      const event = new Date(this.order.created_at)
      return event.toLocaleString('en-GB')
    },
    get_set_sheet: function () {
      return this.$store.state.order_details_bottom_sheet
    },
    order_item: function () {
      return this.$store.getters.get_order_item
    },
    order_items: function () {
      return this.$store.state.instruments.filter(instrument => {
        return instrument.is_favourite === true
      }).map(
        instrument => {
          return {
            label: instrument.vendor + ':' + instrument.name,
            value: instrument
          }
        }
      )
    },
    order: function () {
      return this.$store.state.order_details_selected
    },
    vendor: function () {
      return this.$store.getters.get_vendor_from_id(this.$store.state.order_details_selected.instrument.vendor_id)
    }
  },
  methods: {
    set_sheet_close: function () {
      this.$store.state.order_details_bottom_sheet = false
    }
  },
  data () {
    return {
      base_url: base_url
    }
  },
  created () {
  }
}
</script>

<style scoped>

</style>
