from pawt.exceptions import APIException, BadType
from pawt.models.reply_markup import InlineKeyboardMarkupBuilder
from ... import bm, tg, user

chat = tg.chat(user)

img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Tursiops_' \
      'truncatus_01.jpg/800px-Tursiops_truncatus_01.jpg'

builder = InlineKeyboardMarkupBuilder()
builder.add_button('click on this url', url='https://duckduckgo.com')
REPLY_MARKUP = builder.build()


def test_edit_text_message():
    with bm.use_cassette('test_message__test_edit_text_message'):
        message = chat.send_message('Hello World!')
        message = message.edit('Hello *bold* World! https://t.me',
                               parse_mode='Markdown',
                               disable_web_page_preview=True)
        assert message.text == 'Hello bold World! https://t.me'
        assert str(message.entities[0]) == 'bold'


def test_edit_caption_bad_params():
    with bm.use_cassette('test_message__test_edit_caption_bad_params'):
        message = chat.send_photo(img, 'Hi')
        try:
            message.edit('ok', parse_mode='HTML')
            assert False, 'should raise BadType'
        except BadType:
            pass

        try:
            message.edit('ok', disable_web_page_preview=True)
            assert False, 'should raise BadType'
        except BadType:
            pass


def test_edit_caption():
    with bm.use_cassette('test_message__test_edit_caption'):
        message = chat.send_photo(img, 'Hi')
        message = message.edit('yo')
        assert message.caption == 'yo'


def test_edit_only_reply_markup():
    with bm.use_cassette('test_message__test_edit_only_reply_markup'):
        message = chat.send_message('Hi!')
        message.edit(reply_markup=REPLY_MARKUP)


def test_edit_live_location():
    with bm.use_cassette('test_message__test_edit_live_location'):
        message = chat.send_location(latitude=37.8720789,
                                     longitude=-122.258008,
                                     live_period=120)
        message.edit_live_location(47.6205063, -122.3514661,
                                   reply_markup=REPLY_MARKUP)


def test_stop_live_location():
    with bm.use_cassette('test_message__test_stop_live_location'):
        message = chat.send_location(latitude=37.8720789,
                                     longitude=-122.258008,
                                     live_period=120)
        message.stop_live_location(reply_markup=REPLY_MARKUP)


def test_delete():
    with bm.use_cassette('test_message__test_delete'):
        message = chat.send_message('Hello World!')
        message.delete()
        try:
            # try deleting again to make sure it's gone
            message.delete()
            assert False, 'should raise APIException'
        except APIException as e:
            assert 'message to delete not found' in str(e)


def test_replies():
    pass  # todo
