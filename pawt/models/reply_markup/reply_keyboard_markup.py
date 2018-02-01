def reply_keyboard_markup(keyboard, resize_keyboard=None,
                          one_time_keyboard=None, selective=None):
    out = dict(keyboard=keyboard)
    if resize_keyboard is not None:  # could be False
        out['resize_keyboard'] = resize_keyboard
    if one_time_keyboard is not None:  # could be False
        out['one_time_keyboard'] = one_time_keyboard
    if selective is not None:  # could be False
        out['selective'] = selective
    return out


def keyboard_button(text, request_contact=None, request_location=None):
    out = dict(text=text)
    if request_contact is not None:  # could be False
        out['request_contact'] = request_contact
    if request_location is not None:  # could be False
        out['request_contact'] = request_contact
    return out


class ReplyKeyboardMarkupBuilder:
    def __init__(self):
        self.keyboard = [[]]
        self._row_pointer = 0

    def add_button(self, *args, **kwargs):
        self.keyboard[self._row_pointer].append(
            keyboard_button(*args, **kwargs))

    def new_row(self):
        self.keyboard.append([])
        self._row_pointer += 1

    def build(self, *args, **kwargs):
        return reply_keyboard_markup(self.keyboard, *args, **kwargs)
