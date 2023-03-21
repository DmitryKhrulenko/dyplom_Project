import configuration
import requests
import data


# POST-Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order(data.order_body)
track = response.json()["track"]


# GET-Запрос на Получить заказ по его номеру
def get_order_by_track(track):

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params={"t": track})
response = get_order_by_track(track)

