<template>
  <div>
    <div v-if="logged_in">
      <div v-if="favourite_items.length > 0">
        <div class="Favourites">
            <TickerPriceTable :render_best="true" :title=None  :instruments_to_render="favourite_items" />
        </div>
      </div>
      <div v-else>
        <center>
          <q-img width="20%" height=20% src="no_results.png"></q-img>
          <div class="q-mt-md">
            <strong class="text-h6">Please select some favourites from home to view them</strong>
          </div>
        </center>
      </div>
    </div>
    <div v-else>
      <LoginRequired  page="or add Favourites"></LoginRequired>
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
    this.$store.state.rightDrawerOpen = false

    this.favourite_items = this.$store.state.instruments.filter(instrument => {
      return instrument.is_favourite === true
    })
  }
}
</script>

<style scoped>
.Favourites {
  color: black;
}
</style>
