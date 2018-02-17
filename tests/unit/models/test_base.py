from pawt.models.base import PAWTBase

TG = None


def test_base_creation():
    base = PAWTBase(TG)
    assert hasattr(base, '_tg')
