import pytest

from catinabox import catmath


@pytest.fixture(params=[
])
def test_cat_to_hooman(age):
   pass

def test__cat_years_to_hooman_years__middle_age__succeeds():
    cat_age = 9
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 45


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    cat_age = 0.1
    hooman_age = catmath.cat_years_to_hooman_years(cat_age)
    assert hooman_age == 0.5


def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = catmath.cat_years_to_hooman_years(0)
    assert hooman_age == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
