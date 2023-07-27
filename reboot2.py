from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


def reboot():
    # Configurações do navegador
    options = Options() 
    # Eliminar erro Bluetooth adapter
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    navegador = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    # SETANDO O SITE (CHIPEIRA 85)
    navegador.get('http://192.168.0.85/default/en_US/status.html')
    time.sleep(5)
    login_page = navegador.current_window_handle
    navegador.current_window_handle
    navegador.window_handles
    navegador.switch_to.window(login_page)

reboot()