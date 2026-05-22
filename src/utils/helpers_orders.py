from src.api.orders_api import OrdersAPI


def get_base_order_payload() -> dict:
    """Базовый payload для создания заказа без цвета."""
    return {
        "firstName": "Валентин",
        "lastName": "Миханоша",
        "address": "Москва, Тверская 1",
        "metroStation": "1",
        "phone": "+79990000000",
        "rentTime": 5,
        "deliveryDate": "2026-05-13",
        "comment": "Автотест заказа",
    }


def create_order(comment: str | None = None) -> int:
    """
    Создать заказ и вернуть track.

    comment — текст комментария, если нужно отличать сценарии
    (например, принятие заказа / получить заказ по треку).
    """
    payload = {
        **get_base_order_payload(),
        "color": ["BLACK"],
    }
    if comment is not None:
        payload["comment"] = comment

    response = OrdersAPI.create_order(payload)
    assert response.status_code == 201
    body = response.json()
    track = body.get("track")
    assert isinstance(track, int)
    return track


def get_order_id_by_track(track: int) -> int:
    """Получить id заказа по его track (для accept нужна именно id)."""
    response = OrdersAPI.get_order_by_track(track)
    assert response.status_code == 200
    body = response.json()
    order = body.get("order") or body
    order_id = order.get("id")
    assert isinstance(order_id, int)
    return order_id