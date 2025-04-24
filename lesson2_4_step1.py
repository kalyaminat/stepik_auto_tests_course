from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button = browser.find_element(By.ID, 'book')
button.click()

browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
print(x_element)

result = browser.find_element(By.CSS_SELECTOR, "input#answer")
y = calc(x)
print(y)
result.send_keys(y)

button1 = browser.find_element(By.ID, "solve")
button1.click()

time.sleep(8)
# закрываем браузер после всех манипуляций
browser.quit()
