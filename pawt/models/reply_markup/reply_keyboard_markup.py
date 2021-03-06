from pawt.exceptions import BadArgument


def reply_keyboard_markup(
    keyboard, *, resize_keyboard=None, one_time_keyboard=None, selective=None
):
    out = dict(keyboard=keyboard)
    if resize_keyboard is not None:  # could be False
        out["resize_keyboard"] = resize_keyboard
    if one_time_keyboard is not None:  # could be False
        out["one_time_keyboard"] = one_time_keyboard
    if selective is not None:  # could be False
        out["selective"] = selective
    return out


def keyboard_button(text, *, request_contact=None, request_location=None):
    out = dict(text=text)
    if request_contact and request_location:
        raise BadArgument(
            "At most one of request_contact and " "request_location may be provided."
        )
    if request_contact:  # will only be True or None
        out["request_contact"] = request_contact
    if request_location:  # will only be True or None
        out["request_location"] = request_location
    return out


class ReplyKeyboardMarkupBuilder:
    def __init__(self):
        self.keyboard = [[]]

    def add_button(self, *args, **kwargs):
        self.keyboard[-1].append(keyboard_button(*args, **kwargs))

    def new_row(self):
        self.keyboard.append([])

    def build(self, *args, **kwargs):
        return reply_keyboard_markup(self.keyboard, *args, **kwargs)
