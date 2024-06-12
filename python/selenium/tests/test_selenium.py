from selenium import webdriver
import pytest

@pytest.mark.selenium
def test_selenium():
    """
    Summary:
        Selenium first test
    Run:
        pytest -m selenium
    """
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    assert driver.title == "Selenium"
    driver.quit()