from .base import PAWTBase
from ..exceptions import BadArgument


class MaskPosition(PAWTBase):
    def __init__(self, data):
        super().__init__(tg=None)

        # validate point

        self.point = data['point']
        self.x_shift = data['x_shift']
        self.y_shift = data['y_shift']
        self.scale = data['scale']

        if self.point not in ("forehead", "eyes", "mouth", "chin"):
            raise BadArgument('Point must be one of "forehead", "eyes", '
                              '"mouth", or "chin".')

    def to_dict(self):
        return {'point': self.point,
                'x_shift': self.x_shift,
                'y_shift': self.y_shift,
                'scale': self.scale}
