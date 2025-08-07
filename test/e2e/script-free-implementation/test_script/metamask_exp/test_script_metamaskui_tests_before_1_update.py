# date : 2508070923
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 40.447142362594604
# generation time: 240.6745846271515
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

def show_qr_code(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250807_092109.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.save_screenshot('test_script/metamask_exp/screenshots/enter_20250807_092109.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    driver.save_screenshot('test_script/metamask_exp/screenshots/click_20250807_092109.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').click()
    driver.save_screenshot('test_script/metamask_exp/screenshots/click_20250807_092109.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').is_displayed()
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_element_20250807_092109.png')
    driver.execute_script("""document.querySelector('.account-modal-close').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250807_092109.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').is_displayed()
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_element_20250807_092109.png')

def add_account(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250807_092315.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.save_screenshot('test_script/metamask_exp/screenshots/enter_20250807_092315.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    driver.save_screenshot('test_script/metamask_exp/screenshots/click_20250807_092315.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').is_displayed()
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_element_20250807_092315.png')
    driver.execute_script("""document.querySelector('.account-menu__icon').click(); document.querySelector('.menu__item.menu__item.menu__item--clickable').click();""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250807_092315.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').send_keys('2nd account')
    driver.save_screenshot('test_script/metamask_exp/screenshots/enter_20250807_092315.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').click()
    driver.save_screenshot('test_script/metamask_exp/screenshots/click_20250807_092315.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').is_displayed()
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_element_20250807_092315.png')

