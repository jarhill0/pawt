from pawt.models.reply_markup import reply_keyboard_remove


def test_output():
    assert reply_keyboard_remove() == {'remove_keyboard': True}
    assert reply_keyboard_remove(True) == {'remove_keyboard': True,
                                           'selective': True}
    assert reply_keyboard_remove(False) == {'remove_keyboard': True,
                                            'selective': False}
