from nose.tools import assert_equals
from server import read_time


def test_read_time():
    print(f"is test_read_time <=== ")
    assert len(read_time()) > 0
