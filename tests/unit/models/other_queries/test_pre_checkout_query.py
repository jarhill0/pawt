from pawt import Telegram
from pawt.models.other_queries import PreCheckoutQuery

data = {'id': 'abc123', 'from': {'id': 123456789, 'is_bot': False,
                                 'first_name': 'Sally'},
        'currency': 'USD', 'total_amount': 1999, 'invoice_payload': 'def456'}
dummy_tg = Telegram('')


def test_pre_checkout_query():
    pcq = PreCheckoutQuery(dummy_tg, data)
    assert pcq.id == 'abc123'
    assert pcq.currency == 'USD'
    assert pcq.user == 123456789
    assert pcq.from_ == 123456789
    assert pcq.total_amount == 1999
    assert pcq.invoice_payload == 'def456'

    assert repr(pcq) == '<PreCheckoutQuery abc123>'

    for known_attr in ('id', 'user', 'from_', 'currency',
                       'total_amount', 'invoice_payload',
                       'shipping_option_id', 'order_info'):
        assert hasattr(pcq, known_attr)
