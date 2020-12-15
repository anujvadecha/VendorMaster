<template>
<q-dialog v-model="this.get_set_sheet" @hide="set_sheet_close()"  persistent>
      <q-card style="width: 350px">
          {{order_item}}
          <q-btn flat @click="set_sheet_close()">Close</q-btn>
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
  }
}
</script>

<style scoped>

</style>
