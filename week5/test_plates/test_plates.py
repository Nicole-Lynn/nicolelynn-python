from plates import is_valid

def test_length():
    assert is_valid("HE") == True
    assert is_valid("H") == False
    assert is_valid("HELLOO") == True
    assert is_valid("HELLO, GOODBYE") == False

def test_start_two_letters():
    assert is_valid("PL") == True
    assert is_valid("P2") == False
    assert is_valid("2P") == False
    assert is_valid("22") == False

def test_first_number_nonzero():
    assert is_valid("PL20") == True
    assert is_valid("PL02") == False

def test_numbers_in_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AA22AA") == False

def test_punctuation():
    assert is_valid("PL.20") == False
    assert is_valid("PL?20") == False
