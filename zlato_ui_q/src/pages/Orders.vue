<template>
<div>
  <div class="">
    <div class="q-gutter-y-md" style="">
      <q-card flat >
        <q-tabs
          v-model="tab"
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="executed" label="Executed" />
          <q-tab name="pending" label="Pending" />
          <q-tab name="closed" label="Closed" />
        </q-tabs>
        <q-separator />
        <q-tab-panels swipeable v-model="tab" animated>
          <q-tab-panel name="executed">
            <ExecutedOrders></ExecutedOrders>
          </q-tab-panel>
          <q-tab-panel name="pending">
<!--            <div class="text-h6">Alarms</div>-->
            <PendingOrders></PendingOrders>
          </q-tab-panel>
          <q-tab-panel name="closed">
<!--            <div class="text-h6">Movies</div>-->
            <ClosedOrders></ClosedOrders>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
</div>
  </div>
</div>
</template>

<script>
import ExecutedOrders from 'components/home/ExecutedOrders'
import PendingOrders from 'components/home/PendingOrders'
import ClosedOrders from 'components/home/ClosedOrders'
export default {
  name: 'Orders',
  components: { ClosedOrders, PendingOrders, ExecutedOrders },
  data () {
    return {
      tab: 'executed'
    }
  }
}
</script>

<style scoped>

</style>
