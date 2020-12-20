<template>
  <div v-if="orders.length>0">
  <q-table
      grid
      card-class="bg-primary text-white"
      :title="title"
      :data='orders'
      row-key="name"
      :filter="filter"
      hide-header
      hide-no-data
      hide-pagination
    >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>
      <template v-slot:item="props">
      <div class="q-pa-xs col-xs-12 col-sm-6 col-md-4">
          <q-card>
            <OrderItem :order="props.row"></OrderItem>
        </q-card>
      </div>
      </template>
    </q-table>
    </div>
  <div v-else>
    <div class="center">
      <q-img width="200px" src="/Human.png"></q-img>
      <q-card>
      <strong class="text-h6">No {{title}} orders</strong>
        </q-card>
    </div>

  </div>
</template>

<script>
import OrderItem from 'components/OrderItem'
export default {
  name: 'OrderItemTable',
  components: { OrderItem },
  props: ['orders', 'title'],
  data: function () {
    return {
      filter: ''
    }
  }
}
</script>

<style scoped>

</style>
