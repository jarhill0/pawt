def reply_keyboard_remove(selective=None):
    out = dict(remove_keyboard=True)
    if selective is not None:  # could be False though
        out['selective'] = selective
    return out
