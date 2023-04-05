<template>
<div class="row q-ma-md text-center justify-center items-center align-middle">
  <div class="column q-pa-lg">
    <q-card flat>
      <div class="row" >
      <q-img width="" src="laptop.png"></q-img>
     </div>
    <div class="row q-mt-md">
    <strong class="text-h6">Please login to view {{ page }}</strong>
    </div>
    <div class="row justify-center">
    <q-btn align="" @click="$router.push('Login')" flat class="bg-primary text-white">Login</q-btn>
    </div>
      </q-card>
  </div>
</div>
</template>

<script>
export default {
  name: 'LoginRequired',
  props: ['page']
}
</script>

<style scoped>

</style>
