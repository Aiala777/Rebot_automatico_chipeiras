from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import keyboard
from pushbullet import Pushbullet
import os
import time 
from datetime import date, timedelta, datetime
from enviooutlook import *

# def notifySucesso():
#     #conta1 (Vilela)
#     API_KEY = "o.jVotDSlnZ9fALZQ2cWHt4EidyhbmgsNh"
#     filename = 'C:/Users/Administrator/Desktop/Chipeiras/sucess.txt'
#     with open(filename, mode='r') as f:
#         text = f.read()
#     pb = Pushbullet(API_KEY)
#     push = pb.push_note("CHIPEIRAS", text)

#     #conta2 (Arthur)
#     API_KEY = "o.DP5nFcAOsB5meJWlT6tIFLerirSd042M"
#     filename = 'C:/Users/Administrator/Desktop/Chipeiras/sucess.txt'
#     with open(filename, mode='r') as f:
#         text = f.read()
#     pb = Pushbullet(API_KEY)
#     push = pb.push_note("CHIPEIRAS", text)

#     #conta3 (eficazpush@gmail.com)
#     API_KEY = "o.KMQwI0p7OhFuvtc9jh12ZxpU1hmExL0f"
#     filename = 'C:/Users/Administrator/Desktop/Chipeiras/sucess.txt'
#     with open(filename, mode='r') as f:
#         text = f.read()
#     pb = Pushbullet(API_KEY)
#     push = pb.push_note("CHIPEIRAS", text)



def reboot():
    # Configurações do navegador
    options = Options() 
    # Eliminar erro Bluetooth adapter
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    #Definindo o chrome para abrir em um perfil diferente
    options.add_argument('--profile-directory=Profile 4')
    options.add_argument("user-data-dir=C:\\Users\\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\")
    global navegador
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        #SETANDO O SITE (CHIPEIRA 85)
        navegador.get('http://192.168.0.85/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[16]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)
    except NoSuchElementException: 
            print('ERROR')
            time.sleep(10)

    try:
        #SETANDO O SITE (CHIPEIRA 60)
        navegador.get('http://192.168.0.60/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[14]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)
    except NoSuchElementException: 
            print('ERROR')  
            time.sleep(10)      

    try:
        #SETANDO O SITE (CHIPEIRA 56)
        navegador.get('http://192.168.0.56/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[14]/td/div').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)      
    except NoSuchElementException: 
            print('ERROR')
            time.sleep(10)
    try:
        #SETANDO O SITE (CHIPEIRA 11)
        navegador.get('http://192.168.0.11/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[14]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)
    except NoSuchElementException: 
            print('ERROR')
            time.sleep(10)

    try:
        #SETANDO O SITE (CHIPEIRA 20)
        navegador.get('http://192.168.0.20/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[16]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)
    except NoSuchElementException: 
            print('ERROR') 
            time.sleep(10)               

    try:
        #SETANDO O SITE (CHIPEIRA 64)
        navegador.get('http://192.168.0.64/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[14]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)
    except NoSuchElementException: 
            print('ERROR')
            time.sleep(10)

    try:
        #SETANDO O SITE (CHIPEIRA 32)
        navegador.get('http://192.168.0.32/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[16]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)
    except NoSuchElementException: 
            print('ERROR')
            time.sleep(10)
    try:
        #SETANDO O SITE (CHIPEIRA 13)
        navegador.get('http://192.168.0.13/default/en_US/status.html') #SITE CHIPEIRA
        time.sleep(10)
        keyboard.press_and_release('enter')
        time.sleep(5)
        navegador.find_element(By.XPATH, '//*[@id="table6"]/tbody/tr[5]/td[2]/a/div').click() #XPATH TOOL
        time.sleep(5)
        navegador.find_element(By.XPATH,'//*[@id="mainframe"]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/table/tbody/tr[14]/td/div/input').click() #XPATH REBOOT 
        time.sleep(5)
        keyboard.press_and_release('enter')
        time.sleep(10)

        print('-----CHIPEIRAS REBOOTADAS-----')
        envio()
    except NoSuchElementException: 
            print('ERROR')
            emailInsusesso()
            time.sleep(10)


today = datetime.now().strftime("%d/%m/%Y, %H:%M:%S - ")
try:
  reboot()
  
  os.chdir("C:/Users/Administrator/Desktop/Chipeiras")
  f = open("logpadrao.txt", "a")
  f.write(str(today))
  f.write('Script executado')
  f.close()
except Exception as Argument:
  f = open("log_erro.txt", "a")
  f.write(str(today))
  f.write(str(Argument))
  f.close()


# from selenium.webdriver.common.keys import Keys

# driver.find_element_by_name("Value").send_keys(Keys.ENTER)
