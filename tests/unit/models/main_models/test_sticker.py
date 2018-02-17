from pawt import Telegram
from pawt.exceptions import BadArgument
from pawt.models import Sticker

TG = Telegram('')


def test_attrs():
    sticker = Sticker(TG, data=dict(width=512, height=510, file_id=12345))
    assert sticker.width == 512
    assert sticker.height == 510


def test_mask_pos():
    mask_position = dict(point='forehead', x_shift=-1.5,
                         y_shift=2 / 3, scale=2.0)
    data = dict(width=512, height=510, file_id=12345,
                mask_position=mask_position)
    sticker = Sticker(TG, data=data)

    assert sticker.mask_position.to_dict() == mask_position

    mask_position['point'] = 'invalid location'
    try:
        Sticker(TG, data=data)
    except BadArgument:
        pass
    else:
        assert False


def test_repr():
    sticker = Sticker(TG, data=dict(width=512, height=510, file_id=12345))
    assert repr(sticker) == '<Sticker 12345>'
