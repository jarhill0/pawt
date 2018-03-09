from pawt.models.reply_markup import force_reply
from .. import bm, game, tg, user

chat = tg.chat(user)


def test_load():
    with bm.use_cassette('test_chat__test_load'):
        chat.get_chat()
    assert chat.type.value == 'private'


def test_send_message():
    with bm.use_cassette('test_chat__test_send_message'):
        mess = chat.send_message('Hello world')
    assert mess.text == 'Hello world'


def test_special_arguments():
    with bm.use_cassette('test_chat__test_special_arguments'):
        messages = [
            chat.send_message('This is *bold*.', parse_mode='Markdown'),
            chat.send_message('https://github.com',
                              disable_web_page_preview=True),
            chat.send_message('Shh', disable_notification=True),
            chat.send_message('Talk to me', reply_markup=force_reply())
        ]

    assert messages[0].text == 'This is bold.'


def get_pdf():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'denevi.pdf')


def test_send_document():
    with open(get_pdf(), 'rb') as pdf:
        with bm.use_cassette('test_chat__test_send_document'):
            mess = chat.send_document(pdf, 'Two short stories')

    assert mess.caption == 'Two short stories'


def test_send_video():
    with bm.use_cassette('test_chat__test_send_video'):
        mess = chat.send_video('https://i.imgur.com/LdE8jcw.mp4',
                               duration=8, width=100, height=400,
                               caption='baloncesto')
    assert mess.caption == 'baloncesto'


def test_send_voice():
    with bm.use_cassette('test_chat__test_send_voice'):
        mess = chat.send_voice(
            'https://upload.wikimedia.org/wikipedia/commons/4/47/Beethoven_Moonlight_2nd_movement.ogg',
            duration=125, caption='File:Beethoven Moonlight 2nd movement.ogg')
    assert mess.caption == 'File:Beethoven Moonlight 2nd movement.ogg'


def test_send_game():
    with bm.use_cassette('test_chat__test_send_game'):
        mess = chat.send_game(game)
    assert repr(mess.game).startswith('<Game ')
