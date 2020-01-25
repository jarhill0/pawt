from ..message_specials.base import FileWrapper


class PhotoSize(FileWrapper):
    def __init__(self, tg, data):
        super().__init__(tg, data)

        self.width = data["width"]
        self.height = data["height"]

    def to_dict(self):
        d = dict(file_id=self.file.id, width=self.width, height=self.height)
        if self.file_size:
            d["file_size"] = self.file_size
        return d

    def __eq__(self, other):
        if not (
            hasattr(other, "width")
            and hasattr(other, "height")
            and hasattr(other, "file")
        ):
            return False

        return (
            self.file == other.file
            and self.width == other.width
            and self.height == other.height
        )

    def __gt__(self, other):
        if not (hasattr(other, "width") and hasattr(other, "height")):
            raise TypeError("Cannot compare PhotoSize with type {}".format(type(other)))

        return self.height * self.width > other.height * other.width
