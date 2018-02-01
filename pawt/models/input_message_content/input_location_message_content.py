from .input_message_content import InputMessageContent


class InputLocationMessageContent(InputMessageContent):
    def __init__(self, latitude, longitude, live_period=None):
        self.latitude = latitude
        self.longitude = longitude
        self.live_period = live_period
