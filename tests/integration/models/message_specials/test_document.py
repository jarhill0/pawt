from ... import tg, user, bm

chat = tg.chat(user)

def test_send():
    with bm.use_cassette('test_document__test_send'):
        document = chat.send_document(
            'https://upload.wikimedia.org/wikipedia/commons/7/7c/WLAStickers'
            '.pdf').document
        assert document == document.send(chat).document