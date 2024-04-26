from um import count


def test_count_valid():
    assert count("um") == 1
    assert count("..um..") == 1
    assert count("um, hello, um, world") == 2
    assert count("UM um Um uM") == 4



def test_count_invalid():
    assert count("yum") == 0
    assert count("yummy") == 0

