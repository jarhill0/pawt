from pawt.exceptions import BadArgument
from pawt.models import File

ID = 12345
data = dict(file_id=ID)


def test_num_args():
    try:
        file = File(None)
    except BadArgument:
        pass
    else:
        assert False

    try:
        file = File(None, file_id=ID, data=data)
    except BadArgument:
        pass
    else:
        assert False

    file = File(None, file_id=ID)
    file = File(None, data=data)


def test_repr():
    file = File(None, ID)
    assert repr(file) == "<File 12345>"


def test_eq():
    file1 = File(None, 12345)
    file2 = File(None, "12345")
    file3 = File(None, 123456)

    assert file1 == file1
    assert file1 == file2
    assert file1 != file3

    assert file1 == 12345 == file2
    assert file1 == "12345" == file2
