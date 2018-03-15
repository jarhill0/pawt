from pawt.exceptions import APIException
from pawt.models.other_queries import ShippingQuery
from ... import bm, tg

data = {'id': 'abc123', 'invoice_payload': 'def456',
        'from': {'id': 123456789, 'is_bot': False,
                 'first_name': 'Sally'},
        'shipping_address': {'country_code': 'USA',
                             'state': 'CA',
                             'city': 'San Francisco',
                             'street_line1': '1 Telegraph Hill Blvd',
                             'post_code': '94133'}
        }

prices = [
    ShippingQuery.make_labeled_price('Cheap', 100),
    ShippingQuery.make_labeled_price('Expensive', 10000)
]

option = ShippingQuery.make_shipping_option('def456', 'The main option',
                                             prices)


def test_answer():
    sq = ShippingQuery(tg, data)
    with bm.use_cassette('test_shipping_query__test_answer'):
        try:
            sq.answer(True, [option])
        except APIException as e:  # not registered as merchant
            assert 'QUERY_ID_INVALID' in str(e)
        try:
            sq.answer(False, error_message="It didn't work!")
        except APIException as e:  # not registered as merchant
            assert 'QUERY_ID_INVALID' in str(e)
