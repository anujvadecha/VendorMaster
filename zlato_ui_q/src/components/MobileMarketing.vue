<template>
<div>
  <q-card v-if="!$q.platform.is.mobile" class="q-ma-sm">
    <q-card-section>
  <div  class="bg-light-blue-2">
  <div class="bg-white row  text-white">
<!--    <div class="col-4">-->
<!--      <q-img width="30%" src="mobile.png"/>-->
<!--    </div>-->
    <div class="">
      <span class="q-ma-sm font-bold text-primary row text-h6">
        Experience deltabx on the go
      </span>
      <span class="q-ma-sm font-bold text-primary row ">
        Convenience is guaranteed with our robust order placement engines
        and high priority on experience
      </span>
      <q-btn dense flat class="q-pl-sm q-pr-sm q-ma-sm bg-primary" icon="mdi-apple">IOS</q-btn>
      <q-btn dense flat class="q-pl-sm q-pr-sm q-ma-sm bg-primary" icon="mdi-android">Android</q-btn>
<!--      <q-img width="30%" src="googleplay.png"></q-img>-->
<!--      <q-img class="q-ml-sm" width="30%" src="appstore.png"></q-img>-->
    </div>

  </div>
  </div>
      </q-card-section>
    </q-card>
</div>
</template>

<script>
export default {
  name: 'MobileMarketing'
}
</script>

<style scoped>

</style>
