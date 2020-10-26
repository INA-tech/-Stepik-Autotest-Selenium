def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    browser.execute_script('button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);')
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

# не забываем оставить пустую строку в конце файла