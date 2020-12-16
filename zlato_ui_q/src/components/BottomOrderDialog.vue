<template>
<q-dialog v-model="this.get_set_sheet" @hide="set_sheet_close()"  persistent position="bottom">
    <q-card class="" style="">
      <q-card-section style="background-color: purple; color: white" >
      <div class="q-pa-md">
        <span class="text-h6">{{order_item.vendor}}</span>
        <span class="q-ml-md font-bold">{{order_item.name}}</span>
        <div class="row">
          <span class=" text-right q-ml-sm">B:{{order_item.bid}}</span>
          <span class=" text-right q-ml-sm">A:{{order_item.ask}}</span>
        </div>
      </div>
        </q-card-section>
    <q-card-section style="background-color: white" >
    <q-tabs
          v-model="tab"
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="MARKET" label="MARKET" />
          <q-tab name="LIMIT" label="LIMIT" />
    </q-tabs>
      <q-separator></q-separator>
        <q-tab-panels swipeable v-model="tab" animated>
          <q-tab-panel name="MARKET">
            <q-input type="number" standout="text-white" v-model="quantity" label="Quantity" />
            <q-input type="number" readonly v-model="price" :label="order_item.ask" />
          </q-tab-panel>
          <q-tab-panel name="LIMIT">
            <q-input type="number"  standout="text-white" v-model="quantity" label="Quantity" />
            <q-input type="number"  v-model="price" :label="order_item.ask" />
          </q-tab-panel>
        </q-tab-panels>
    </q-card-section>
    <q-card-section style="background-color: white" >
      <q-btn outline color="purple" @click="set_sheet_close()">Buy</q-btn>
      <q-btn outline class="q-ml-md" @click="set_sheet_close()">Close</q-btn>
    </q-card-section>
    </q-card>
</q-dialog>
</template>

<script>
export default {
  name: 'BottomOrderDialog',
  computed: {
    get_set_sheet: function () {
      return this.$store.getters.get_sheet
    },
    order_item: function () {
      return this.$store.getters.get_order_item
    }
  },
  methods: {
    set_sheet_close: function () {
      this.$store.state.bottom_sheet = false
    }
  },
  data () {
    return {
      tab: 'MARKET',
      quantity: 0,
      price: ''
    }
  }
}
</script>

<style scoped>

</style>
