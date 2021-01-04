import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME=60
email='email'
password='password'

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
driver.get('https://youtube.com/edit?video_id=DO_41NWqOxU6ups=1')
driver.find_element_by_id('identifierId').send_keys(email)
driver.find_element_by_id('identifierNext').click()

#tunggu sampai password muncul
element = WebDriverWait(driver,WAIT_TIME).until(EC.element_to_be_clickable((By.NAME,'password')))
driver.find_element_by_name('password').send_keys(password)
element.send_keys(password)
driver.find_element_by_id('passwordNext').click()

#tunggu sampai Use Youtube As... muncul
element = WebDriverWait(driver,WAIT_TIME).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='radio'][value='117836062881483054646']")))
element.click()
driver.find_element_by_id('identity-prompt-confirm-button').click()

#tunggu sampai .yt-uix-form-input-textarea-.metadata-share-contacts bisa diklik
element = WebDriverWait(driver,WAIT_TIME).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'.yt-uix-form-input-textarea-.metadata-share-contacts')))
element.send_keys('email')
driver.find_element_by_css_selector('.yt-uix-form-input-checkbox.notify-via-email').click()
driver.find_element_by_css_selector(
    '.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary.sharing-dialog-button.sharing-dialog-ok').click()

#tunggu sampai muncul Saved. di .yt-dialog-working-bubble .yt-dialog-waiting-content
element = WebDriverWait(driver,WAIT_TIME).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.yt-dialog-working-bubble .yt-dialog-waiting-content'),'Saved.'))
driver.quit()