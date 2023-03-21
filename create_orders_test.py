import sender_stand_request

current_track = sender_stand_request.track

# Тест 1. Проверить, что код ответа равен 200
def test_get_order_by_track_get_success_response():

    # В переменную order_response сохраняется результат на GET-Запрос (Получить заказ по его номеру)
    order_response = sender_stand_request.get_order_by_track(current_track)
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
