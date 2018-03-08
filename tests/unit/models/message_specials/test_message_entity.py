from pawt import Telegram
from pawt.models.message_specials import Bold, BotCommand, Code, Email, Hashtag, \
    Italic, Mention, Pre, TextLink, TextMention, Url

dummy_tg = Telegram(token='')


# todo test the rest of the classes

def test_mention():
    data = {'offset': 3, 'length': 12}
    text = 'Hi Ben Franklin!'
    m = Mention(dummy_tg, data, text)
    assert m.content == 'Ben Franklin'
    assert str(m) == m.content
    assert repr(m) == '<Mention: Ben Franklin>'


def test_hashtag():
    data = {'offset': 6, 'length': 4}
    text = 'Dummy #lit, bruh'
    h = Hashtag(dummy_tg, data, text)
    assert h.content == '#lit'
    assert str(h) == h.content
    assert repr(h) == '<Hashtag: #lit>'


def test_botcommand():
    data = {'offset': 3, 'length': 10}
    text = 'ok /go@my_bot now'
    bc = BotCommand(dummy_tg, data, text)
    assert bc.content == '/go@my_bot'
    assert str(bc) == bc.content
    assert repr(bc) == '<BotCommand: /go@my_bot>'

    assert bc.command == '/go'


def test_url():
    data = {'offset': 6, 'length': 22}
    text = 'Go to https://duckduckgo.com now!'
    u = Url(dummy_tg, data, text)
    assert u.content == 'https://duckduckgo.com'
    assert str(u) == u.content
    assert repr(u) == '<Url: https://duckduckgo.com>'


def test_email():
    data = {'offset': 12, 'length': 9}
    text = 'Email me at hi@hi.com if you want'
    e = Email(dummy_tg, data, text)
    assert e.content == 'hi@hi.com'
    assert str(e) == e.content
    assert repr(e) == '<Email: hi@hi.com>'


def test_bold():
    data = {'offset': 10, 'length': 4}
    text = 'This test must pass.'
    b = Bold(dummy_tg, data, text)
    assert b.content == 'must'
    assert str(b) == b.content
    assert repr(b) == '<Bold: must>'


def test_italic():
    data = {'offset': 2, 'length': 4}
    text = 'I love this test.'
    i = Italic(dummy_tg, data, text)
    assert i.content == 'love'
    assert str(i) == i.content
    assert repr(i) == '<Italic: love>'


def test_code():
    data = {'offset': 4, 'length': 21}
    text = 'Use python3 setup.py test to run these tests.'
    c = Code(dummy_tg, data, text)
    assert c.content == 'python3 setup.py test'
    assert str(c) == c.content
    assert repr(c) == '<Code: python3 setup.py test>'


def test_pre():
    data = {'offset': 5, 'length': 10}
    text = 'um,\n\nWUT\nUU\nT T\n\n…'
    p = Pre(dummy_tg, data, text)
    assert p.content == 'WUT\nUU\nT T'
    assert str(p) == p.content
    assert repr(p) == '<Pre: WUT\nUU\nT T>'


def test_textlink():
    data = {'offset': 6, 'length': 4, 'url': 'https://duckduckgo.com'}
    text = 'Click here to search.'
    tl = TextLink(dummy_tg, data, text)
    assert tl.content == 'here'
    assert tl.url == 'https://duckduckgo.com'
    assert str(tl) == tl.content
    assert repr(tl) == '<TextLink: here>'


def test_textmention():
    data = {'offset': 6, 'length': 4, 'user': {'id': 123456789,
                                               'is_bot': False,
                                               'first_name': 'Sally'}}
    text = 'Click here to view my profile.'
    tm = TextMention(dummy_tg, data, text)
    assert tm.content == 'here'
    assert tm.user == 123456789
    assert str(tm) == tm.content
    assert repr(tm) == '<TextMention: here>'
