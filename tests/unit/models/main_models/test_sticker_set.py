from pawt.exceptions import BadArgument
from pawt.models import StickerSet

DATA = dict(name="sticker_set", title="My sticker set")  # missing attrs
NAME = "sticker_set"


def test_num_args():
    try:
        StickerSet(None)
    except BadArgument:
        pass
    else:
        assert False

    try:
        StickerSet(None, name=NAME, data=DATA)
    except BadArgument:
        pass
    else:
        assert False

    StickerSet(None, name=NAME)
