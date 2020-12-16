<template>
  <div class="Favourites">
      <TickerPriceTable :instruments_to_render="favourite_items" />
  </div>
</template>

<script>
import TickerPriceTable from 'components/TickerPriceTable'

export default {
  name: 'Favourites',
  components: {
    TickerPriceTable
  },
  data () {
    return {
      favourite_items: []
    }
  },
  created () {
    this.favourite_items = this.$store.state.instruments.filter(instrument => {
      return instrument.is_favourite === true
    })
    console.log(this.favourite_items)
  }
}
</script>

<style scoped>
.Favourites {
  color: black;
}
</style>
