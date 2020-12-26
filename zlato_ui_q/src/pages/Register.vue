<template>
<div>
<div
    class="window-height window-width row justify-center items-center"
       style="">
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width:300px;height:485px;">
          <q-card-section style="background-color: lightgrey">
            <q-img
            :src="imageSrc"
            transition="scale-transition"
            width="40px"
            />
            <div class="absolute-bottom-right q-pr-md" style="transform: translateY(50%);">
              <q-btn fab icon="add" color="primary" />
            </div>
          </q-card-section>
          <q-></q->
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl">
              <q-input square clearable v-model="username" type="text" label="Username">
                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>
              <q-input square clearable v-model="email" type="email" label="Email">
                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>
              <q-input square clearable v-model="password1" type="password" label="Password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
              <q-input square clearable v-model="password2" type="password" label="Re-type your password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-lg">
            <q-btn @click="registerUser()" unelevated size="lg" color="primary" class="full-width text-white" label="Sign Up" />
          </q-card-actions>
          <q-card-section class="text-center q-pa-sm">
            <p class="text-grey-6"> Forgot your password? </p>
          </q-card-section>
        </q-card>
      </div>
    </div>
    </div>
</div>
</template>

<script>
import { Notify } from 'quasar'

export default {
  data () {
    return {
      username: '',
      email: '',
      password1: '',
      password2: ''
    }
  },
  methods: {
    registerUser () {
      const axios = require('axios')
      const router = this.$router
      const data = { username: this.username, email: this.email, password1: this.password1, password2: this.password2 }
      const quasar_q = this.$q
      const config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/registration',
        headers: {
          'Content-Type': 'application/json'
        },
        data: data
      }
      axios(config)
        .then((res) => {
          quasar_q.localStorage.set('token', res.data.key)
          console.log('Pushed to home')
          router.push('Home')
        })
        .catch(function (err) {
          console.log(err)
          Notify.create({
            message: 'Incorrect format of registration details',
            position: 'top-right',
            timeout: 1000
          })
        })
    }
  }
}
</script>

<style scoped>

</style>
