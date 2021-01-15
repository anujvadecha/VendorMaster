<template>
<div>
  <div class="">
    <div v-if="logged_in"  >
      <div class="col">
       <div class="col-12">
<!--        <q-card bordered square class="shadow-2" >-->
<!--          <q-card-section class="bg-primary text-white text-h6">-->
<!--          <strong>Account Settings</strong>-->
<!--          </q-card-section>-->
<!--          <q-separator></q-separator>-->
<!--          <q-card-section class="">-->
<!--               <q-btn-->
<!--                 size="lg"-->
<!--              fab-->
<!--              color="white"-->
<!--              icon="mdi-account"-->
<!--              class="absolute text-black"-->
<!--              style="top: 0; right: 12px; transform: translateY(-50%);"-->
<!--        />-->
<!--              {{$store.state.user_details.username}}-->
<!--          </q-card-section>-->
<!--        </q-card>-->
      </div>
    <div class="row">
      <div class="col-12">
        <q-card square flat class=""  >
          <q-card-section class="">
          <strong>  Account margins</strong>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section class="">
             <q-item
            clickable
            tag="a"
            target="_blank"
           @click="$router.push('Margins')"
          >
          <q-item-section avatar>
          <q-icon class="text-primary" name="mdi-locker" />
        </q-item-section>
        <q-item-section class="text-primary">Margins available from each vendors</q-item-section>
        </q-item>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-12">
        <q-separator></q-separator>
        <q-card square flat class=" " @click="support_request_method()">
          <q-card-section class="">
          <strong>Support</strong>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section class="">
            <q-item
            clickable
            tag="a"
            target="_blank"
           @click="support_request_method()"
          >
          <q-item-section avatar>
          <q-icon class="text-primary" name="mdi-account-arrow-right" />
        </q-item-section>
        <q-item-section class="text-primary">Send a request for support</q-item-section>
        </q-item>
          </q-card-section>
        </q-card>
      </div>
       <div class="col-12">
         <q-separator></q-separator>
        <q-card square class="" flat >
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
          <q-card-section class="">
          <strong>Account Settings</strong>
          </q-card-section>
          <q-separator></q-separator>
          <q-card-section class="">
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
  </div>

  <div v-else class="" >
    <LoginRequired page="Account Settings"></LoginRequired>
  </div>
    <q-dialog style="" v-model="reset" >
    <q-card class="" style="">
      <q-card-section class="bg-primary text-h6" style=" color: white" >
        Reset Password
      </q-card-section>
       <q-card-section class="q-ma-md q-gutter-y-md" style="background-color: white" >
         <q-input outlined v-model="new_password1"  label="Enter New Password" />
         <q-input  outlined v-model="new_password2"  label="Re-enter new password" />
    </q-card-section>
      <q-card-section>
            <q-btn class="q-ml-md btn-danger" @click="reset=false">Close</q-btn>
      <q-btn class="q-ml-md btn-primary" color="primary" @click="changePassword">Confirm</q-btn>

      </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog style="" v-model="support" >
    <q-card class="" style="">
      <q-card-section class="bg-primary text-h6" style=" color: white" >
        Support
      </q-card-section>
      <q-card-section>
        <q-input outlined label="Title" v-model="request_title" />
        <br />
        <q-input outlined label="Message" type="textarea" v-model="request_message" id="" cols="33" rows="10"></q-input>
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
