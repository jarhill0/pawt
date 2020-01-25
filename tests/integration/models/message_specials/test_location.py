from ... import bm, tg, user

chat = tg.chat(user)


def test_send():
    with bm.use_cassette("test_location__test_send"):
        location = chat.send_location(
            latitude=37.8720789, longitude=-122.258008
        ).location
        assert str(location) == str(location.send(chat).location)
