<template>
  <div>
    <li>This is item {{instrument}}</li>
  </div>
</template>

<script>
export default {
  name: "TickerListItem",
  props:["instrument"]
}
</script>
<style scoped>

</style>