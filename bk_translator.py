from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
import time


# inicializuje prekladac
def prekladac_cz(from_lang, to_lang):
    # inicializace prohlizece
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(chrome_options=options)
    # driver.minimize_window()
    driver.get('https://www.prekladac.cz/')

    # nastaveni prekladaneho jazyka
    language_from = driver.find_element_by_id('lang_from')
    language_from.send_keys(from_lang)

    # nastaveni ciloveho jazyka
    language_to = driver.find_element_by_id('lang_to')
    language_to.send_keys(to_lang)

    return driver


# prelozi blok vet
def preloz_text(t_str, driver, time_delay):

    # odstraneni mezer ve vete ???
    t_str.join(t_str.split())

    # vlozeni textu do prekladace
    driver.find_element_by_id('from_text').clear()
    text_area = driver.find_element_by_id('from_text')
    text_area.send_keys(t_str)

    # zahajeni prekladu
    translate_button: WebElement = driver.find_element_by_css_selector('.btn-sm')
    translate_button.click()

    # cekani na server
    time.sleep(time_delay)

    # ziskani prelozeneho textu
    element = driver.find_element_by_id("result")
    content = element.text

    return content
