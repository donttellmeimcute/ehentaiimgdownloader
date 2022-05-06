from email.mime import image
from tkinter.ttk import Progressbar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tqdm
num=1
wget="C:\gnu\wget.exe --no-check-certificate "
url=input("Introduce la url: ")
folder = input("Introduce el nombre de la carpeta: ")
os.system("mkdir "+folder)
os.system("cd "+folder)
os.chdir(folder)
folder = folder + " "
wd = webdriver.Chrome(executable_path="C:/Users/hendr/Desktop/chromedriver_win32/chromedriver.exe")
wd.get(url)
times=wd.find_element(By.XPATH, ('/html/body/div[1]/div[1]/div[1]/div/span[2]')).text

times = int(times)
while (num<=times):
    try:
        currurl= wd.current_url
        photo=wd.find_element(By.XPATH, ('/html/body/div[1]/div[2]/a/img')).get_attribute('src')
        actualnumber=wd.find_element(By.XPATH,('//*[@id="i2"]/div[1]/div/span[1]')).text
        actualnumber=int(actualnumber)
        os.system(wget + photo)
        print(photo)
        element=wd.find_element(By.XPATH, ('//*[@id="i3"]'))
        element.click()
        progress=actualnumber/times
        progress=progress*100
        print("progress: ",progress,"%")
        num+=1
    except:
        num+=1
        pass
os.system("rename *.2 *.jpg")
os.system("rename *.1 *.jpg")
os.system("rename *.0 *.jpg")
os.system("rename *.3 *.jpg")
os.system("del *.2")
os.system("del *.1")
os.system("del *.0")
os.system("del *.3")
os.system("clear")
wd.quit()