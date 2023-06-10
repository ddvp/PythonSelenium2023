import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"

class TestLaboratorioQAMinds:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 120)
        self.driver.maximize_window()
        self.driver.get(URL)
    def test_login(self):
        #valores esperados
        exp_success_msg = " Warning: No match for E-Mail Address and/or Password."

        usr_name = self.driver.find_element(By.ID, "input-email")
        usr_name.send_keys("test@test.com")
        time.sleep(2)
        assert usr_name.is_enabled()
        pswd_usr = self.driver.find_element(By.ID, "input-password")
        pswd_usr.send_keys("test")
        time.sleep(2)
        btn_login = self.driver.find_element(By.XPATH, '//input[@value="Login"]')
        btn_login.click()
        time.sleep(2)

        warn_msg = self.driver.find_element(By.CLASS_NAME, "alert alert-danger alert-dismissible")
        assert warn_msg.is_enabled(), "Warning message should be displayed"
        print(warn_msg.text)
        assert exp_success_msg in warn_msg.text, f"Warning message should contain {exp_success_msg}"
        time.sleep(5)
    def teardown_method(self):
        self.driver.quit()