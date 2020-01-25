from pawt.models.base import PAWTBase, PAWTLazy, Sendable

TG = None


def test_base_creation():
    base = PAWTBase(TG)
    assert hasattr(base, "_tg")


def test_lazy_not_implemented():
    lazy = PAWTLazy(None)
    try:
        lazy.attribute
        assert False, "should raise NotImplementedError"
    except NotImplementedError:
        pass


def test_sendable_not_implemented():
    send = Sendable(None)
    try:
        send.send(None)
        assert False, "should raise NotImplementedError"
    except NotImplementedError:
        pass
