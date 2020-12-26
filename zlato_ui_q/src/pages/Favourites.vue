<template>
  <div>
  <div class="Favourites">
      <TickerPriceTable title="Favourites" :instruments_to_render="favourite_items" />
  </div>
  <div v-if="logged_in">
  </div>
  <div v-else>
    <LoginRequired page="or add Favourites"></LoginRequired>
  </div>
  </div>
</template>

<script>
import TickerPriceTable from 'components/TickerPriceTable'
import LoginRequired from 'components/LoginRequired'

export default {
  name: 'Favourites',
  components: {
    LoginRequired,
    TickerPriceTable
  },
  data () {
    return {
      favourite_items: []
    }
  },
  computed: {
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        return false
      } else {
        return true
      }
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
