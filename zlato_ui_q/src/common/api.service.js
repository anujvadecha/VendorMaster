// import { CSRF_TOKEN } from './csrf_token.js'
import store from 'src/store/index'

function handleResponse (response) {
  if (response.status === 204) {
    return ''
  } else if (response.status === 404) {
    return null
  } else {
    return response.data
  }
}

function apiService (endpoint, method, data) {
  // D.R.Y. code to make HTTP requests to the REST API backend using fetch
  // const store = this.$store.state.token
  // console.log('inside api service token is' + store)
  // const config = {
  //   method: method || 'GET',
  //   body: data !== undefined ? JSON.stringify(data) : null,
  //   headers: {
  //     'content-type': 'application/json',
  //     'X-CSRFTOKEN': CSRF_TOKEN
  //   }
  // }
  // return fetch(endpoint, config)
  //   .then(handleResponse)
  //   .catch(error => console.log(error))
  var axios = require('axios')
  var config = {
    method: method || 'GET',
    url: endpoint,
    headers: {
      Authorization: 'Token ' + store.state.token,
      'Content-Type': 'application/json'
    },
    data: data
  }
  return axios(config)
    .then(response => handleResponse(response))
    .catch(function (error) {
      console.log(error)
    })
}

export { apiService }
