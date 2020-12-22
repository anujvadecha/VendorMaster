<template>
<div>
  <div class="q-pa-md">
    <div class="row">
      <div class="col col-sm-6 col-md-6 col-xs-12">
        <q-card class=" q-ma-md" bordered @click="$router.push('Margins')">
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
        <q-card class=" q-ma-md" bordered @click="support_request_method()">
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
    <q-dialog style="" v-model="reset" persistent>
    <q-card class="" style="">
      <q-card-section class="bg-primary text-h6" style=" color: white" >
        Reset Password
      </q-card-section>
       <q-card-section style="background-color: white" >
      <q-btn class="q-ml-md btn-danger" @click="reset=false">Close</q-btn>
      <q-btn class="q-ml-md btn-primary" color="primary" @click="reset=false">Confirm</q-btn>
    </q-card-section>
    </q-card>
  </q-dialog>
  <q-dialog style="" v-model="support"  persistent>
    <q-card class="" style="">
      <q-card-section class="bg-primary text-h6" style=" color: white" >
        Support
      </q-card-section>
       <q-card-section style="background-color: white" >
      <q-btn class="q-ml-md btn-danger" @click="support=false">Close</q-btn>
      <q-btn class="q-ml-md btn-primary" color="primary" @click="support=false">Send request</q-btn>
    </q-card-section>
    </q-card>
  </q-dialog>
</div>
</template>

<script>
import { support_request } from 'src/common/api_calls'
import { Notify } from 'quasar'

export default {
  name: 'Account',
  methods: {
    logout: function () {
      this.$q.localStorage.set('token', '')
      return this.$router.push('Login')
    },
    reset_password: function () {

    },
    support_request_method: function () {
      this.support = true
      support_request({
        username: 'anuj',
        message: 'hey'
      }).then(res => {
        Notify.create({
          message: res,
          position: 'top-right'
        })
      })
    }
  },
  data: function () {
    return {
      reset: false,
      support: false
    }
  },
  created () {

  }
}
</script>

<style scoped>

</style>
