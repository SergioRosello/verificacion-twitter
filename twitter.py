from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.google.es")
    elem = driver.find_element_by_name("q")
    elem.send_keys("u-tad")
    elem.send_keys(Keys.RETURN)
    driver.close()
    print 'Hello world!'