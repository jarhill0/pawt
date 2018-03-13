from ... import bm, tg, user

chat = tg.chat(user)
url = ('https://upload.wikimedia.org/wikipedia/commons/b/b2/RhB_Ge_4-4_III_'
       'UNESCO_Weltkulturerbe_auf_Landwasserviadukt.jpg')


def test_send():
    with bm.use_cassette('test_photo__test_send'):
        photo = chat.send_photo(url).photo
        assert photo.max_size == photo.send(chat).photo.max_size
