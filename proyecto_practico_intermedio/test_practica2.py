from selenium.webdriver.common.by import By
import time
from factory.webdriver_factory import get_driver


URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
    def test_search(self):

        #Escribir display en la barra de busqueda

        element = self.driver.find_element(By.XPATH, '//*[@name="search"]')
        element.send_keys("Mac (1)")

        #Abrir producto mac
        mac_img = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[1]/a/img')
        mac_img.click()

        #Agregar producto
        add_bttn = self.driver.find_element(By.ID, 'button-cart')
        add_bttn.click()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()