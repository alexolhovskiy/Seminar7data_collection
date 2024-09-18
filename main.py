from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #задержки
from selenium.webdriver.support import expected_conditions as EC #события
from selenium.webdriver.common.action_chains import ActionChains

import time
import csv
from pprint import pprint

options=Options()
options.add_argument('start=maximized')
driver=webdriver.Chrome(options=options)


def writeToFile(filename,laptops):
    # Запись в CSV файл
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'price', 'url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(laptops)

    print(f"Данные записаны в {filename}")




laptops=[]
driver.get("https://www.ebay.com/")

time.sleep(2)#задержка для полной загрузки страницы
input= driver.find_element(By.ID,'gh-ac')#поиск по id
input.send_keys('laptop computers Full Warranty')#вводим поисковый запрос
input.send_keys(Keys.ENTER)#жмем ввод
wait=WebDriverWait(driver,60)#ждет до загрузки или до указанного времени

page=1

while page<6:
    
    cards=wait.until(EC.presence_of_all_elements_located((By.XPATH,"//ul[@class='srp-results srp-list clearfix']//div[@class='s-item__wrapper clearfix']")))
    print(f"Страница {page},Найдено карточек: {len(cards)}")
    
    #Собираем данные
    for card in cards:
        laptop={}
        try:
            laptop["name"]=card.find_element(By.CLASS_NAME,"s-item__title").text
        except:
            laptop["name"]="None"
        try:
            laptop["price"]=card.find_element(By.CLASS_NAME,"s-item__price").text
        except:
            laptop["price"]="None"
        try:
            laptop["url"]=card.find_element(By.CLASS_NAME,"s-item__link").get_attribute("href")
        except:
            laptop["url"]="None"
        laptops.append(laptop)
    
    # try:
    #     button=driver.find_element(By.CLASS_NAME,"pagination__next") #переходим на след страницу - кликаем на кнопке next
    #     actions=ActionChains(driver)#Это перемещение прокрутки к элементу
    #     # actions.scroll_to_element(button).click()#к button #клик по кнопке
    #     actions.move_to_element(button).click()#к button #клик по кнопке
    #     actions.perform()#выполнение действия, или цепочки действий. Таким образом можно нажать 2 кнопки одновременно например
    #     time.sleep(5)
    # except:
    #     break

    button=driver.find_element(By.CLASS_NAME,"pagination__next") 
    actions=ActionChains(driver)#Это перемещение прокрутки к элементу
    actions.move_to_element(button).click()#к button #клик по кнопке
    actions.perform()#выполнение действия, или цепочки действий. Таким образом можно нажать 2 кнопки одновременно например
    time.sleep(2)
    page+=1

time.sleep(2)
# writeToFile("eBayLaps.csv",laptops)

# laptops=[]
driver.get("https://www.amazon.com/")

time.sleep(30)#задержка для полной загрузки страницы
input= driver.find_element(By.ID,'twotabsearchtextbox')#поиск по id
input.send_keys('laptop full warranty')#вводим поисковый запрос
input.send_keys(Keys.ENTER)#жмем ввод
wait=WebDriverWait(driver,60)#ждет до загрузки или до указанного времени
scrolls=10
scroll_pause_time=1
while True:
    for _ in range(scrolls):
        ActionChains(driver).scroll_by_amount(0, 500).perform()
        time.sleep(scroll_pause_time)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,"puis-card-container")))
        except Exception as e:
            print("Новых элементов больше нет или произошла ошибка:", e)
            break

    cards=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"puis-card-container")))
    # cards=driver.find_elements(By.XPATH,"//div[@class='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2ylpaeq2w6ozo2hshprbixi3ep s-latency-cf-section puis-card-border']")
    print(f"Найдено карточек: {len(cards)}")
    
    #Собираем данные
    for card in cards:
        laptop={}
        try:
            laptop["name"]=card.find_element(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']").text #любой тег по имени класса
        except:
            laptop["name"]="None"
        try:
            laptop["price"]=card.find_element(By.XPATH,".//span[@class='a-color-base']").text
        except:
            laptop["price"]="None"
        try:
            laptop["url"]=card.find_element(By.XPATH,".//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").get_attribute("href") #любой тег по атрибуту
        except:
            laptop["url"]="None"
        print(laptop)
        laptops.append(laptop)
    
    try:
        button=driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']") #переходим на след страницу - кликаем на кнопке next
        actions=ActionChains(driver)#Это перемещение прокрутки к элементу
        actions.move_to_element(button).click()#к button #клик по кнопке
        actions.perform()#выполнение действия, или цепочки действий. Таким образом можно нажать 2 кнопки одновременно например
        time.sleep(2)
    except:
        break

time.sleep(2)#когда выполнил скрипт - закрывает браузер - задержка
# writeToFile("AmazoneLaps.csv",laptops)


# laptops=[]
driver.get("https://www.aliexpress.com/")

time.sleep(30)#задержка для полной загрузки страницы
input= driver.find_element(By.ID,'search-words')#поиск по id
input.send_keys('laptop')#вводим поисковый запрос
input.send_keys(Keys.ENTER)#жмем ввод
page=1
scroll_pause_time = 2
scrolls = 15
wait=WebDriverWait(driver,60)

while page<6:
    for _ in range(scrolls):
        ActionChains(driver).scroll_by_amount(0, 500).perform()
        time.sleep(scroll_pause_time)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='list--gallery--C2f2tvm search-item-card-wrapper-gallery']")))
        except Exception as e:
            print("Новых элементов больше нет или произошла ошибка:", e)
            break

    cards=driver.find_elements(By.XPATH,"//div[@class='list--gallery--C2f2tvm search-item-card-wrapper-gallery']")#указываем чего ждем - появление элемента
    print(f"Страница {page}: Найдено карточек: {len(cards)}")
    
    #Собираем данные
    for card in cards:
        laptop={}
        try:
            laptop["name"]=card.find_element(By.XPATH,".//h3[@class='multi--titleText--nXeOvyr']").text #любой тег по имени класса
        except:
            laptop["name"]="None"
        try:
            laptop["price"]=card.find_element(By.XPATH,".//div[@class='multi--price-sale--U-S0jtj']").text
        except:
            laptop["price"]="None"
        try:
            laptop["url"]=card.find_element(By.XPATH,".//a[@class='multi--container--1UZxxHY cards--card--3PJxwBm search-card-item']").get_attribute("href") #любой тег по атрибуту
        except:
            laptop["url"]="None"
        # print(laptop)
        laptops.append(laptop)
    
    try:
        button=driver.find_element(By.XPATH,"//li[@class='comet-pagination-next']") #переходим на след страницу - кликаем на кнопке next
        actions=ActionChains(driver)#Это перемещение прокрутки к элементу
        actions.move_to_element(button).click()#к button #клик по кнопке
        actions.perform()#выполнение действия, или цепочки действий. Таким образом можно нажать 2 кнопки одновременно например
        page+=1
        time.sleep(2)
    except:
        break

time.sleep(2)#когда выполнил скрипт - закрывает браузер - задержка
# writeToFile("AliexpressLaps.csv",laptops)
writeToFile("laps.csv",laptops)





