from pawt import Telegram
from pawt.exceptions import BadArgument
from pawt.models.other_queries import PreCheckoutQuery

data = {
    "id": "abc123",
    "from": {"id": 123456789, "is_bot": False, "first_name": "Sally"},
    "currency": "USD",
    "total_amount": 1999,
    "invoice_payload": "def456",
    "order_info": {
        "name": "Cool Purchase",
        "email": "abc@xyz.com",
        "address": {
            "country_code": "USA",
            "state": "CA",
            "city": "San Francisco",
            "street_line1": "1 Telegraph Hill Blvd",
            "post_code": "94133",
        },
    },
}
dummy_tg = Telegram("")


def test_pre_checkout_query():
    pcq = PreCheckoutQuery(dummy_tg, data)
    assert pcq.id == "abc123"
    assert pcq.currency == "USD"
    assert pcq.user == 123456789
    assert pcq.from_ == 123456789
    assert pcq.total_amount == 1999
    assert pcq.invoice_payload == "def456"

    assert repr(pcq) == "<PreCheckoutQuery abc123>"

    for known_attr in (
        "id",
        "user",
        "from_",
        "currency",
        "total_amount",
        "invoice_payload",
        "shipping_option_id",
        "order_info",
    ):
        assert hasattr(pcq, known_attr)


def test_validation():
    pcq = PreCheckoutQuery(dummy_tg, data)
    try:
        pcq.answer(False)
        assert False, "should raise BadArgument"
    except BadArgument:
        pass

    try:
        pcq.answer(True, "There was an error")
        assert False, "should raise BadArgument"
    except BadArgument:
        pass
