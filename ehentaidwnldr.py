from email.mime import image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
num=1
wget="WGETLOCATION --no-check-certificate "
url=input("Introduce la url: ")
folder = input("Introduce el nombre de la carpeta: ")
os.system("mkdir "+folder)
os.system("cd "+folder)
os.chdir(folder)
folder = folder + " "
wd = webdriver.Edge(executable_path="WEBDRIVERLOCATION")
wd.get(url)
times=wd.find_element(By.XPATH, ('/html/body/div[1]/div[1]/div[1]/div/span[2]')).text
times = int(times)
while (num<=times):
    photo=wd.find_element(By.XPATH, ('/html/body/div[1]/div[2]/a/img')).get_attribute('src')
    os.system(wget + photo)
    os.system("TIMEOUT 2")
    element=wd.find_element(By.XPATH, ('//*[@id="i3"]'))
    element.click()
    num+=1
os.system("rename *.2 *.jpg")
os.system("rename *.1 *.jpg")
os.system("rename *.0 *.jpg")
os.system("rename *.3 *.jpg")
os.system("del *.2")
os.system("del *.1")
os.system("del *.0")
os.system("del *.3")
wd.quit()