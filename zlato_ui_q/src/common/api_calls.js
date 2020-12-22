import { apiService } from './api.service'
const base_url = 'http://127.0.0.1:8000'

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

export {
  base_url,
  add_to_favourites,
  remove_from_favourites,
  get_orders,
  place_order,
  cancel_order,
  get_user_margins,
  support_request
}
