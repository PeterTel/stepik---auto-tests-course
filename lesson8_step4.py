from selenium import webdriver
import time
import os 

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/file_input.html")

    element = browser.find_element_by_css_selector("[name='firstname']")
    element.send_keys("Мой ответ")
    element = browser.find_element_by_css_selector("[name='lastname']")	
    element.send_keys("Мой ответ")
    element = browser.find_element_by_css_selector("[name='email']")
    element.send_keys("Мой ответ")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к файлу со скриптом  
    file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла в той же директории
    fd = browser.find_element_by_id("file") # ищим кнопку прикрепить
    fd.send_keys(file_path) # прикреплем файл
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
 
    time.sleep(1)


finally:
   
    time.sleep(10)
  
    browser.quit()






