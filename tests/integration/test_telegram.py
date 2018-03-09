from . import bm, tg

def test_get_me():
    with bm.use_cassette('test_telegram__test_get_me'):
        me = tg.get_me()
        assert me.is_bot
        assert me == tg.get_me()