class InputMessageContent:
    def to_dict(self):
        out = dict()
        for key, val in self.__dict__:
            if not key.startswith('_') and val:
                out[key] = val
        return out
