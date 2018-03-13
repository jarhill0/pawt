from pawt.models.message_specials import OrderInfo

dummy_tg = None
address = {'country_code': 'USA',
           'state': 'CA',
           'city': 'San Francisco',
           'street_line1': '1 Telegraph Hill Blvd',
           'post_code': '94133'}
dummy_data = {'name': 'Cool Purchase', 'email': 'abc@xyz.com'}


def test_attrs():
    oi = OrderInfo(dummy_tg, dummy_data)
    assert oi.name == 'Cool Purchase'
    assert oi.email == 'abc@xyz.com'

    for known_attr in ('name', 'phone_number', 'email', 'shipping_address'):
        assert hasattr(oi, known_attr)

    dummy_data['shipping_address'] = address
    oi = OrderInfo(dummy_tg, dummy_data)
    assert oi.shipping_address.city == 'San Francisco'
