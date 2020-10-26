def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    valuex = int(x_element.get_attribute("valuex"))
    y = calc(valuex)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

# не забываем оставить пустую строку в конце файла