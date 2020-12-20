<template>
<div>
  <div class="q-pa-md">
    <q-table
      grid
      card-class="bg-primary text-white"
      title="Margins from vendors"
      :data="margins"
      :columns="columns"
      row-key="name"
      :filter="filter"
      hide-header
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
            <q-card-section class="text-center">
              <q-img width="40px" :src="get_logo_url(props.row.vendor.theme.logo)"></q-img>
              <strong>{{ props.row.vendor.name }}</strong>
            </q-card-section>
            <q-separator />
            <q-card-section class="" >
              <div class="row">Margin: {{ props.row.margin }} gms</div>
              <div class="row">Available: {{ props.row.margin_available }} gms</div>
            </q-card-section>
          </q-card>
        </div>
      </template>
    </q-table>
  </div>
</div>
</template>

<script>
import { get_user_margins, base_url } from 'src/common/api_calls'

export default {
  name: 'UserMargins',
  methods: {
    get_logo_url (img_url) {
      return base_url.concat(img_url)
    }
  },
  data: function () {
    return {
      margins: [],
      filter: '',
      columns: [
        {
          name: 'vendor',
          required: true,
          label: 'Vendor',
          align: 'left',
          field: row => row.vendor.name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'margin', align: 'center', label: 'Margin', field: 'margin', sortable: true },
        { name: 'margin_available', label: 'Margin Available', field: 'margin_available', sortable: true }
      ]
    }
  },
  created () {
    console.log('requesting for margins')
    get_user_margins().then(
      res => {
        res.map(margin => {
          margin.vendor = this.$store.getters.get_vendor_from_id(margin.vendor)
        })
        this.margins = res
      }
    )
  }
}

</script>

<style scoped>

</style>
