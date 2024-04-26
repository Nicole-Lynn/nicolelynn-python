from bank import value

def test_zero():
    assert value("hello") == 0
    assert value("Hello, Scarlett") == 0

def test_twenty():
    assert value("How are you doing?") == 20

def test_hundred():
    assert value("What's good?") == 100

def test_space():
    assert value(  "Hello") == 0
    assert value("How are you?    ") == 20
    assert value("What can I     help you with?") == 100
