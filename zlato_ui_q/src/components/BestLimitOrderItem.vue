<template>
  <div class="">
    <q-card square style="" class="my-card" flat bordered>
      <q-card-actions align="right">
         <div class="justify-start">
           <q-chip outline color="black" dense >ID : {{order.best_limit_id}}</q-chip>
        </div>
          <q-chip outline  color="orange" dense >BEST_LIMIT</q-chip>
<!--          <q-chip outline  color="blue" dense ></q-chip>-->
          <q-chip v-if="cancelled" outline  color="blue" dense >Cancelled</q-chip>
          <q-btn @click="cancel_limit_order()" outline  color="black" dense >CANCEL</q-btn>
        </q-card-actions>
      <q-expansion-item
      v-model="expanded"
      :label="order.orders[0].instrument.vendor+' :'+order.orders[0].instrument.name+'  +'+(order.orders.length-1) +' more'"
      class="font-bold"
      >
<!--      <template v-slot:header>-->
<!--          <div class="row row-span-full q-ma-sm">-->
<!--          <div class="col">-->
<!--        <strong>{{order.orders[0].instrument.vendor}}</strong>-->
<!--            <span class="font-bold q-ml-xs-sm " style=""> {{order.orders[0].instrument.name}}</span>-->
<!--          </div>-->
<!--          <div class="col">-->
<!--              {{order.orders.length-1}} more-->
<!--          </div>-->
<!--             <span class="text-right text-sm q-ml-sm" style="color: grey">ltp: {{order.orders[0].instrument.ask}}</span>-->
<!--      </div>-->
<!--        </template>-->
        <div v-for="best_order in order.orders" :key="best_order.order_id">

      <q-separator/>

      <div class="row q-ma-sm">
          <div class="col">
        <strong>{{best_order.instrument.vendor}}</strong>
            <span class="font-bold q-ml-xs-sm " style=""> {{best_order.instrument.name}}</span>
          </div>
             <span class="text-right text-sm q-ml-sm" style="color: grey">ltp: {{best_order.instrument.ask}}</span>
      </div>
        </div>

    </q-expansion-item>
      <q-separator/>
      <div class="row q-ma-sm">
        <div class="col"><q-chip dense outline color="orange">{{order.orders[0].side}} </q-chip> {{order.orders[0].quantity}}
          <span class="q-ml-sm" style="color:grey"><q-icon name="mdi-clock"></q-icon>{{get_formated_time}}</span>
            </div>
        <div class="col">
            <div class="text-right align-right">
                <div class="col text-right">Price:{{order.orders[0].price}}</div>
            </div>
            </div>
      </div>
    </q-card>

  </div>
</template>

<script>
import { cancel_order } from 'src/common/api_calls'
export default {
  name: 'BestLimitOrderItem',
  props: ['order'],
  computed: {
    get_formated_time () {
      const event = new Date(this.order.orders[0].created_at)
      return event.toLocaleString('en-GB')
    },
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        return false
      } else {
        return true
      }
    }
  },
  methods: {
    cancel_limit_order () {
      console.log(this.order.orders)
      this.order.orders.map(order => {
        console.log(order)
        cancel_order({ order_id: order.order_id })
      })
      // for (var cancellation_order in this.order.orders) {
      //   console.log(cancellation_order.order_id)

      // }
    }
  },
  data: function () {
    return {
      cancelled: false
    }
  },
  created () {
  }

}
</script>

<style scoped>

</style>
