from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

def main():
    # Set up Facebook login account name and password
    account = "sample@gmail.com"
    password = "sample"

    # Set up Facebook groups to post, you must be a member of the group
    groups_links_list = [
        "https://www.facebook.com/groups/sample1", "https://www.facebook.com/groups/sample2"
    ]

    # Set up text content to post
    message = "Checkout an amazing selenium script for posting automaticaaly on Facebook groups! https://github.com/ethanXWL/Python-Selenium-Facebook-group-poster"

    # Set up paths of images to post
    images_list = ['C:/Users/OEM/Pictures/sample1.jpg','C:/Users/OEM/Pictures/sample2.jpg']

    # Login Facebook
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.facebook.com')
    emailelement = driver.find_element(By.XPATH,'//*[@id="email"]')
    emailelement.send_keys(account)
    passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
    passelement.send_keys(password)
    loginelement = driver.find_element(By.XPATH,'//*[@id="loginbutton"]')
    loginelement.click()

    # Post on each group
    for group in groups_links_list:
        driver.get(group)
        time.sleep(2)
        try:
            driver.find_element(By.XPATH,'//*[@label="Start Discussion"]').click()
            post_box=driver.find_element_by_css_selector("[name='xhpc_message_text']")
        except:
            post_box=driver.find_element_by_css_selector("[name='xhpc_message_text']")
        post_box.send_keys(message)
        time.sleep(1)
        for photo in images_list:
            photo_element = driver.find_element(By.XPATH,'//input[@type="file"]')
            photo_element.send_keys(photo)
            time.sleep(1)
        time.sleep(6)
        post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
        clickable = False
        while not clickable:
            cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
            if cursor == "pointer":
                clickable = True
            break
        post_button.click()
        time.sleep(5)
    # Close driver
    driver.close()

if __name__ == '__main__':
  main()


