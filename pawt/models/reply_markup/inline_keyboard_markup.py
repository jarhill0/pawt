from ...exceptions import BadArgument


def inline_keyboard_markup(inline_keyboard):
    return dict(inline_keyboard=inline_keyboard)


def inline_keyboard_button(text, *, url=None, callback_data=None,
                           switch_inline_query=None,
                           switch_inline_query_current_chat=None,
                           callback_game=None, pay=None):
    if (url, callback_data, switch_inline_query,
        switch_inline_query_current_chat, callback_game,
        pay).count(None) != 5:
        raise BadArgument('Exactly one parameter besides text should be '
                          'provided.')
    out = dict(text=text)
    if url:
        out['url'] = url
    if callback_data:
        out['callback_data'] = callback_data
    if switch_inline_query:
        out['switch_inline_query'] = switch_inline_query
    if switch_inline_query_current_chat:
        shorter_var_name = switch_inline_query_current_chat
        out['switch_inline_query_current_chat'] = shorter_var_name
    if callback_game:
        out['callback_game'] = callback_game
    if pay is not None:  # can be False
        out['pay'] = pay

    return out


def callback_game():
    """API docs say this has yet to be implemented."""
    return dict()


class InlineKeyboardMarkupBuilder():
    def __init__(self):
        self.keyboard = [[]]

    def add_button(self, *args, **kwargs):
        self.keyboard[-1].append(inline_keyboard_button(*args, **kwargs))

    def new_row(self):
        self.keyboard.append([])

    def build(self):
        return inline_keyboard_markup(self.keyboard)
