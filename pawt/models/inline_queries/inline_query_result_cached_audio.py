from .inline_query_result import InlineQueryResult


class InlineQueryResultCachedAudio(InlineQueryResult):
    """Represents a link to an mp3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user. Alternatively, you
    can use input_message_content to send a message with the specified content
    instead of the audio."""

    def __init__(self, id_, audio_file_id, caption=None,
                 reply_markup=None, input_message_content=None):
        super().__init__('audio', id_, reply_markup)

        self.audio_file_id = audio_file_id
        self.caption = caption
        self.input_message_content = None

        if input_message_content:
            self.input_message_content = input_message_content.to_dict()
