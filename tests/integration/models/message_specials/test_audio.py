from ... import bm, tg, user

chat = tg.chat(user)


def test_send():
    with bm.use_cassette('test_audio__test_send'):
        message = chat.send_audio(
            'http://www.billwurtz.com/la-de-da-de-da-de-da-de-day-oh.mp3',
            caption='La-de-da-de-da-de-da-de-day-oh!', duration=191,
            performer='Bill Wurtz', title='La de da de da de da de day oh')
        audio = message.audio
        message_2 = audio.send(chat)
        assert message_2.audio == audio
