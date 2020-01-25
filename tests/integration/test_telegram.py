from . import bm, tg


def test_get_me():
    with bm.use_cassette("test_telegram__test_get_me"):
        me = tg.get_me()
        assert me.is_bot
        assert me == tg.get_me()


def test_get_updates():
    with bm.use_cassette("test_telegram__test_get_updates"):
        updates = tg.get_updates(limit=2, allowed_updates=["message"])
        assert len(updates) == 2
        offset = 0
        for update in updates:
            assert update.message
            offset = max(offset, update.id)
        tg.get_updates(offset=offset + 1, timeout=5)
