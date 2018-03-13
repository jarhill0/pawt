from pawt.models.message_specials import Invoice
from ... import bm, tg

dummy_data = {'title': 'Electric Razor',
              'description': 'For shaving your face.',
              'start_parameter': '',
              'currency': 'USD',
              'total_amount': 1999}


def test_format_cost():
    invoice = Invoice(tg, dummy_data)
    with bm.use_cassette('test_invoice__test_format_cost'):
        assert invoice.format_cost() == '$19.99'
        assert str(invoice) == 'Electric Razor ($19.99)'
