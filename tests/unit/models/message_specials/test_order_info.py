from pawt.models.message_specials import OrderInfo

dummy_tg = None
dummy_data = {'name': 'Cool Purchase', 'email': 'abc@xyz.com',
              'shipping_address': {'country_code': 'USA',
                                   'state': 'CA',
                                   'city': 'San Francisco',
                                   'street_line1': '1 Telegraph Hill Blvd',
                                   'post_code': '94133'}}


def test_attrs():
    oi = OrderInfo(dummy_tg, dummy_data)
    assert oi.name == 'Cool Purchase'
    assert oi.email == 'abc@xyz.com'

    for known_attr in ('name', 'phone_number', 'email', 'shipping_address'):
        assert hasattr(oi, known_attr)
