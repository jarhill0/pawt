from pawt.models.message_specials import OrderInfo

dummy_tg = None
dummy_data = {'name': 'Cool Purchase', 'email': 'abc@xyz.com'}


def test_attrs():
    oi = OrderInfo(dummy_tg, dummy_data)
    assert oi.name == 'Cool Purchase'
    assert oi.email == 'abc@xyz.com'

    for known_attr in ('name', 'phone_number', 'email', 'shipping_address'):
        assert hasattr(oi, known_attr)
