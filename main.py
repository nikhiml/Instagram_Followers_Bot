import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

chrome_driver_path = '/Users/nikhilmittal/Documents/Selenium/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# The following can be hardcoded in the code or can get from the user
url = 'https://www.instagram.com/'
u_name = '***********'
pwd = '**********'
target_acct = '********'


class Instagram:
    def __init__(self, my_driver, url_link, username, password, acct_to_follow):
        self.my_web_driver = my_driver
        self.url_to = url_link
        self.login_user = username
        self.login_pwd = password
        self.acct_liked = acct_to_follow
        self.login()

    def login(self):

        self.my_web_driver.get(self.url_to)
        time.sleep(5)
        email_input = self.my_web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        email_input.send_keys(self.login_user)

        pwd_input = self.my_web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        pwd_input.send_keys(self.login_pwd)

        log_in = self.my_web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')
        log_in.click()

    def follow(self):

        notification_btn = self.my_web_driver.find_element(by=By.XPATH,
                                                   value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
        notification_btn.click()

        input_field = self.my_web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')
        input_field.send_keys(self.acct_liked)

        time.sleep(3)

        input_acct = self.my_web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div')
        input_acct.click()

        time.sleep(5)

        followers_count = self.my_web_driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers_count.click()

        time.sleep(5)

        followers_all = self.my_web_driver.find_elements(by=By.CSS_SELECTOR, value='._aaey li button')

        n = 0
        for follower in followers_all:
            n += 1
            if n < 5:
                follower.click()
                time.sleep(7)

        time.sleep(5)

        self.my_web_driver.quit()

# Main
# Create object and login
my_insta_obj = Instagram(driver, url, u_name, pwd, target_acct)

# Wait after logging in for page to fully load up
time.sleep(15)

# Call the follow method of the class
my_insta_obj.follow()


