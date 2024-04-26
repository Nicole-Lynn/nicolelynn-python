
from numb3rs import validate

def main():
    test_validate_correct()
    test_validate_wrong()
    test_validate_non_number()

def test_validate_correct():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_validate_wrong():
    assert validate("1.2.3.4") == True
    assert validate("1.555.555.555") == False

def test_validate_non_number():
    assert validate("cat") == False
    assert validate("one.two.three.four") == False



if __name__=="__main__":
    main()
