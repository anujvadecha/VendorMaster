<template>
  <div class="orders">
    <v-card>
      <v-card-title>Orders</v-card-title>
      <v-tabs horizontal>
        <v-tab>
          <v-icon left>
            mdi-account
          </v-icon>
          Open
        </v-tab>
        <v-tab>
          <v-icon >
            mdi-lock
          </v-icon>
          Executed
        </v-tab>
        <v-tab>
          <v-icon >
            mdi-access-point
          </v-icon>
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
                Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit
                amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna,
                posuere eget, vestibulum et, tempor auctor, justo.
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
          icon: 'mdi-inbox',
          text: 'Inbox',
        },
        {
          icon: 'mdi-star',
          text: 'Star',
        },
        {
          icon: 'mdi-send',
          text: 'Send',
        },
        {
          icon: 'mdi-email-open',
          text: 'Drafts',
        },
      ],
      model: 1,
      active_orders: [
        {
          title: "Arihant",
          instrument_id: "#12313123",
          quantity: 200,
          order_id: 1,
          price: 1000
        },
        {
          title: "Tribhovan",
          instrument_id: "#0327490",
          quantity: 300,
          order_id: 2,
          price: 2000
        }
      ]
    }
  },
};
</script>

<style scoped>
.orders {
  color: black;
}
</style>