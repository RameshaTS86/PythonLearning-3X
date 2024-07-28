import pytest
import allure
@allure.title("Tc_01: Addition")
@allure.description("Checking Addition")
@pytest.mark.smoke
def test_addition():
    assert 1+1 == 2

@allure.title("Tc_02: Addition")
@allure.description("Checking Addition")
@pytest.mark.smoke
def test_addition2():
    assert 1 - 1 == 0

@allure.title("Tc_03: Addition")
@allure.description("Checking Addition")
@pytest.mark.Regression
def test_addition3():
    assert 1+1 == 2

@allure.title("Tc_04: Addition")
@allure.description("Checking Addition")
@pytest.mark.Skip
def test_addition4():
    assert 1 - 1 == 0