from selenium.webdriver.common.by import By
import time
from factory.webdriver_factory import get_driver


URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
    def test_search(self):

        #valores esperados
        exp_cost = "$122.00"
        exp_wish_list_label = "1"
        exp_success_msg = "Success: You have added"


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

        #verificar mensaje de que se agrego exitosamente
        success_msg = self.driver.find_element(By.CLASS_NAME, "alert-success")
        assert success_msg.is_enabled(), "Success message should be displayed"
        print(success_msg.text)
        assert exp_success_msg in success_msg.text, f"Success message should contain {exp_success_msg}"




    def teardown_method(self):
        self.driver.quit()