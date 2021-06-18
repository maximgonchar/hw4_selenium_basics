import pytest
from selenium import webdriver
import os

DRIVERS = os.path.expanduser("~/Documents/Develop/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera", "safari"], default="chrome")
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    # parser.addoption("--impl_wait", action="store", default="3", required=False)
    parser.addoption("--headless", action="store_true", help="Run headless", default=False)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--url")
    # wait = request.config.getoption("--impl_wait")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(options=options, executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Driver not supported: {}".format(browser))

    # driver.implicitly_wait(wait)
    request.addfinalizer(driver.quit)
    driver.get(url)

    if maximized:
        driver.maximize_window()

    return driver


@pytest.fixture()
def on_login_page(browser):
    browser.get('https://demo.opencart.com/index.php?route=account/login')
    return browser


@pytest.fixture()
def admin(browser):
    browser.get('https://demo.opencart.com/admin/')
    return browser


@pytest.fixture()
def catalog_page(browser):
    browser.get('https://demo.opencart.com/index.php?route=product/category&path=20')
    return browser


@pytest.fixture()
def macbook(browser):
    browser.get('https://demo.opencart.com/index.php?route=product/product&path=18&product_id=45')
    return browser
