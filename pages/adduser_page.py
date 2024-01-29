import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddUser():

    def __init__(self, driver):
        self.driver = driver
        self.userrole = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
        self.employee_name = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
        self.status = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
        self.e_username = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
        self.e_password = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
        self.c_password = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
        self.save_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')
        self.cancel_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]')

    def open_adduserpage(self, url):
        self.driver.get(url)


    def input_userrole(self):
        userrole_element = self.driver.find_element(*self.userrole)
        userrole_element.click()
        userrole_element.send_keys(Keys.ARROW_DOWN)
        userrole_element.send_keys(Keys.ENTER)

    def input_employeenname(self, name):
        e_name_element = self.driver.find_element(*self.employee_name)
        e_name_element.send_keys(name)
        time.sleep(2)
        e_name_element.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        e_name_element.send_keys(Keys.ENTER)


    def input_status(self):
        status_element = self.driver.find_element(*self.status)
        status_element.click()
        status_element.send_keys(Keys.ARROW_DOWN)
        status_element.send_keys(Keys.ENTER)

    def input_username(self, uname):
        self.driver.find_element(*self.e_username).send_keys(uname)

    def input_password(self, password):
        self.driver.find_element(*self.e_password).send_keys(password)

    def confirm_pass(self, cpass):
        self.driver.find_element(*self.c_password).send_keys(cpass)

    def click_savebutton(self):
        self.driver.find_element(*self.save_button).click()

