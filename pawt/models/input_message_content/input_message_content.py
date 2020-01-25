class InputMessageContent:
    def to_dict(self):
        out = dict()
        for key, val in self.__dict__.items():
            if not key.startswith("_") and val is not None:
                out[key] = val
        return out
