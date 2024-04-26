from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    with pytest.raises(ValueError):
        jar = Jar(-1)
        jar = Jar(14)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(4)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    jar.withdraw(5)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(4)
