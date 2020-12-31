<template>
<div>
  <div v-if="!$q.platform.is.mobile" class="bg-light-blue-2">
  <div class="bg-secondary row q-pa-md text-white">
    <div class="col">
      <q-img width="40%" src="mobile.png"/>
    </div>
    <div class="col">
      <span class="q-ma-md font-bold row text-h5">
        Experience zlato on the go
      </span>
      <span class="q-ma-md font-bold row text-h6">
        Convenience is garunteed with our robust order placement engines
        and high priority on experience
      </span>
      <q-img width="40%" src="googleplay.png"></q-img>
      <q-img class="q-ml-sm" width="40%" src="appstore.png"></q-img>
    </div>
  </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'MobileMarketing'
}
</script>

<style scoped>

</style>
