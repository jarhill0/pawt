from ... import bm, tg, user

user = tg.user(user)


def test_file():
    emojis = '😀😃😇'
    title = "'test_file__test_file'"
    url = 'https://i.imgur.com/BDZfRJg.png'
    with bm.use_cassette('test_file__test_file'):
        set_name = 'pawt_test_file_by_{}'.format(tg.get_me().username)
        user.create_new_sticker_set(name=set_name, title=title, png_sticker=url,
                                    emojis=emojis)
        file = tg.sticker_set(set_name).stickers[0].file
        file.refresh()
        filecopy = file.get_file()
        assert file.__dict__ == filecopy.__dict__
        assert file.link.startswith('https://api.telegram.org/file/bot')
