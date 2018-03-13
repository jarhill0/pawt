from ... import bm, tg, user

chat = tg.chat(user)

def get_voice():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'voice.ogg')

def test_send():
    with bm.use_cassette('test_voice__test_send'):
        with open(get_voice(), 'rb') as v:
            voice = chat.send_voice(v).voice
        assert voice == voice.send(user).voice