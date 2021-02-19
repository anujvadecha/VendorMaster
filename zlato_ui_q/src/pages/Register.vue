<template>
<div>
<div class="window-height window-width row justify-center items-center" style="">
    <div class="column q-pa-lg">
      <strong class="text-h6">{{message}}</strong>
      <q-card-section style="">
            <div class="row">
            <q-img
              :src="imageSrc"
              transition="scale-transition"
              width="50px"
            />
             <strong class="text-h6 q-ml-md q-my-md">DeltaBX</strong>
            </div>
          </q-card-section>
          <q-separator color="orange" size="5px"></q-separator>
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl">
              <q-input square clearable v-model="username" type="text" label="Username"
               lazy-rules
               :rules="[ val => !!val || 'Please provide a username']"
              >
                <template v-slot:prepend>
                  <q-icon name="email"/>
                </template>
              </q-input>
              <q-input square clearable v-model="email" type="email" label="Email"
               lazy-rules
               :rules="[val => !!val || 'Email is missing!', isValidEmail]"
              >
                <template v-slot:prepend>
                  <q-icon name="email" />
                </template>
              </q-input>
              <q-input square clearable v-model="password1" type="password" label="Password"
               lazy-rules
               :rules="[val => val.length >= 8 || 'Please enter a minimum of 8 characters']"
              >
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
      password2: '',
      imageSrc: 'logo.png'
    }
  },
  methods: {
    registerUser () {
      if (this.password1 !== this.password2) {
        Notify.create({
          message: 'The passwords entered do not match!'
        })
        return
      }
      const axios = require('axios')
      const router = this.$router
      const data = { username: this.username, email: this.email, password1: this.password1, password2: this.password2, imageSrc: 'logo.png' }
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
            message: 'The password entered is too common',
            position: 'top-right',
            timeout: 1000
          })
        })
    },
    isValidEmail () {
      const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
      return emailPattern.test(this.email) || 'Invalid email entered!'
    }
  }
}
</script>

<style scoped>

</style>
