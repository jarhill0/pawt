from .inline_query_result import InlineQueryResult


class InlineQueryResultAudio(InlineQueryResult):
    """Represents a link to an mp3 audio file. By default, this audio file
    will be sent by the user. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the audio."""

    def __init__(
        self,
        id_,
        audio_url,
        title,
        caption=None,
        performer=None,
        audio_duration=None,
        reply_markup=None,
        input_message_content=None,
    ):
        super().__init__("audio", id_, reply_markup)

        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.performer = performer
        self.audio_duration = audio_duration
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
