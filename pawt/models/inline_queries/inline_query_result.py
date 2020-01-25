class InlineQueryResult:
    def __init__(self, type_, id_, reply_markup=None):
        self.type = type_
        self.id = id_
        self.reply_markup = reply_markup  # maybe need to call json.dumps()

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.id)

    def to_dict(self):
        out = dict()
        for key, val in self.__dict__.items():
            if not key.startswith("_") and val is not None:
                out[key] = val
        return out
