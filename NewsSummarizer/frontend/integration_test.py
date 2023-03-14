import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_integration(driver):
    driver.get('http://example.com')
    # Perform integration test here
    # Example:
    assert "Example Domain" in driver.title