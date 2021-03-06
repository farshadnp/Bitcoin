from time import sleep
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from info import user, passwd
import time


class Bot():
    def __init__(self):
        self.login(user, passwd)

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.instagram.com/')

        sleep(10)
        username_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username_input.send_keys(username)
        print(">>>> Username inserted")
        sleep(1)

        password_input = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password_input.send_keys(password)
        print(">>>> Password inserted")
        sleep(1)

        # click on Login-button
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
        print(">>>> Loged in")
        sleep(7)

        # redirect to main panel of instagram
        # self.driver.get('https://www.instagram.com/')
        # sleep(4)

        # Bypass save your login info popup
        # self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        # sleep(4)

    # go to #BTC hashtah with 7billion post over the world
        self.driver.get('https://www.instagram.com/explore/tags/btc/')
        sleep(6)

        # scroll page for show more post (bypass post lazy loading)
        print(">>>> Scrolling for Get more post...")
        for i in range(300):
            self.driver.execute_script("window.scrollBy(0, 400)")
            sleep(0.8)

        # find image src with loop condition
        listOfSrc = []
        for i in self.driver.find_elements_by_class_name('FFVAD'):
            listOfSrc.append(i.get_attribute('src'))
            sleep(1)
            #print(listOfSrc)
            #print('__________________________\n')
            #sleep(0.1)
            # make dataframe from src tags
            UrlDF = pd.DataFrame(listOfSrc)
            # export src as CSV file for next steps
            UrlDF.to_csv('url.csv')


        # make dataframe from src tags
        UrlDF = pd.DataFrame(listOfSrc)
        # export src as CSV file for next steps
        UrlDF.to_csv('url.csv')


def main():
    myBot = Bot()


if __name__ == '__main__':
    main()
