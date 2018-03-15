from pawt.exceptions import APIException
from pawt.models.other_queries import PreCheckoutQuery
from ... import bm, tg

data = {'id': 'abc123', 'from': {'id': 123456789, 'is_bot': False,
                                 'first_name': 'Sally'},
        'currency': 'USD', 'total_amount': 1999, 'invoice_payload': 'def456'}
pcq = PreCheckoutQuery(tg, data)


def test_amount():
    with bm.use_cassette('test_util__get_currencies_json'):
        assert '$19.99' == pcq.format_amount()


def test_answer():
    with bm.use_cassette('test_pre_checkout_query__test_answer'):
        try:
            pcq.answer(True)
        except APIException as e:
            # I don't actually have a registered commerce account
            assert 'QUERY_ID_INVALID' in str(e)
