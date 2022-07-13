import pandas as pd
import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


website = "https://servicios.pami.org.ar/vademecum/views/consultaPublica/listado.zul"
driver = webdriver.Chrome(executable_path=r"C:\Users\segui\PycharmProjects\pythonProject4\chromedriver.exe")

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

#Esta funcion se encarga de tomar todos los datos de los farmacos y almacenarlos en archivos csv
def scrap_precios():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(10)
    precio = driver.find_elements_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr/td[7]/span")

    precios = []
    for a in precio:
        precios.append(a.text.strip("$"))
    precios = [ele for ele in precios if ele.strip()]
    df_data = pd.DataFrame(precios)
    print(df_data)
    df_data.to_csv(f"{i}.csv", index=False, header=False, mode="a")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    click(XPATH="/html/body/div/div/div/div/div[2]/div/div/div[3]/ul/li[4]/a/i")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

with open("C:\\Users\\segui\\PycharmProjects\\Data_Analysis\\Scrap.csv", "r") as f:
        a=csv.reader(f)
        d=[]

        for i in a:
            print(i)

            driver.get(website)  # Este driver tiene que ir dentro del loop
            keys_2()
            click(
                XPATH="/html/body/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/table/tbody[1]/tr[7]/td[3]/div/div/div[1]/button")
            print("d")
            while True:

                try:
                    scrap_precios()


                    try:
                        print("a")
                        element = driver.find_element_by_xpath('//a[@name="zk_comp_99-next"]').get_attribute("disabled")

                        if element == None:
                            print("c")
                            pass

                        else:
                            print("b")
                            scrap_precios()
                            #time.sleep(10)
                            #driver.quit()
                            break
                    except:
                        quit("Terminó")
                except:
                    print("ñ")
                    break






