from pawt.models import MaskPosition
from .. import bm, tg, user

user = tg.user(user)


def get_sticker():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'gradient2.png')


def test_sticker_set():
    emojis = '😀😃'
    mask_position = MaskPosition(point='mouth')
    title = 'Testing: the sticker set'
    with bm.use_cassette('test_user__test_sticker_set'):
        name = 'pawt_test_set_by_{}'.format(tg.get_me().username)
        with open(get_sticker(), 'rb')as f:
            # will create a set of mask stickers
            assert user.create_new_sticker_set(name=name, title=title,
                                               png_sticker=f, emojis=emojis[0],
                                               mask_position=mask_position)
        url = 'https://i.imgur.com/BDZfRJg.png'
        assert user.add_sticker_to_set(name=name,
                                       png_sticker=url,
                                       emojis=emojis[1])


def test_profile_photos():
    with bm.use_cassette('test_user__test_profile_photos'):
        photos = user.get_profile_photos(0, 1)
    assert photos.total_count == 1
    for photo in photos:
        assert photo
