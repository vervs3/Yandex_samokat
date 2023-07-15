import sender_stand_request

def positive_assert():
    # В переменную response сохраняется результат запроса на проверку заказа по треку:
    response = sender_stand_request.get_order_by_track()
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200

# Евгения Чепрасова(Веремей), 6-я когорта — Финальный проект. Инженер по тестированию плюс

#Тест 1. Успешная проверка заказа по треку
def test_receive_order_by_track():
    positive_assert()
