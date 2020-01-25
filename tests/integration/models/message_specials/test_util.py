from pawt.models.message_specials import format_currency
from ... import bm, tg


def test_large_amount():
    with bm.use_cassette("test_util__get_currencies_json"):
        assert "$1,000,000.00" == format_currency("USD", 100000000, tg)


def test_no_decimal():
    with bm.use_cassette("test_util__get_currencies_json"):
        assert "CLP 1.234" == format_currency("CLP", 1234, tg)


def test_symbol_space_configurations():
    # symbol left, with space
    with bm.use_cassette("test_util__get_currencies_json"):
        assert "AED 1,234.56" == format_currency("AED", 123456, tg)

    # symbol left, no space
    with bm.use_cassette("test_util__get_currencies_json"):
        assert "AFN1,234.56" == format_currency("AFN", 123456, tg)

    # symbol right, with space
    with bm.use_cassette("test_util__get_currencies_json"):
        assert "1,234.56 AMD" == format_currency("AMD", 123456, tg)

    # symbol right, no space
    with bm.use_cassette("test_util__get_currencies_json"):
        assert "1.234,56ALL" == format_currency("ALL", 123456, tg)
