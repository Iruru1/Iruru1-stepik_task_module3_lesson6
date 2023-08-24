import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

#Добавить обработчик, который считывает из командной строки  браузер
#Добавить обработчик, который считывает из командной строки параметр language
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                    help="Choose language")

#Реализовать логику запуска браузера с указанным языком пользователя. 
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language= request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    if user_language != None:
        if browser_name == "chrome":
            options_ = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            browser = webdriver.Firefox(options=options_firefox)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else: 
        raise pytest.UsageError("--language must be specified")
    yield browser
    browser.quit()
    

