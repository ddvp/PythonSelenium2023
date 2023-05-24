from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver
import time
URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search(self):
        # Escribir display en la barra de busqueda
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")

        # Dar click en buscar
        search_btn = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        assert search_btn.is_displayed() and search_btn.is_enabled(), "El boton de busqueda tiene que estar visible y habilitado"
        search_btn.click()

        # Verificar el mensaje
        msg_opc = self.driver.find_element(By.XPATH, '//*[@id="content"]/p[2]')
        assert msg_opc.is_displayed(), "There is no product that matches the search criteria"

        #Seleccionar la opcion search
        box_btn = self.driver.find_element(By.ID, "description")
        assert box_btn.is_displayed()
        box_btn.click()

        #Click en el boton search
        search_btn = self.driver.find_element(By.ID, "button-search")
        assert search_btn.is_displayed()
        search_btn.click()

        #Verificar los resultados de los productos
        appleCinema_img = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[1]/a/img')
        assert appleCinema_img.is_displayed(), "La imagen de appleCinema tiene que estar en el DOM"

        ipodNano_img = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]/div/div[1]/a/img')
        assert ipodNano_img.is_displayed(), "La imagen deñ ipodNano tiene que estar visible"

        ipodTouch_img = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[3]/div/div[1]/a/img')
        assert ipodTouch_img.is_displayed(), "La imagen de ipodTouch tiene que estar visible"

        macBook_img = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[4]/div/div[1]/a/img')
        assert macBook_img.is_displayed(), "La imagen de macBook tiene que estar visible"
        time.sleep(2)
    def teardown_method(self):
        self.driver.quit()