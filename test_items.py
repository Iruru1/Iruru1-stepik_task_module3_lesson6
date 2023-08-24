from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. 

class TestMain():
    def test_language(self,browser):
        # проверить, что загрузилась кнопка
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        basket_btn = WebDriverWait(browser, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"button.btn-add-to-basket"))
                )
         #проверка теста - наличие кнопки добавления в корзину
        assert basket_btn
        
        