import random
import sys
import time
import pandas as pd

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


def get_dataframe(file):
    string_tokens = file.split(".")
    if len(string_tokens) != 2:
        sys.exit("Invalid file")
    else:
        if string_tokens[1] == "csv":
            df = pd.read_csv(file)
        elif string_tokens[1] == "xlsx":
            df = pd.read_excel(file)
        elif string_tokens[1] == "json":
            df = pd.read_json(file)
        else:
            sys.exit("Invalid extension")

        return df



browser = webdriver.Chrome('chromedriver')

def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2, 4))

        input_username = browser.find_element(By.NAME, 'username')
        input_password = browser.find_element(By.NAME, 'password')

        input_username.send_keys(username)
        time.sleep(random.randrange(2, 4))
        input_password.send_keys(password)
        time.sleep(random.randrange(2, 4))
        input_password.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()


XPath_DM = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div'
XPath_not_now = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[' \
                '3]/button[2] '
XPath_send_message = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[' \
                     '2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button '
XPath_to = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[' \
           '1]/div/div[2]/input '
XPath_choose_user = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[' \
                    '2]/div[2]/div[1]/div[1]/div/div/div[3]/div/button '
XPath_next = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[' \
             '3]/div/button '
XPath_message_body = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[' \
                     '2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea '
XPath_next_message = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[' \
                     '2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button '


def send_message(df, message_tokens):
    try:
        browser.find_element(By.XPATH, XPath_DM).click()
        time.sleep(random.randrange(3, 5))
        browser.find_element(By.XPATH, XPath_not_now).click()
        time.sleep(random.randrange(2, 4))

        browser.find_element(By.XPATH, XPath_send_message).click()
        time.sleep(random.randrange(3, 5))
        for index, row in df.iterrows():
            browser.find_element(By.XPATH, XPath_to).send_keys(row['Username'])
            time.sleep(random.randrange(2, 4))
            browser.find_element(By.XPATH, XPath_choose_user).click()
            time.sleep(random.randrange(3, 6))
            browser.find_element(By.XPATH, XPath_next).click()
            time.sleep(random.randrange(3, 6))
            text_area = browser.find_element(By.XPATH, XPath_message_body)

            if len(message_tokens) == 2:
                personalized_message = message_tokens[0] + row['Name'] + message_tokens[1]
            else:
                personalized_message = message_tokens[0]

            text_area.send_keys(personalized_message)
            time.sleep(random.randrange(2, 4))
            text_area.send_keys(Keys.ENTER)

            print(f"Message sent to {row['Username']}")
            time.sleep(5)

            browser.find_element(By.XPATH, XPath_next_message).click()

    except Exception as err:
        print(err)
        browser.quit()