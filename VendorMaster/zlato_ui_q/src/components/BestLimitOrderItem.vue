<template>
  <div class="">
    <q-card square style="" class="my-card" flat bordered>
      <q-card-actions align="right">
         <div class="justify-start">
           <q-chip outline color="black" dense >ID : {{order.best_limit_id}}</q-chip>
        </div>
          <q-chip outline  color="orange" dense >BEST_LIMIT</q-chip>
<!--          <q-chip outline  color="blue" dense ></q-chip>-->
          <q-chip v-if="is_cancelled" outline  color="red" dense >Cancelled</q-chip>
          <q-btn v-else @click="cancel_limit_order()" outline  color="black" dense >CANCEL</q-btn>
        </q-card-actions>
      <q-expansion-item
      :label="order.orders[0].instrument.vendor+' :'+order.orders[0].instrument.name+'  +'+(order.orders.length-1) +' more'"
      class="font-bold"
      >
      <div v-for="best_order in order.orders" :key="best_order.order_id">

      <q-separator/>

      <div class="row q-ma-sm">
          <div class="col">
        <strong>{{best_order.instrument.vendor}}</strong>
            <span class="font-bold q-ml-xs-sm " style=""> {{best_order.instrument.name}}</span>
          </div>
             <span class="text-right text-sm q-ml-sm" style="color: grey">LTP: {{best_order.instrument.ask}}</span>
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
    },
    is_cancelled: function () {
      return this.cancelled
    }
  },
  methods: {
    cancel_limit_order () {
      console.log(this.order.orders)
      this.order.orders.map(order => {
        cancel_order({ order_id: order.order_id }).then(res => {
          this.cancelled = true
        })
      })
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
