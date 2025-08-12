# date : 2508120523
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 34.92665219306946
# generation time: 329.0114850997925
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def first_time_flow(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250812_052323_2296.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_2311.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div/div[2]/div[2]/button').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_3429.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div/div[2]/div[2]/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div/div[5]/div[1]/header/button[1]').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_4173.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div/div[5]/div[1]/header/button[1]').click()
    driver.find_element(By.ID,'confirm-password').screenshot('test_script/metamask_exp/screenshots/enter_20250812_052323_4876.png')
    driver.find_element(By.ID,'confirm-password').clear()
    driver.find_element(By.ID,'confirm-password').send_keys('correct horse battery staple')
    driver.find_element(By.ID,'create-password').screenshot('test_script/metamask_exp/screenshots/enter_20250812_052323_3219.png')
    driver.find_element(By.ID,'create-password').clear()
    driver.find_element(By.ID,'create-password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/form/div[3]/span/a').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_7689.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/form/div[3]/span/a').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/form/button').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_9960.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/form/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[2]/button[1]').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_7141.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[2]/button[1]').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/click_20250812_052323_2137.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').screenshot('test_script/metamask_exp/screenshots/assert_element_20250812_052323_6336.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-modal-close').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250812_052323_6406.png')

