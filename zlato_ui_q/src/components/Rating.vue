<template>
    <div>
        <q-dialog v-model="card">
            <q-card>
              <q-card-section class="bg-primary text-h6" style=" color: white" >
                {{order.instrument_id.vendor}}
              </q-card-section>
                <q-card-section>
                    <q-rating
                        v-model="stars"
                        aria-placeholder="Please provide a rating for the Vendor!"
                        :max="5"
                        size="32px"
                    />
                </q-card-section>
                <q-card-section>
                    <div>
                        <q-input
                            v-model="rating_text"
                            label="Please leave a review here ..."
                            filled
                            type="textarea"
                            cols="33" rows="10"
                            autogrow
                        />
                    </div>
                </q-card-section>
                <q-separator />
                <q-card-actions align="right">
                    <q-btn flat color="primary" label="Submit" @click="rateVendor" />
                </q-card-actions>
            </q-card>
        </q-dialog>
    </div>
</template>

<script>

import { Notify } from 'quasar'

export default {
  name: 'Rating',
  props: ['data'],
  methods: {
    rateVendor () {
      if (this.stars) {
        if (this.stars > 2) {
          this.card = false
        } else if (this.stars < 3 && this.rating_text.length === 0) {
          Notify.create({
            message: 'Please provide a review for rating below 3',
            position: 'top-right'
          })
          return
        }
      } else {
        Notify.create({
          message: 'Please provide a rating for the given vendor',
          position: 'top-right'
        })
        return
      }
      this.card = false
      const axios = require('axios')
      const data = { vendor_id: this.order.instrument_id.vendor_id, rating: this.stars, rating_text: this.rating_text, is_rated: true, order_id: this.order.order_id }
      const config = {
        method: 'post',
        url: 'http://localhost:8000' + '/api/ratevendor/',
        headers: {
          Authorization: `Token ${this.$q.localStorage.getItem('token')}`
        },
        data: data
      }
      axios(config)
        .then((res) => {
          console.log(res)
          Notify.create({
            message: 'Your review has been successfully delivered!',
            position: 'top-right'
          })
          this.order.is_rated = true
        })
        .catch((err) => {
          console.log(err)
          Notify.create({
            message: 'Your rating could not be submitted!',
            position: 'top-right'
          })
        })
    }
  },
  data () {
    return {
      order: [],
      card: false,
      rating_text: '',
      stars: ''
    }
  },
  created () {
    this.order = this.data[0]
    this.card = this.data[1]
    console.log('Created of rating!')
    console.log(this.data)
  }
}
</script>

<style scoped>

</style>
