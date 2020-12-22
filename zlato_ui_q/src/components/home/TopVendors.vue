<template>
  <div>
  <span class="q-ma-md row text-h6">Top vendors</span>
  <div class=" row q-pa-md">
  <div v-for="vendor in vendors" :key="vendor.vendor_id">
  <q-card class="q-ml-md" @click="open_vendor_dialog(vendor.vendor_id)">
    <q-card-section v-bind:style="{
              backgroundColor: vendor.theme.css_header_background_color,
              height:'150px',
              width:'120px'
            }">
      <q-img width="80px" :src="base_url+vendor.theme.logo" :alt="vendor.name"/>
      <span class="text-white" style="font-weight: bold">{{ vendor.name }}</span>
    </q-card-section>
  </q-card>
  </div>
</div>
    </div>
</template>

<script>
import { base_url } from 'src/common/api_calls'
export default {
  name: 'TopVendors',
  props: ['vendors'],
  data () {
    return {
      base_url: base_url
    }
  },
  methods: {
    open_vendor_dialog: function (vendor_id) {
      var selected_vendor_item = this.$store.getters.get_vendor_instruments(
        vendor_id
      )
      this.$router.push({
        name: 'Vendor',
        params: {
          vendor_object: selected_vendor_item
        }
      })
    }
  }
}

</script>

<style scoped>

</style>
