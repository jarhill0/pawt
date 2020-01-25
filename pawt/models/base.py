class PAWTBase:
    def __init__(self, tg):
        self._tg = tg


class PAWTLazy(PAWTBase):
    def __init__(self, tg):
        super().__init__(tg)
        self._fetched = False

    def __getattr__(self, item):
        if not self._fetched:
            self._load()
            self._fetched = True
            return getattr(self, item)
        raise AttributeError(
            "{} does not have attribute {!r}".format(self.__class__.__name__, item)
        )

    def _load(self):
        raise NotImplementedError("Should be implemented by subclass.")


class Sendable(PAWTBase):
    def send(self, chat, *args, **kwargs):
        raise NotImplementedError("Should be implemented by subclass")

    def _chat_parser(self, chat):
        if isinstance(chat, (str, int)):
            chat = self._tg.chat(chat)
        return chat
