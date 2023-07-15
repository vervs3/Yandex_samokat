import configuration
import requests
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=data.order_body,
                         headers=data.headers)

def get_order_by_track():
    trackID = post_new_order().json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(trackID))
