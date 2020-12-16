<template>
<div class="row q-pa-md" style="background-color:#f4e8ff;">
  <div v-for="vendor in vendors" :key="vendor.vendor_id">
  <q-card
  @click="open_vendor_dialog(vendor.vendor_id)"
  >
    <q-card-section
      v-bind:style="{
              backgroundColor: vendor.theme.css_header_background_color,
              height:'150px',
              width:'120px'
            }">
      <q-img :src="base_url+vendor.theme.logo" :alt="vendor.name"/>
    </q-card-section>
    <div class="q-ma-sm" style="max-width: 120px">{{ vendor.name }}</div>
  </q-card>
  </div>
</div>
</template>

<script>
export default {
  name: 'TopVendors',
  props: ['vendors'],
  data () {
    return {
      base_url: this.$store.state.base_url
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
