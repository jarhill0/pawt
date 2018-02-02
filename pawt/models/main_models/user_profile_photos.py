from ..base import PAWTBase


class UserProfilePhotos(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)
        self.total_count = data['total_count']
        self.photos = [
            [tg.photo_size(data=ps) for ps in photo]
            for photo in data['photos']
        ]

    def __str__(self):
        return str(self.photos)

    def __iter__(self):
        return iter(self.photos)
