<template>
<div id="q-app">
    <div class="row justify-center items-center" style="">
      <div class="column q-pa-lg">
        <q-card-section style="">
          <div class="row">
            <q-img
            :src="imageSrc"
            transition="scale-transition"
            width="50px"
            />
            <strong class="text-h6 justify-center items-center ">User Activation</strong>
            </div>
          </q-card-section>
          <q-separator color="orange" size="5px"></q-separator>
          <q-card-section>
            <q-form @submit="submitForm" class="q-px-sm q-pt-xl">
              <q-input
                name="phone_number"
                square clearable
                outlined
                v-model="phone_number"
                label="Your phone number "
                lazy-rules
                :rules="[ val => val && val.length === 10 || 'Please type something']"
              >
              </q-input>
              <q-file
                name="profile_picture"
                square clearable
                label="Profile picture"
                outlined
                v-model="profile_picture"
              >
                <template v-slot:prepend>
                  <q-icon name="image" />
                </template>
              </q-file>
              <br />
              <q-file
                name="pan_card"
                square clearable
                label="Pan Card"
                outlined
                v-model="pan_card"
                lazy-rules
                :rules="[ val => val || 'Please attach your pancard']"
              >
                <template v-slot:prepend>
                  <q-icon name="attach_file" />
                </template>
              </q-file>
              <q-file
                name="business_card"
                square clearable
                label="Business Card"
                outlined
                v-model="business_card"
                lazy-rules
                :rules="[ val => val || 'Please attach your pancard']"
              >
                <template v-slot:prepend>
                  <q-icon name="attach_file" />
                </template>
              </q-file>
              <q-input
                name="reference_1_name"
                square clearable
                outlined
                v-model="reference_1_name"
                label="Name for reference "
              >
              </q-input>
              <br />
              <q-input
                name="reference_1_mobile"
                square clearable
                outlined
                v-model="reference_1_mobile"
                label="Phone number for reference "
                lazy-rules
                :rules="[ val => val && val.length === 10 || 'Please type something']"
              >
              </q-input>
              <q-input
                name="reference_2_name"
                square clearable
                outlined
                v-model="reference_2_name"
                label="Name for reference "
              >
              </q-input>
              <br />
              <q-input
                name="reference_2_mobile"
                square clearable
                outlined
                v-model="reference_2_mobile"
                label="Phone number for reference "
              >
              </q-input>
              <br />
              <q-btn type="submit" unelevated size="lg" color="primary" class="full-width text-white" label="Activate" />
            </q-form>
          </q-card-section>
        <!-- <q-card-actions class="q-px-lg">
          <q-btn type="submit" unelevated size="lg" color="primary" class="full-width text-white" label="Activate" />
        </q-card-actions> -->
      </div>
    </div>
  </div>
</template>

<script>
import { Notify } from 'quasar'

export default {
  name: 'RegistrationForm',
  data () {
    return {
      phone_number: '',
      profile_picture: '',
      pan_card: '',
      business_card: '',
      reference_1_name: '',
      reference_1_mobile: '',
      reference_2_name: '',
      reference_2_mobile: ''
    }
  },
  methods: {
    submitForm (evt) {
      const formData = new FormData(evt.target)
      const axios = require('axios')
      // const url = window.location.host
      // console.log(this.profile_picture)
      formData.append('profile_picture', this.profile_picture)
      formData.append('pan_card', this.pan_card)
      formData.append('business_card', this.business_card)
      const data = []
      for (const [name, value] of formData.entries()) {
        if (value.length > 0) {
          data.push({
            name,
            value
          })
        }
      }
      console.log(data)
      const config = {
        method: 'put',
        url: 'http://127.0.0.1:8000/user/api/activateUser',
        headers: {
          'Content-type': 'multipart/form-data',
          // 'Content-Disposition': 'attachment; filename=file',
          // filename: 'file',
          Authorization: `Token ${this.$q.localStorage.getItem('token')}`
        },
        data: data
      }
      axios(config, formData)
        .then((res) => {
          console.log(res)
          Notify.create({
            message: 'Registration completed! Activation status under review',
            position: 'top-right',
            timeout: 1000
          })
        })
        .catch((err) => {
          console.log(err)
          Notify.create({
            message: 'Error! Invalid format of details entered',
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
