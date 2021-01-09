<template>
<div>
  <div class="q-pa-md">
    <div v-if="logged_in">
    <div class="row">
      <div class="col col-sm-6 col-md-6 col-xs-12">
        <q-card class="bg-light-blue-3 q-ma-md" bordered @click="$router.push('Margins')">
          <q-card-section class="text-center">
          <strong>  Account margins</strong>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section class="text-center">
              Margins available from each vendors
          </q-card-section>
        </q-card>
      </div>
      <div class="col col-sm-6 col-md-6 col-xs-12">
        <q-card class="bg-light-blue-3 q-ma-md" bordered @click="support_request_method()">
          <q-card-section class="text-center">
          <strong>Support</strong>
          </q-card-section>
          <q-separator></q-separator>

          <q-card-section class="text-center">
              Send a request for support
          </q-card-section>
        </q-card>
      </div>
       <div class="col col-sm-6 col-md-6 col-xs-12">
        <q-card class=" q-ma-md" bordered >
          <div class="col col-sm-6 col-md-6 col-xs-12">
<!--        <q-card class="bg-white " flat bordered @click="$router.push('Margins')">-->
<!--          <q-card-section class="text-center">-->
<!--          <strong> Account</strong>-->
<!--          </q-card-section>-->
<!--          <q-separator></q-separator>-->
<!--          <q-card-section class="text-center">-->
<!--              {{this.$store.state.user_details.username}}-->
<!--          </q-card-section>-->
<!--        </q-card>-->
      </div>
          <q-card-section class="text-center">
          <strong>Account Settings</strong>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section class="text-center">
              <q-list>
        <q-item
            clickable
            tag="a"
            target="_blank"
            @click="logout()"
          >
          <q-item-section avatar>
          <q-icon class="text-primary" name="mdi-logout" />
        </q-item-section>
        <q-item-section class="text-primary">Logout</q-item-section>
        </q-item>
        <q-item
          @click="reset=true"
            clickable
            tag="a"
            target="_blank"
          >
          <q-item-section avatar>
          <q-icon class="text-primary" name="mdi-lock-reset" />
        </q-item-section>
        <q-item-section class="text-primary">Reset Password</q-item-section>
        </q-item>
      </q-list>
          </q-card-section>
        </q-card>
      </div>

    </div>
  </div>
  <div v-else class="" >
    <LoginRequired page="Account Settings"></LoginRequired>
  </div>
    <q-dialog style="" v-model="reset" persistent>
    <q-card class="" style="">
      <q-card-section class="bg-primary text-h6" style=" color: white" >
        Reset Password
      </q-card-section>
       <q-card-section class="q-ma-md" style="background-color: white" >
         <q-input v-model="new_password1"  label="Enter New Password" />
         <q-input v-model="new_password2"  label="Re-enter new password" />
    </q-card-section>
      <q-card-section>
            <q-btn class="q-ml-md btn-danger" @click="reset=false">Close</q-btn>
      <q-btn class="q-ml-md btn-primary" color="primary" @click="changePassword">Confirm</q-btn>

      </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog style="" v-model="support"  persistent>
    <q-card class="" style="">
      <q-card-section class="bg-primary text-h6" style=" color: white" >
        Support
      </q-card-section>
      <q-card-section>
        <q-input outlined label="Title" v-model="request_title" />
        <br />
        <textarea name="message" v-model="request_message" placeholder="Request" id="" cols="33" rows="10"></textarea>
      </q-card-section>
       <q-card-section style="background-color: white" >
      <q-btn class="q-ml-md btn-danger" @click="support=false">Close</q-btn>
      <q-btn class="q-ml-md btn-primary" color="primary" @click="sendRequest">Send request</q-btn>
    </q-card-section>
    </q-card>
  </q-dialog>

    </div>
</div>
</template>

<script>
// import { support_request } from 'src/common/api_calls'
import { Notify } from 'quasar'
import LoginRequired from 'components/LoginRequired'

export default {
  name: 'Account',
  components: { LoginRequired },
  methods: {
    logout: function () {
      this.$q.localStorage.set('token', '')
      Notify.create({
        message: 'You have been logged out',
        position: 'top-right'
      })
      return this.$router.push('Home')
    },
    reset_password: function () {

    },
    support_request_method: function () {
      this.support = true
      // support_request({
      //   username: 'anuj',
      //   message: 'hey'
      // }).then(res => {
      //   Notify.create({
      //     message: res,
      //     position: 'top-right'
      //   })
      // })
    },
    changePassword () {
      const axios = require('axios')
      const data = { new_password1: this.new_password1, new_password2: this.new_password2 }
      const config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/password/change/',
        headers: {
          Authorization: `Token ${this.$q.localStorage.getItem('token')}`
        },
        data: data
      }
      axios(config)
        .then((res) => {
          console.log(res)
          Notify.create({
            message: 'New password has been set!',
            position: 'top-right',
            timeout: 1000
          })
        })
        .catch(function (error) {
          if (error.response) {
            console.log(error.response.data)
            console.log(error.response.status)
            console.log(error.response.headers)
          }
          Notify.create({
            message: error.response.data.new_password2,
            position: 'top-right',
            timeout: 1000
          })
        })
    },
    sendRequest () {
      const axios = require('axios')
      const data = { title: this.request_title, message: this.request_message }
      const config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/support/',
        headers: {
          Authorization: `Token ${this.$q.localStorage.getItem('token')}`
        },
        data: data
      }
      axios(config)
        .then((res) => {
          console.log(res)
          Notify.create({
            message: 'Request has been succesfully sent!',
            position: 'top-right',
            timeout: 1000
          })
        })
        .catch((err) => {
          console.log(err)
          Notify.create({
            message: 'Error while sending the request',
            position: 'top-right',
            timeout: 1000
          })
        })
    }
  },
  data: function () {
    return {
      reset: false,
      support: false,
      new_password1: '',
      new_password2: '',
      request_title: '',
      request_message: ''
    }
  },
  created () {
    console.log(this.$q.localStorage.getItem('token'))
  },
  computed: {
    logged_in: function () {
      const token = this.$q.localStorage.getItem('token')
      if (token === '' || token === null || token === 'null') {
        console.log('returning false')
        return false
      } else {
        console.log('returning true')
        return true
      }
    }
  }
}
</script>

<style scoped>

</style>
