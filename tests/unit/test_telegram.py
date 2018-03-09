from pawt import Telegram
from pawt.models import Chat, File, StickerSet, User

DUMMY_TOKEN = '542097629:AAGxYuGjLUWR7X1xf1x3kszU7DjRSCNE9VU'


def test_creation():
    tg = Telegram(DUMMY_TOKEN)


def test_custom_url():
    tg = Telegram(DUMMY_TOKEN, url='http://mysite.com/{token}')
    assert tg.path == \
           'http://mysite.com/542097629:AAGxYuGjLUWR7X1xf1x3kszU7DjRSCNE9VU/'


def test_message():
    data = dict(message_id=12345, date=1234567890,
                chat=dict(id=67890, type='private'))
    message = Telegram('').message(data=data)
    assert repr(message) == '<Message 12345>'


def test_sticker():
    sticker = Telegram('').sticker(data=dict(width=512, height=510,
                                             file_id=12345))
    assert sticker.width == 512
    assert sticker.height == 510


def test_copy():
    tg = Telegram(DUMMY_TOKEN)
    copy = tg.copy()

    assert tg is not copy
    assert tg.token == copy.token


def test_alt_url():
    url = 'https://altelapi.com/bot/{token}'  # without trailing slash
    tg = Telegram(DUMMY_TOKEN, url=url)

    assert tg.path == tg.copy().path


def test_return_types():
    dummy_id = 23456
    tg = Telegram(DUMMY_TOKEN)

    chat = tg.chat(dummy_id)
    assert isinstance(chat, Chat)

    file = tg.file(dummy_id)
    assert isinstance(file, File)

    sticker_set = tg.sticker_set('set name')
    assert isinstance(sticker_set, StickerSet)

    user = tg.user(dummy_id)
    assert isinstance(user, User)
