from .animation import Animation
from .message_entity import MessageEntity
from ..base import PAWTBase


class Game(PAWTBase):
    def __init__(self, tg, data):
        super().__init__(tg)

        self.title = data['title']
        self.description = data['description']
        self.photo = [tg.photo_size(data=ps) for ps in data['photo']]
        self.text = data.get('text')

        if data.get('text_entities'):
            self.text_entities = MessageEntity.build(tg, data['text_entities'],
                                                     self.text)
        else:
            self.text_entities = None
        if data.get('animation'):
            self.animation = Animation(tg, data=data['animation'])
        else:
            self.animation = False

    def __repr__(self):
        return '<Game {!r}>'.format(self.title)

    def __str__(self):
        return self.title
