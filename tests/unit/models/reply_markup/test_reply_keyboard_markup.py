from pawt.exceptions import BadArgument
from pawt.models.reply_markup import ReplyKeyboardMarkupBuilder

EXPECTED = {'keyboard': [
    [{'text': 'Hi'}],
    [
        {'text': 'Who are you?', 'request_contact': True},
        {'text': 'Where are you?', 'request_location': True}
    ]
], 'resize_keyboard': True, 'one_time_keyboard': True, 'selective': True}


def test_building():
    builder = ReplyKeyboardMarkupBuilder()
    assert {'keyboard': [[]]} == builder.build()

    builder = ReplyKeyboardMarkupBuilder()
    builder.add_button('Hi')
    builder.new_row()
    builder.add_button('Who are you?', request_contact=True)
    builder.add_button('Where are you?', request_location=True)
    assert EXPECTED == builder.build(resize_keyboard=True,
                                     one_time_keyboard=True, selective=True)


def test_false_args():
    builder = ReplyKeyboardMarkupBuilder()
    assert {'keyboard': [[]], 'selective': False} == builder.build(
        selective=False)

    builder.add_button('Only location', request_contact=False,
                       request_location=True)

    expected = {'text': 'Only location', 'request_location': True}
    assert expected == builder.build()['keyboard'][0][0]


def test_num_args():
    builder = ReplyKeyboardMarkupBuilder()
    try:
        builder.add_button('should fail', request_contact=True,
                           request_location=True)
        assert False, "Should throw BadArgument"
    except BadArgument:
        pass
