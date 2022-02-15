import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


driver = None


@pytest.fixture
def setup():
    global driver
    print("start browser")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")


def test_1(setup):
    driver.get("https://www.facebook.com/")
    print("test 1 executed")


def test_2(setup):
    driver.get("https://www.facebook.com/")
    print("test 2 executed")


def test_3(setup):
    driver.get("https://www.facebook.com/")
    print("test 3 executed")

