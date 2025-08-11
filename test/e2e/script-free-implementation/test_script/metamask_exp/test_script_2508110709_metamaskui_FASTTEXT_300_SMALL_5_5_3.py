# date : 2508110709
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 35.49086022377014
# generation time: 234.18453311920166
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def show_qr_code(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_070711_3788.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_070711_7087.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_070711_4837.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_070711_8252.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[1]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[1]').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_070711_8885.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-modal-close').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_070711_8037.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_070711_2813.png')

def add_account(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_070913_4462.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_070913_7127.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_070913_8729.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_070913_2622.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click(); document.querySelector('.menu__item.menu__item.menu__item--clickable').click();""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_070913_4137.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').screenshot('test_script/metamask_exp/screenshots/enter_20250811_070913_4447.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').send_keys('2nd account')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_070913_6835.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_070913_9597.png')

