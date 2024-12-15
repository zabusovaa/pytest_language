import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as opt_chrome
from selenium.webdriver.firefox.options import Options as opt_firefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='None',
                     help="Choose language: '--language=en/ru/es/fr' etc.")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = opt_chrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = opt_firefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()