import { apiService } from './api.service'
const base_url = 'https://admin.deltabx.com'
const base_websocket_url = 'admin.deltabx.com'
// const base_url = 'http://localhost:8000'
// const base_websocket_url = 'localhost:8000'

function add_to_favourites (instrument_id) {
  const endpoint = base_url + '/api/favourites/'
  return apiService(endpoint, 'POST', instrument_id)
}

function support_request (data) {
  const endpoint = base_url + '/api/support/'
  return apiService(endpoint, 'POST', data)
}

function remove_from_favourites (instrument_id) {
  const endpoint = base_url + '/api/favourites/'
  var instrument = { instrument_id: instrument_id }
  return apiService(endpoint, 'DELETE', instrument)
}

function get_orders () {
  const endpoint = base_url + '/order/api/orders'
  return apiService(endpoint, 'GET', null)
}

function place_order (order) {
  const endpoint = base_url + '/order/api/orders'
  return apiService(endpoint, 'POST', order)
}

function cancel_order (order) {
  const endpoint = base_url + '/order/api/orders'
  return apiService(endpoint, 'DELETE', order)
}

function get_user_margins () {
  const endpoint = base_url + '/order/api/usermargins'
  return apiService(endpoint, 'GET', null)
}

function get_user_details () {
  const endpoint = base_url + '/api/rest-auth/user'
  return apiService(endpoint, 'GET', null)
}

function rate_order (data) {
  const endpoint = base_url + '/api/ratevendor/'
  return apiService(endpoint, 'POST', data)
}

function activate_user (data) {
  const endpoint = base_url + '/user/api/activateUser'
  return apiService(endpoint, 'POST', data)
}

export {
  base_url,
  add_to_favourites,
  remove_from_favourites,
  get_orders,
  place_order,
  cancel_order,
  get_user_margins,
  support_request,
  get_user_details,
  base_websocket_url,
  rate_order,
  activate_user
}
