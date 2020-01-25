from ..base import PAWTBase


class GameHighScore(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.user = tg.user(data=data["user"])
        self.position = data["position"]
        self.score = data["score"]

    def __repr__(self):
        return "<GameHighScore for {!r}>".format(self.user)

    def __str__(self):
        return "#{}: {} got {} points".format(self.position, str(self.user), self.score)
