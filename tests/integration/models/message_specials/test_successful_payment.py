from pawt.models.message_specials import SuccessfulPayment
from ... import bm, tg

order_info = {'name': 'Cool Purchase', 'email': 'abc@xyz.com',
              'shipping_address': {'country_code': 'USA',
                                   'state': 'CA',
                                   'city': 'San Francisco',
                                   'street_line1': '1 Telegraph Hill Blvd',
                                   'post_code': '94133'}}
dummy_data = {'currency': 'USD', 'total_amount': 1999,
              'invoice_payload': 'abc123',
              'telegram_payment_charge_id': '12345',
              'provider_payment_charge_id': '67890',
              'order_info': order_info}


def test_format_cost():
    sp = SuccessfulPayment(tg, dummy_data)
    with bm.use_cassette('test_successful_payment__test_format_cost'):
        assert repr(sp) == '<SuccessfulPayment $19.99>'
        assert sp.format_cost() == '$19.99'
