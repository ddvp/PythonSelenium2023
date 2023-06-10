import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(5)
        self.wait_driver = WebDriverWait(self.driver, 120)
        self.driver.maximize_window()
        self.driver.get(URL)
    def test_laptopSection(self):
        #valores esperados
        exp_msg = "There are no products to list in this category."

        nav_lap = self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/a')
        nav_lap.click()
        time.sleep(2)
        nav_wind = self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a')
        nav_wind.click()
        time.sleep(2)

        prod_msg = self.driver.find_element(By.CLASS_NAME, "col-sm-9")
        assert prod_msg.is_enabled(), "Product message should be displayed"
        print(prod_msg.text)
        assert exp_msg in prod_msg.text, f"Product message should contain {exp_msg}"
        time.sleep(2)

        btn_continue = self.driver.find_element(By.CLASS_NAME, 'btn btn-primary')
        btn_continue.click()

    def teardown_method(self):
        self.driver.quit()