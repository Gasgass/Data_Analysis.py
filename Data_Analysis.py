import pandas as pd
import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"

#input_2 = input("ingrese su farmaco: ")



#WebScraping Vademecum



#Defino las funciones
def keys_2():
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[2]/td[3]/div/input"))) \
        .send_keys(i)

def click(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .click()

def scrap(XPATH):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, XPATH)))

def remove_punc(string):
    punt = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in string:
        if ele in punt:
            string = string.replace(ele, "")
    return string

#Esta funcion se encarga de tomar todos los datos de los farmacos y almacenarlos en archivos csv
def scrap_precios():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(10)
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")

    precios = []
    for a in precio:
        precios.append(a.text)
    precios = [ele for ele in precios if ele.strip()]

    farmaco = []
    for n in range(len(precios)):
        data = {"Precio": precios[n].strip("$"),
                }
        farmaco.append(data)
    df_data = pd.DataFrame(farmaco)
    print(df_data)
    df_data.to_csv("a.csv", index=False, header=False, mode="a")

    click(XPATH="/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i")
    #time.sleep(5)



#element = driver.find_element_by_xpath('//a[@name="zk_comp_99-next"]').get_attribute("disabled")
with open("C:\\Users\\segui\\PycharmProjects\\Data_Analysis\\Scrap.csv", "r") as f:


    for i in f:
        print(i)
        driver = webdriver.Chrome(executable_path=r"C:\Users\segui\PycharmProjects\pythonProject4\chromedriver.exe")
        driver.get(website)
        while True:

            try:
            # Accedo al sitio de ANMAT
                keys_2(
                )
                click(
                    XPATH="/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[7]/td[3]/div/div/div[1]/button")
                while True:
                    scrap_precios()
                    element = driver.find_element_by_xpath('//a[@name="zk_comp_99-next"]').get_attribute("disabled")
                    if element == None:
                        continue
                    else:
                        scrap_precios()
                        time.sleep(10)
                        driver.quit()
                        break
                        # quit()
            except:
                break

