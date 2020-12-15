<template>
  <div>
<q-card style="max-width: 700px" class="my-card" flat bordered>
      <q-card-actions align="right" class="">
          <q-chip outline  color="blue" dense >Payment confirmed</q-chip>
          <q-chip outline color="blue" dense >OTP:7496</q-chip>
        </q-card-actions>
      <q-separator/>
      <div class="row q-ma-sm">
          <div class="col">
            <span style=" font-weight: bold;color:darkblue;font-size: large"> Arihant</span>
            <span class="font-bold q-ml-sm " style="font-size: large"> Gold 999</span>
          </div>
        <div class="col">
            <div class="text-right align-right">
                 <span class="q-ml-sm" style="color: grey"> B:7496 A:6547</span>
            </div>
          </div>
      </div>
      <div class="row q-ma-sm">
        <div class="col"><q-chip dense outline color="orange">BUY</q-chip> 200
            </div>
        <div class="col text-right">Price:50600</div>
      </div>
    </q-card>
    </div>
</template>

<script>
export default {
  name: 'ExecutedOrders'
}
</script>

<style scoped>

</style>
