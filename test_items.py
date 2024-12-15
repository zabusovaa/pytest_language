import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basketbtn_is_displayed(browser):
    browser.get(link)
    time.sleep(30)
    basketbtn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basketbtn.is_displayed() == True, "Отсутствует кнопка добавления в корзину"

