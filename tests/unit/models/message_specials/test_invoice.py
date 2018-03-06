from pawt.models.message_specials import Invoice

dummy_tg = None
dummy_data = {'title': 'Electric Razor',
              'description': 'For shaving your face.',
              'start_parameter': '',
              'currency': 'USD',
              'total_amount': 1999}


def test_attrs():
    i = Invoice(dummy_tg, dummy_data)
    assert i.title == 'Electric Razor'
    assert i.description == 'For shaving your face.'
    assert i.start_parameter == ''
    assert i.currency == 'USD'
    assert i.total_amount == 1999
    assert repr(i) == '<Invoice Electric Razor>'

    for known_attr in ('title', 'description', 'start_parameter', 'currency',
                       'total_amount'):
        assert hasattr(i, known_attr)
