from email.mime import image
from threading import TIMEOUT_MAX
from tkinter.ttk import Progressbar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tqdm
import time
num=1
wget="C:\gnu\wget.exe --no-check-certificate -o c:/nul "
url=input("Introduce la url: ")
folder = input("Introduce el nombre de la carpeta: ")
os.system("mkdir "+folder)
os.system("cd "+folder)
os.chdir(folder)
folder = folder + " "
options = webdriver.ChromeOptions()
options.add_argument("headless")
wd = webdriver.Chrome(executable_path="C:/Users/hendr/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options)
wd.get(url)
times=wd.find_element(By.XPATH, ('/html/body/div[1]/div[1]/div[1]/div/span[2]')).text
times = int(times)
for i in range(times):
        currurl= wd.current_url
        print("current url: " + currurl)
        photo=wd.find_element(By.XPATH, ('/html/body/div[1]/div[2]/a/img')).get_attribute('src')
        actualnumber=wd.find_element(By.XPATH,('//*[@id="i2"]/div[1]/div/span[1]')).text
        actualnumber=int(actualnumber)
        os.system(wget + photo)
        element=wd.find_element(By.XPATH, ('//*[@id="i3"]'))
        element.click()
        time.sleep(2)
        progress=actualnumber/times
        #implement a progressbar with the variables times and actualnumber
        pbar = tqdm.tqdm(total=times)
        num=num+1
        print("Total progress: ")
        pbar.update(actualnumber)
        pbar.close()
os.system("rename *.2 *.jpg")
os.system("rename *.1 *.jpg")
os.system("rename *.0 *.jpg")
os.system("rename *.3 *.jpg")
os.system("del *.2")
os.system("del *.1")
os.system("del *.0")
os.system("del *.3")
os.system("cls")
wd.quit()