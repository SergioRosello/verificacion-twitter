from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.twitter.com")
    login = driver.find_element_by_id('signin-email')
    login.send_keys("@login_prueba")
    password = driver.find_element_by_id('signin-password')
    password.send_keys('verificacion2017')
    password.send_keys(Keys.ENTER)
    driver.set_page_load_timeout(2)
    tweet = driver.find_element_by_id('tweet-box-home-timeline')
    tweet.send_keys('Hi. I\'m using Selenium.')
    tweet.send_keys(Keys.CONTROL, Keys.ENTER)
    time.sleep(5)
    driver.close()