from seasons import get_year_month_day, age_minutes


def test_get_valid_year_month_day():
    assert get_year_month_day("2020-12-17") == (2020, 12, 17)
    assert get_year_month_day("2001-3-14") == (2001, 3, 14)

def test_get_invalid_year_month_day():
    assert get_year_month_day("December 17 2020") == "Invalid date"
    assert get_year_month_day("2020,12,17") == "Invalid date"


def test_age_minutes():
    assert age_minutes(2020, 12, 17) == "One million, seven hundred fifty-six thousand, eight hundred minutes"
    assert age_minutes(23, 12, 17) == "One billion, fifty-two million, seventy-eight thousand, four hundred minutes"

def test_age_minutes_wrong():
    assert age_minutes(12, 20, 20) == "Invalid date"




