<template>
  <div class="orders">
    <v-card>
      <v-card-title>Orders</v-card-title>
      <v-tabs horizontal>
        <v-tab>
          <!--          <v-icon left>mdi-circle</v-icon>-->
          Open
        </v-tab>
        <v-tab>
          <!--          <v-icon>mdi-</v-icon>-->
          Executed
        </v-tab>
        <v-tab>
          <!--          <v-icon>mdi-access-point</v-icon>-->
          Previous
        </v-tab>
        <v-tab-item>
          <ActiveOrders v-bind:active_orders="active_orders" />
        </v-tab-item>

        <v-tab-item>
          <ExecutedOrders />
        </v-tab-item>

        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <p>
                Fusce a quam. Phasellus nec sem in justo pellentesque facilisis.
                Nam eget dui. Proin viverra, ligula sit amet ultrices semper,
                ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In
                dui magna, posuere eget, vestibulum et, tempor auctor, justo.
              </p>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
import ActiveOrders from "../components/orders/ActiveOrders";
import ExecutedOrders from "../components/orders/ExecutedOrders";
import { apiService } from "@/common/api.service";

export default {
  name: "Orders",
  components: {
    ActiveOrders,
    ExecutedOrders
  },
  data() {
    return {
      items: [
        {
          icon: "mdi-inbox",
          text: "Inbox"
        },
        {
          icon: "mdi-star",
          text: "Star"
        },
        {
          icon: "mdi-send",
          text: "Send"
        },
        {
          icon: "mdi-email-open",
          text: "Drafts"
        }
      ],
      model: 1,
      orders: [],
      active_orders: [],
      executed_orders: [],
      previous_orders: []
    };
  },
  created() {
    let endpoint = window.location.host + "/order/api/orderDetails";
    apiService(endpoint).then(res => {
      // console.log(res);
      this.orders = res;
      // console.log(this.orders);
    })
    .then(() => {
      this.orders.map(order => {
        order.instrument = this.$store.getters.get_instrument(order.instrument_id);
        console.log(order.instrument);
      })
    })
    .then(() => {
      this.active_orders = this.orders.filter(order => {
        return order.status === 'OPEN';
      })
      // console.log(this.active_orders)
    })
  }
}
</script>

<style scoped>
.orders {
  color: black;
}
</style>