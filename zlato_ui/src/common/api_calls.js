import { apiService } from "./api.service";
const base_url = "127.0.0.1:8000";

function add_to_favourites(instrument_id) {
  let endpoint = base_url + "/api/favourites/";
  return apiService(endpoint, "POST", instrument_id);
}

function remove_from_favourites(instrument_id) {
  let endpoint = base_url + "/api/favourites/";
  console.log(instrument_id);
  return apiService(endpoint, "DELETE", instrument_id);
}

function get_orders() {
  let endpoint = base_url + +"/order/api/orderDetails";
  return apiService(endpoint);
}

export { base_url, add_to_favourites, remove_from_favourites, get_orders };
