<template>
  <div>
    <q-card class="q-ma-md" style="height: 100%;">
      <q-img style="max-height: 200px" src="https://cdn.quasar.dev/img/parallax2.jpg">
        <div class="absolute-bottom">
          <div class="text-h6">{{ vendor_object.vendor.name }}</div>
          <div class="text-subtitle2">{{ vendor_object.vendor.email }}</div>
        </div>
      </q-img>
      <TickerPriceTable :title="'Our'+' symbols'" :instruments_to_render="vendor_object.instruments"></TickerPriceTable>
      <q-card flat bordered>
        <div class="q-ma-md text-h6">Messages from {{ vendor_object.vendor.name }}</div>
        <div class="q-ma-md">
          {{ vendor_object.vendor.vendor_details.messages }}
        </div>
      </q-card>
      <q-card>
        <div class="q-ma-md text-h6">Company info from {{ vendor_object.vendor.name }}</div>
        <q-tabs
          v-model="tab"
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="About-us" label="About us"/>
          <q-tab name="Contact-info" label="Contact info"/>
          <q-tab name="Delivery-charges" label="Delivery charges"/>
        </q-tabs>
        <q-separator/>
        <q-tab-panels swipeable v-model="tab" animated>
          <q-tab-panel name="About-us">
               <span
                 v-html="vendor_object.vendor.vendor_details.about_us"
               ></span>
          </q-tab-panel>
          <q-tab-panel name="Contact-info">
            <span
              v-html="vendor_object.vendor.vendor_details.contact_details"
            ></span>
          </q-tab-panel>
          <q-tab-panel name="Delivery-charges">
            <span
              v-html="vendor_object.vendor.vendor_details.delivery_charges"
            ></span>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </q-card>
  </div>
</template>

<script>
import TickerPriceTable from 'components/TickerPriceTable'

export default {
  name: 'VendorDetails',
  props: ['vendor_object', 'vendor'],
  components: { TickerPriceTable },
  data () {
    return {
      tab: 'About-us',
      headers: [
        { text: 'Symbol', value: 'name' },
        { text: 'Bid', value: 'bid', filterable: false },
        { text: 'Ask', value: 'ask', filterable: false },
        { text: 'High', value: 'high', filterable: false },
        { text: 'Low', value: 'low', filterable: false }
      ],
      selected_item: null
    }
  },
  methods: {
    // open_order_sheet: function(item) {
    //   this.$store.dispatch("set_sheet", true);
    //   this.selected_item = item;
    // }
  }
}
</script>

<style scoped>

</style>
