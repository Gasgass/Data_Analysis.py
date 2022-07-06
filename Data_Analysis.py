import pandas as pd
import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"

input_2 = input("ingrese su farmaco: ")

preciario_depurado = []
#WebScraping Vademecum
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\PycharmProjects\pythonProject4\chromedriver.exe")
driver.get(website)

#Defino las funciones
def keys_2(XPATH):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, XPATH))) \
        .send_keys(input_2)

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
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")
    #Este bucle toma solo los precios de los farmacos, para usarlos en el grafico posterior
    precios = []
    for a in precio:
        precios.append(a.text)
    precios = [ele for ele in precios if ele.strip()]

    farmaco = []
    for i in range(len(precios)):
        data = {"Precio": precios[i].strip("$"),
                }
        farmaco.append(data)
    df_data = pd.DataFrame(farmaco)
    print(df_data)
    df_data.to_csv(f"{input_2}.csv", index=False, header=False, mode="a")

    click(XPATH="/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i")
    time.sleep(15)




#Accedo al sitio de ANMAT
try:
    keys_2(
        XPATH="/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[2]/td[3]/div/input")
    click(
        XPATH="/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[7]/td[3]/div/div/div[1]/button")
except TimeoutException:
    print(f"{input_2} no se encuentra en la base de datos. Reinicie el programa.")
    driver.quit()
    quit()

#Recorro pagina a pagina por cada medicamento
while True:
    scrap_precios()

    element = driver.find_element_by_xpath('//a[@name="zk_comp_99-next"]').get_attribute("disabled")
    if element == None:
        continue
    else:
        scrap_precios()
        time.sleep(30)
        driver.quit()
        quit()


#DataVizualisation
def prueba():
    a = csv.reader(f)
    for row in a:
        try:
            n = row[1]
            n = round(float(n.replace(",", ".")))
            if type == str:
                del row[1]
        except ValueError:
            pass
    promedio_preciario_depurado = sum(preciario_depurado) / len(preciario_depurado)
    preciario_depurado.clear()

#Data Visualization
with open("C:\\Users\\segui\\PycharmProjects\\pythonProject4\\Farmacos\\Enfermedades mentales\\clonazepam.csv", "r") as f:
    try:
        a = csv.reader(f)
        for row in a:
            try:
                n = row[1]
                n = round(float(n.replace(",", ".")))
                if type == str:
                    del row[1]
                preciario_depurado.append(n)
                promedio_preciario_depurado = sum(preciario_depurado) / len(preciario_depurado)
            except:
                pass

    except:
        pass