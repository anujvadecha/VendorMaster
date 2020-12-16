<template>
<div>

</div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login_action: function () {
      const store = this.$store
      console.log('login action with' + this.email + this.password)
      var axios = require('axios')
      var data = JSON.stringify({ username: this.email, password: this.password })
      var config = {
        method: 'post',
        url: 'http://127.0.0.1:8000/api/rest-auth/login/',
        headers: {
          'Content-Type': 'application/json',
          Cookie: 'csrftoken=qY3htpK0KxfhuDlT7E47PB3qqrxG7rkF5EHi7YcvteLej7mJYd3Tx6pReQTwsoGP; sessionid=hcvf8yblipbwwzdjp2aw8djgu4ovr4g4'
        },
        data: data
      }
      axios(config)
        .then(function (response) {
          store.dispatch('set_token', response.data.key)
          console.log(JSON.stringify(response.data))
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.q-card {
  width: 360px;
}
</style>
