from pawt.models.message_specials import SuccessfulPayment

dummy_tg = None
order_info = {'name': 'Cool Purchase', 'email': 'abc@xyz.com',
              'shipping_address': {'country_code': 'USA',
                                   'state': 'CA',
                                   'city': 'San Francisco',
                                   'street_line1': '1 Telegraph Hill Blvd',
                                   'post_code': '94133'}}
dummy_data = {'currency': 'USD', 'total_amount': 1999,
              'invoice_payload': 'abc123',
              'telegram_payment_charge_id': '12345',
              'provider_payment_charge_id': '67890'}


def test_attrs():
    sp = SuccessfulPayment(dummy_tg, dummy_data)
    assert sp.currency == 'USD'
    assert sp.total_amount == 1999
    assert sp.invoice_payload == 'abc123'
    assert sp.telegram_payment_charge_id == '12345'
    assert sp.provider_payment_charge_id == '67890'

    for known_attr in ('currency', 'total_amount', 'invoice_payload',
                       'shipping_option_id', 'telegram_payment_charge_id',
                       'provider_payment_charge_id', 'order_info'):
        assert hasattr(sp, known_attr)

    dummy_data['order_info'] = order_info
    sp = SuccessfulPayment(dummy_tg, dummy_data)
    assert sp.order_info.shipping_address.state == 'CA'
