from pawt.models import StickerSet
from ... import bm, tg, user

user = tg.user(user)


def get_sticker():
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, 'gradient2.png')


def test_sticker_set():
    with bm.use_cassette('test_sticker_set__test_sticker_set'):
        name = 'pawt_test_stickers_set_by_' + tg.get_me().username
        with open(get_sticker(), 'rb') as f:
            user.create_new_sticker_set(name, 'test_sticker_set.py', f, '🙃')

        sticker_set = tg.sticker_set(name)

        sticker_set.add(user.id, 'https://i.imgur.com/BDZfRJg.png', '🍊')

        assert str(sticker_set) == 'test_sticker_set.py'
    assert repr(sticker_set).startswith(
        '<StickerSet pawt_test_stickers_set_by_')


def test_objectify_from_data():
    with bm.use_cassette('test_sticker_set__test_objectify_from_data'):
        data = tg.get('getStickerSet', params={'name': 'LazyPanda'})
        sticker_set = StickerSet(tg, data=data)
    assert sticker_set.name == 'LazyPanda'
    assert sticker_set.title == 'Lazy Panda'
    assert len(sticker_set.stickers) > 5
