import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.adduser_page import AddUser
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()



def test_adduser(driver):
    adduser = AddUser(driver)
    adduser.open_adduserpage("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
    adduser.input_userrole()
    time.sleep(2)
    adduser.input_employeenname("Ravi M B")
    time.sleep(2)
    adduser.input_status()
    time.sleep(2)
    adduser.input_username("vvvvvv")
    time.sleep(2)
    adduser.input_password("lisa2023#")
    time.sleep(2)
    adduser.confirm_pass("lisa2023#")
    time.sleep(2)
    adduser.click_savebutton()
    time.sleep(10)

    assert "viewsystemusers" in driver.current_url.lower(), "Add unsuccessful"



# if __name__ == "__main__":
#     pytest.main([__file__])
