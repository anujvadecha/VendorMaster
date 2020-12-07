import { apiService } from "./api.service";

function add_to_favourites(instrument_id) {
  let endpoint = "/api/favourites/";
  return apiService(endpoint, "POST", instrument_id);
}

function remove_from_favourites(instrument_id) {
  let endpoint = "/api/favourites/";
  return apiService(endpoint, "DELETE", instrument_id);
}

function get_orders() {
  let endpoint = window.location.host + "/order/api/orderDetails";
  return apiService(endpoint);
}

export { add_to_favourites, remove_from_favourites, get_orders };
