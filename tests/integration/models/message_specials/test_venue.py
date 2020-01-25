from ... import bm, tg, user

chat = tg.chat(user)


def test_send():
    with bm.use_cassette("test_venue__test_send"):
        venue = chat.send_venue(
            latitude=37.8720789,
            longitude=-122.258008,
            title="The Campanile",
            address="Sather Tower, Berkeley, CA 94720",
        ).venue
        assert venue.address == venue.send(chat).venue.address
