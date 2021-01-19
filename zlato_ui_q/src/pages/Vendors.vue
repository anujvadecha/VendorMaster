<template>
  <TopVendors class=""  :vendors="vendors_computed"></TopVendors>
</template>
<script>
import TopVendors from 'components/home/TopVendors'
export default {
  name: 'Vendors',
  components: { TopVendors },
  computed: {
    vendors_computed: function () {
      return this.$store.getters.get_all_vendors
    }
  }
}
</script>

<style scoped>

</style>
