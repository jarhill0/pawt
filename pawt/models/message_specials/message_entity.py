from ..base import PAWTBase


class MessageEntity(PAWTBase):
    @staticmethod
    def build(tg, data, text):
        t = data['type']
        return type_map[t](tg, data, text)

    @property
    def content(self):
        return self._text[self.offset:self.offset + self.length]

    def __init__(self, tg, data, text):
        super().__init__(tg)

        self._text = text

        self.offset = data['offset']
        self.length = data['length']

    def __repr__(self):
        return '<{class_name}: {content}>'.format(
            class_name=self.__class__.__name__, content=self.content
        )

    def __str__(self):
        return self.content

    def __eq__(self, other):
        return (str(self) == str(other) and hasattr(other, 'length') and
                self.length == other.length and hasattr(other, 'offset') and
                self.offset == other.offset and type(self) == type(other))


class Mention(MessageEntity):
    pass


class Hashtag(MessageEntity):
    pass


class Cashtag(MessageEntity):
    pass


class BotCommand(MessageEntity):
    @property
    def command(self):
        return str(self).split('@')[0]  # strips any @ tag at the end


class Url(MessageEntity):
    pass


class Email(MessageEntity):
    pass


class PhoneNumber(MessageEntity):
    pass


class Bold(MessageEntity):
    pass


class Italic(MessageEntity):
    pass


class Code(MessageEntity):
    pass


class Pre(MessageEntity):
    pass


class TextLink(MessageEntity):
    def __init__(self, tg, data, text):
        super().__init__(tg, data, text)
        self.url = data['url']


class TextMention(MessageEntity):
    def __init__(self, tg, data, text):
        super().__init__(tg, data, text)
        self.user = tg.user(data=data['user'])


type_map = {'mention': Mention,
            'hashtag': Hashtag,
            'cashtag': Cashtag,
            'bot_command': BotCommand,
            'url': Url,
            'email': Email,
            'phone_number': PhoneNumber,
            'bold': Bold,
            'italic': Italic,
            'code': Code,
            'pre': Pre,
            'text_link': TextLink,
            'text_mention': TextMention}
