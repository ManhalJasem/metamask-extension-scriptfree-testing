# date : 2508110728
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 34.3732168674469
# generation time: 934.2971923351288
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def show_account_information(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_071412_4313.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_071412_8879.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_071412_1480.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_071412_6978.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[1]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[1]').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_071412_8456.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_071412_3204.png')
    assert '0x0Cc5261AB8cE458dc977078A3623E2BaDD27afD3' in driver.page_source, 'string "0x0Cc5261AB8cE458dc977078A3623E2BaDD27afD3" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_071412_8052.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-modal-close').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_071412_3242.png')

def add_account(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_071830_7473.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_071830_5787.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_071830_8347.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]').screenshot('test_script/metamask_exp/screenshots/click_div_20250811_071830_8392.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[2]/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_071830_5262.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[2]/div/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_071830_6417.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click(); document.querySelector('.menu__item.menu__item.menu__item--clickable').click();""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_071830_5755.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').screenshot('test_script/metamask_exp/screenshots/enter_20250811_071830_5360.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').send_keys('2nd account')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_071830_2570.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_071830_3373.png')
    assert '2nd account' in driver.page_source, 'string "2nd account" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_071830_9859.png')

def import_account_with_private_key(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_072121_3005.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_072121_5730.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_072121_8245.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_072121_8205.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').screenshot('test_script/metamask_exp/screenshots/click_div_20250811_072121_3045.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').click()
    driver.find_element(By.ID,'private-key-box').screenshot('test_script/metamask_exp/screenshots/enter_20250811_072121_1295.png')
    driver.find_element(By.ID,'private-key-box').clear()
    driver.find_element(By.ID,'private-key-box').send_keys('14abe6f4aab7f9f626fe981c864d0adeb5685f289ac9270c27b8fd790b4235d6')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_072121_2778.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_072121_3548.png')
    assert 'Imported' in driver.page_source, 'string "Imported" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_072121_6718.png')

def import_and_remove_account(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_072849_5409.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_072849_8299.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_072849_6473.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button').click()
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_072849_7757.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').screenshot('test_script/metamask_exp/screenshots/click_div_20250811_072849_3679.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').click()
    driver.find_element(By.ID,'private-key-box').screenshot('test_script/metamask_exp/screenshots/enter_20250811_072849_8964.png')
    driver.find_element(By.ID,'private-key-box').clear()
    driver.find_element(By.ID,'private-key-box').send_keys('F4EC2590A0C10DE95FBF4547845178910E40F5035320C516A18C117DE02B5669')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_072849_7596.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_072849_3548.png')
    assert 'Account 3' in driver.page_source, 'string "Account 3" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_072849_1037.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_072849_8511.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[7]/div[1]/img').screenshot('test_script/metamask_exp/screenshots/click_20250811_072849_9570.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[7]/div[1]/img').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[1]').screenshot('test_script/metamask_exp/screenshots/click_20250811_072849_2014.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[1]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_072849_4382.png')
    assert 'Account 1' in driver.page_source, 'string "Account 1" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_072849_8278.png')

