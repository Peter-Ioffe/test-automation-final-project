import allure
import pytest
import sqlite3
import selenium.webdriver
import appium.webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
# from applitools.selenium import Eyes
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data, get_timestamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages

driver = None
action = None
action2 = None
m_action = None
# eyes = Eyes()  # Applitools
# web_driver = "Chrome"
db_connector = None


@pytest.fixture(scope="class")
def init_web_driver(request):
    if get_data("ExecuteApplitools").lower() == "yes":
        globals()["driver"] = get_web_driver()
    else:
        edriver = get_web_driver()
        globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(int(get_data("WaitTime")))
    driver.get(get_data("Url"))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    ManagePages.init_web_pages()
    # if get_data("ExecuteApplitools").lower() == "yes":
    #     eyes.api_key = get_data("ApplitoolsKey")
    yield
    driver.quit()
    # if get_data("ExecuteApplitools").lower() == "yes":
    #     eyes.close()
    #     eyes.abort()


@pytest.fixture(scope="class")
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.implicitly_wait(int(get_data("WaitTime")))
    request.cls.driver = driver
    globals()["action"] = TouchAction(driver)
    request.cls.action = globals()["action"]
    globals()["action2"] = TouchAction(driver)
    request.cls.action2 = globals()["action2"]
    globals()["m_action"] = MultiAction(driver)
    request.cls.m_action = globals()["m_action"]
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


@pytest.fixture(scope="class")
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.implicitly_wait(int(get_data("WaitTime")))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    request.cls.action = globals()["action"]
    ManagePages.init_electron_pages()
    yield
    driver.quit()


@pytest.fixture(scope="class")
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()["driver"]
    driver.implicitly_wait(int(get_data("WaitTime")))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


@pytest.fixture(scope="class")
def init_db_connection(request):
    db_path = get_data("DB_Path")
    db_connector = sqlite3.connect(db_path)
    globals()["db_connector"] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()


def get_web_driver():
    web_driver = get_data("Browser")
    if web_driver.lower() == "chrome":
        driver = get_chrome()
    elif web_driver.lower() == "firefox":
        driver = get_firefox()
    elif web_driver.lower() == "edge":
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong Input, Unrecognized Browser")
    return driver


def get_mobile_driver():
    if get_data("MobileDevice").lower() == "android":
        driver = get_android(get_data("UDID"))
    elif get_data("MobileDevice").lower() == "ios":
        driver = get_ios(get_data("UDID"))
    else:
        driver = None
        raise Exception("Wrong input, unknown mobile OS")
    return driver


def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data("ElectronApp")
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data("ElectronDriver"))
    return driver


def get_chrome():
    srv = Service(ChromeDriverManager().install())          # Selenium 4.x
    chrome_driver = selenium.webdriver.Chrome(service=srv)  # Selenium 4.x
    # chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())  # Selenium 3.x
    return chrome_driver


def get_desktop_driver():
    dc = {}
    dc["app"] = get_data("ApplicationName")
    dc["platformName"] = "Windows"
    dc["deviceName"] = "WindowsPC"
    driver = appium.webdriver.Remote(get_data("WinAppDriverService"), dc)
    return driver


def get_firefox():
    # srv = Service(executable_path=GeckoDriverManager().install())  # Selenium 4.x
    # firefox_driver = selenium.webdriver.Firefox(service=srv)       # Selenium 4.x
    firefox_driver = selenium.webdriver.Chrome(GeckoDriverManager().install())  # Selenium 3.x
    return firefox_driver


def get_edge():
    # srv = Service(EdgeChromiumDriverManager().install())  # Selenium 4.x
    # edge_driver = selenium.webdriver.Edge(service=srv)    # Selenium 4.x
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())  # Selenium 3.x
    return edge_driver


def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data("AppPackage")
    dc['appActivity'] = get_data("AppActivity")
    dc['platformName'] = "android"
    android_driver = appium.webdriver.Remote(get_data("AppiumServer"), dc)
    return android_driver


def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundleId'] = get_data("BundleId")
    dc['platformName'] = "ios"
    ios_driver = appium.webdriver.Remote(get_data("AppiumServer"), dc)
    return ios_driver


# Catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()["driver"] is not None:  # this condition is for API testing
            image = get_data("ScreenshotPath") + "screenshot_" + str(get_timestamp()) + ".png"
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
