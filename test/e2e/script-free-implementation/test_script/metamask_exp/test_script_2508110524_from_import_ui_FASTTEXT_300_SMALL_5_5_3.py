# date : 2508110524
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 33.77372097969055
# generation time: 973.7075917720795
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def show_account_information(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_050929_9705.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_050929_1500.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').screenshot('test_script/metamask_exp/screenshots/click_20250811_050929_1039.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/click_20250811_050929_6003.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[1]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[1]').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_050929_2944.png')
    assert driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/span/div[1]/div/div/div/div[4]/div[2]/input').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_050929_7885.png')
    assert '0x0Cc5261AB8cE458dc977078A3623E2BaDD27afD3' in driver.page_source, 'string "0x0Cc5261AB8cE458dc977078A3623E2BaDD27afD3" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_050929_7200.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-modal-close').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_050929_4045.png')

def add_account(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_051352_8853.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_051352_1523.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').screenshot('test_script/metamask_exp/screenshots/click_20250811_051352_9030.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]').screenshot('test_script/metamask_exp/screenshots/click_div_20250811_051352_4810.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]').click()
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/li[6]/span').screenshot('test_script/metamask_exp/screenshots/click_20250811_051352_1295.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/li[6]/span').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/button').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/button').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_051352_8940.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click(); document.querySelector('.menu__item.menu__item.menu__item--clickable').click();""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_051352_5259.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').screenshot('test_script/metamask_exp/screenshots/enter_20250811_051352_3013.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[2]/input').send_keys('2nd account')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_051352_6910.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_051352_2166.png')
    assert '2nd account' in driver.page_source, 'string "2nd account" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_051352_1130.png')

def import_account_with_private_key(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_051649_2369.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_051649_4406.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').screenshot('test_script/metamask_exp/screenshots/click_20250811_051649_6836.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').click()
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_051649_1378.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').screenshot('test_script/metamask_exp/screenshots/click_div_20250811_051649_3536.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').click()
    driver.find_element(By.ID,'private-key-box').screenshot('test_script/metamask_exp/screenshots/enter_20250811_051649_2002.png')
    driver.find_element(By.ID,'private-key-box').clear()
    driver.find_element(By.ID,'private-key-box').send_keys('14abe6f4aab7f9f626fe981c864d0adeb5685f289ac9270c27b8fd790b4235d6')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_051649_3398.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_051649_3746.png')
    assert 'Imported' in driver.page_source, 'string "Imported" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_051649_7857.png')

def import_and_remove_account(driver):
    driver.get('chrome-extension://fochammdjkalfjmglakiadgeeipdajka/home.html#')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/metamask_exp/screenshots/open_20250811_052438_6039.png')
    driver.find_element(By.ID,'password').screenshot('test_script/metamask_exp/screenshots/enter_20250811_052438_5919.png')
    driver.find_element(By.ID,'password').clear()
    driver.find_element(By.ID,'password').send_keys('correct horse battery staple')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').screenshot('test_script/metamask_exp/screenshots/click_20250811_052438_1875.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/button/span').click()
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_052438_7978.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').screenshot('test_script/metamask_exp/screenshots/click_div_20250811_052438_7805.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div[7]/div[2]').click()
    driver.find_element(By.ID,'private-key-box').screenshot('test_script/metamask_exp/screenshots/enter_20250811_052438_4879.png')
    driver.find_element(By.ID,'private-key-box').clear()
    driver.find_element(By.ID,'private-key-box').send_keys('F4EC2590A0C10DE95FBF4547845178910E40F5035320C516A18C117DE02B5669')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_052438_5995.png')
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div/div/div[4]/div/div/div[1]/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_052438_4322.png')
    assert 'Account 3' in driver.page_source, 'string "Account 3" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_052438_1006.png')
    sleep(2)
    driver.execute_script("""document.querySelector('.account-menu__icon').click()""")
    driver.save_screenshot('test_script/metamask_exp/screenshots/execute_script_20250811_052438_1923.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[5]/div/div/div[1]/div[1]/div[1]/div[3]/span').screenshot('test_script/metamask_exp/screenshots/click_20250811_052438_8398.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[5]/div/div/div[1]/div[1]/div[1]/div[3]/span').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[5]/div/div/div[2]/div[1]/div/div[2]/button[2]').screenshot('test_script/metamask_exp/screenshots/click_20250811_052438_5854.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[5]/div/div/div[2]/div[1]/div/div[2]/button[2]').click()
    assert driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[4]/div/div[1]/div[3]/div[1]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[4]/div/div[1]/div[3]/div[1]').screenshot('test_script/metamask_exp/screenshots/assert_element_20250811_052438_6656.png')
    assert 'Account 1' in driver.page_source, 'string "Account 1" is not exist'
    driver.save_screenshot('test_script/metamask_exp/screenshots/assert_string_20250811_052438_4038.png')

