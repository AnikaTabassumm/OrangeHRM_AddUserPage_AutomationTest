import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import adduser_test
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("username, password",[
    ("Admin","admin123")
])

def test_loginpage(driver,username, password):
    login_page = LoginPage(driver)
    login_page.open_loginpage("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    login_page.input_username(username)
    time.sleep(1)
    login_page.input_password(password)
    time.sleep(1)
    login_page.click_loginbutton()
    time.sleep(5)

    adduser_test.test_adduser(driver)

    print("Done")


if __name__ == "__main__":
    pytest.main([__file__])
