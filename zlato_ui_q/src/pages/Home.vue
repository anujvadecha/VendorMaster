<template>
  <div>
  <TopVendors class="mobile-hide"></TopVendors>
  <div class="q-pa-md">
    <q-card bordered>
    <q-tabs
          v-model="tab"

          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
          swipable
        >
          <q-tab name="All" label="All" />
          <q-tab name="gold 999" label="Gold 999" />
          <q-tab name="gold 999 1kg" label="gold 999 1kg" />
          <q-tab name="gold 995" label="Gold 995" />
          <q-tab name="gold 995 1kg" label="Gold 995 1kg" />
        </q-tabs>
    <q-separator />
        <q-tab-panels swipeable v-model="tab" animated keep-alive>
          <q-tab-panel name="All">
            <div class="text-h6">Mails</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
          <q-tab-panel name="gold 999">
            <div class="text-h6">Mails</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
          <q-tab-panel name="gold 999 1kg">
            <div class="text-h6">Alarms</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
          <q-tab-panel name="gold 995">
            <div class="text-h6">Movies</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>

          <q-tab-panel name="gold 995 1kg">
            <div class="text-h6">Movies</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
        </q-tab-panels>
</q-card>

<!--    <q-table-->
<!--      title="Ticker Prices"-->
<!--      :data="data"-->
<!--      :columns="columns"-->
<!--      row-key="id"-->
<!--      :pagination.sync="pagination"-->
<!--      :loading="loading"-->
<!--      :filter="filter"-->
<!--      @request="onRequest"-->
<!--      binary-state-sort-->
<!--    >-->
<!--      <template v-slot:top-right>-->
<!--        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">-->
<!--          <template v-slot:append>-->
<!--            <q-icon name="search" />-->
<!--          </template>-->
<!--        </q-input>-->
<!--      </template>-->
<!---->
<!--    </q-table>-->
  </div>

  </div>
</template>

<script>
import TopVendors from 'components/home/TopVendors'
export default {
  name: 'Home',
  components: { TopVendors },
  data () {
    return {
      tab: 'All'
    }
  }
}
</script>

<style scoped>

</style>
