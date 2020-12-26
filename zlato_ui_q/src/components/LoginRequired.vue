<template>
<div>
  <div class="q-ma-md row justify-center">
    <q-img width="50%" src="laptop.png"></q-img>
      </div>
    <div class="row justify-center">
    <strong class="text-h6">Please login to view {{ page }}</strong>
    </div>
    <div class="q-ma-lg row justify-center">
    <q-btn @click="$router.push('Login')" flat class="bg-primary text-white">Login</q-btn>
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
