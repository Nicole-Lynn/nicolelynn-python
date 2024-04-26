import pytest
from working import convert



def test_convert_format():
    assert convert("8:00 AM to 7:00 PM") == "08:00 to 19:00"
    assert convert("8 PM to 7 AM") == "20:00 to 07:00"
    assert convert("12 AM to 7:30 AM") == "00:00 to 07:30"
    assert convert("7:30 PM to 12 PM") == "19:30 to 12:00"


def test_convert_format_error():
     with pytest.raises(ValueError):
        convert("8:00 AM - 7:00 PM")


def test_convert_invalid_time():
    with pytest.raises(ValueError):
        convert("8:60 AM to 13:00 PM")


