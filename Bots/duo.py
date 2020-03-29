from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import translations as tr
import sys
import selenium


# setup
fp = webdriver.FirefoxProfile()
fp.set_preference("webdriver.load.strategy", "unstable")
driver = webdriver.Firefox(firefox_profile=fp)


def main(argv):
    login('username', 'pass')
    nav_story()


def login(username, password):
    try:
        driver.maximize_window()
        driver.get("https://duolingo.com/log-in")
        driver.find_element_by_css_selector("[data-test='email-input']").send_keys(username)
        driver.find_element_by_css_selector("[data-test='password-input']").send_keys(password, Keys.RETURN)
    except selenium.common.exceptions.NoSuchElementException as exception:
        print(exception)

def nav_story():
    try:
        driver.find_element_by_css_selector("[data-test='stories-nav']").click()
    except selenium.common.exceptions.NoSuchElementException as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)

