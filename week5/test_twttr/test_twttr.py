from twttr import shorten

def test_lower():
    assert shorten("hey") == "hy"
    assert shorten("what's your name?") == "wht's yr nm?"

def test_upper():
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("0") == "0"
    assert shorten("1") == "1"

def test_punctuation():
    assert shorten(".,?!") == (".,?!")
