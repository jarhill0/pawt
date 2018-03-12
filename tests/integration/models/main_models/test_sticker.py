from ... import bm, tg, user

user = tg.user(user)


def get_sticker():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'gradient2.png')


def test_sticker():
    with bm.use_cassette('test_sticker__test_sticker'):
        name = 'pawt_misc_sticker_testing_by_' + tg.get_me().username
        with open(get_sticker(), 'rb') as f:
            user.create_new_sticker_set(name, 'test_sticker.py', f, '🙃')
        user.add_sticker_to_set(name, 'https://i.imgur.com/BDZfRJg.png', '🍊')

        sticker_set = tg.sticker_set(name)
        assert sticker_set == sticker_set.stickers[0].get_set()
        stickers_orig = sticker_set.stickers
        stickers_orig[1].set_position(0)
        stickers_new = tg.sticker_set(name).stickers

        assert stickers_orig == stickers_new[1:] + stickers_new[:1]

        assert user.chat.send_sticker(stickers_new[0])

        stickers_new[0].delete()
        assert len(tg.sticker_set(name).stickers) == 1
