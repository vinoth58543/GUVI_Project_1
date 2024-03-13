from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from Test_Data import data
from Test_Locator import locator
from selenium.common.exceptions import NoSuchElementException
class Test_vinoth:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
    #script for title of the webpage
    def test_title(self, booting_function):
        try:
           self.driver.get(data.Data().url)
           assert self.driver.current_url == data.Data().url
           print("SUCESS : web Title captured correct")
        except:
            print('error occured')
    #script for login page
    def test_login(self, booting_function):
        try:
           self.driver.get(data.Data().url)
           #implicit wait
           self.driver.implicitly_wait(10)
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.NAME, value=locator.Locators().password_input_box).send_keys(data.Data().password)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().submit_button).click()
           print("SUCESS : Logged with username {a} and password{b}".format(a=data.Data().username, b=data.Data().password))
        except:
            print('error occured')
 
    #script for invalid login
    def test_invalid_login(self, booting_function):
        try:
           self.driver.get(data.Data().url)
        #implicit wait has been used
           self.driver.implicitly_wait(10)
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.NAME, value=locator.Locators().password_input_box).send_keys(data.Data().invalid_password)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().submit_button).click()
           print("SUCESS : Logged with username {a} and password{b}".format(a=data.Data().username, b=data.Data().password))

        except:
            print('error occured')

    #script for add employee
    def test_add_employee(self,booting_function):
        try:
           self.driver.get(data.Data().url)
           #implicit wait use
           self.driver.implicitly_wait(10)
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.NAME, value=locator.Locators().password_input_box).send_keys(data.Data().password)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().submit_button).click()
           self.driver.find_element(by=By.XPATH, value=locator.Locators().PIM).click()
           self.driver.find_element(by=By.XPATH,value=locator.Locators().Add_Employee).click()
           self.driver.find_element(by=By.NAME, value=locator.Locators().first_name).send_keys(data.Data().first_Name)
           self.driver.find_element(by=By.NAME, value=locator.Locators().last_name).send_keys(data.Data().last_Name)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().Employee_Id).send_keys(data.Data().Employee_Id)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().save_button).click()
           print("SUCESS : Logged with username {a} and password{b}".format(a=data.Data().username, b=data.Data().password))
        except:
            print('error occured')
    
    #script for delete employee
    def test_delete_employee(self,booting_function):
        try:
           self.driver.get(data.Data().url)
           #implicit wait has been used
           self.driver.implicitly_wait(10)
           self.driver.find_element(by=By.NAME, value=locator.Locators().username_input_box).send_keys(data.Data().username)
           self.driver.find_element(by=By.NAME, value=locator.Locators().password_input_box).send_keys(data.Data().password)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().submit_button).click()
           self.driver.find_element(by=By.XPATH, value=locator.Locators().PIM).click()
           self.driver.find_element(by=By.XPATH,value=locator.Locators().Employees_list).click()
           self.driver.find_element(by=By.XPATH, value=locator.Locators().Employee_ID).send_keys(data.Data().Employee_Id)
           self.driver.find_element(by=By.XPATH, value=locator.Locators().search_button).click()
           self.driver.find_element(by=By.XPATH, value=locator.Locators().Trash).click()
           self.driver.find_element(by=By.XPATH, value=locator.Locators().delete).click()
           print("SUCESS : Logged with username {a} and password{b}".format(a=data.Data().username, b=data.Data().password))
        except:
            print('error occured')


