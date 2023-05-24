import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_search_tablets(self):
        # Varoles esperados
        exp_title = "Samsung Galaxy Tab 10.1"
        exp_cost = "$241.99"
        exp_wish_list_label = "1"
        exp_success_msg = "Success: You have added"

        # Seleccionar nav de tablets:
        tablets_menu = self.driver.find_element(By.XPATH, "//a[contains(@href, 'category&path=57')]")
        assert tablets_menu.is_displayed() and tablets_menu.is_enabled(), "Menu de tabletas tiene que estar visible"
        tablets_menu.click()
        time.sleep(2)

        # Verificar el titulo:
        title = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href, 'product_id=49')]")
        assert title.is_displayed(), "Title should be displayed"
        assert title.text == exp_title, f"Title should be {exp_title}"

        # Dar click al titulo
        title.click()
        time.sleep(5)

        # Verificar costo
        cost = self.driver.find_element(By.XPATH, "//div[@id='content']//li//h2")
        assert cost.is_displayed(), "Cost should be displayed"
        assert cost.text == exp_cost, f"Cost should be {exp_cost}"

        # Agregarlo al wish list
        wish_list = self.driver.find_element(By.XPATH, '//div[@id="content"]//button[./i[@class="fa fa-heart"]]')
        assert wish_list.is_displayed() and wish_list.is_enabled(), "Wish list should be displayed"
        wish_list.click()
        time.sleep(2)

        # Validar wish list update
        wish_list_label = self.driver.find_element(By.XPATH, '//a[@id="wishlist-total"]/span')
        assert wish_list_label.is_displayed(), "Wish list label should be displayed"
        assert exp_wish_list_label in wish_list_label.text, f"Wish list label should contains {exp_wish_list_label}"

        # Agregarlo al carro de compra
        add_to_cart = self.driver.find_element(By.ID, "button-cart")
        assert add_to_cart.is_displayed() and add_to_cart.is_enabled(), "Add to cart should be displayed"
        add_to_cart.click()
        time.sleep(2)

        success_msg = self.driver.find_element(By.CLASS_NAME, "alert-success")
        assert success_msg.is_enabled(), "Success message should be displayed"
        print(success_msg.text)
        assert exp_success_msg in success_msg.text, f"Success message should contain {exp_success_msg}"

    def teardown_method(self):
        self.driver.quit()