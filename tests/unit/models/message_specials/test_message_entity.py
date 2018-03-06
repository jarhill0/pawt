from pawt import Telegram
from pawt.models.message_specials import Mention, Hashtag, BotCommand, Url, \
    Email, Bold, Italic, Code, Pre, TextLink, TextMention

dummy_tg = Telegram(token='')

# todo test the rest of the classes

def test_mention():
    data = {'offset': 3, 'length':12}
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


def test_equality():
    pass

