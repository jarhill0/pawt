def force_reply(selective=None):
    out = dict(force_reply=True)
    if selective is not None:  # could be false
        out["selective"] = selective
    return out
