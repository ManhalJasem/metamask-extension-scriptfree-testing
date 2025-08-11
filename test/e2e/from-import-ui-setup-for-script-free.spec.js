const path = require('path')
const assert = require('assert')
const webdriver = require('selenium-webdriver')
const { By, Key, until } = webdriver
const {
  delay,
  buildChromeWebDriver,
  buildFirefoxWebdriver,
  installWebExt,
  getExtensionIdChrome,
  getExtensionIdFirefox,
} = require('./func-script-free-setup')
const {
  checkBrowserForConsoleErrors,
  closeAllWindowHandlesExcept,
  verboseReportOnFailure,
  findElement,
  findElements,
} = require('./helpers')
const fetchMockResponses = require('./fetch-mocks.js')


describe('Using MetaMask with an existing account', function () {
  let extensionId
  let driver

  const testSeedPhrase = 'forum vessel pink push lonely enact gentle tail admit parrot grunt dress'
  const testAddress = '0x0Cc5261AB8cE458dc977078A3623E2BaDD27afD3'
  const testPrivateKey2 = '14abe6f4aab7f9f626fe981c864d0adeb5685f289ac9270c27b8fd790b4235d6'
  const testPrivateKey3 = 'F4EC2590A0C10DE95FBF4547845178910E40F5035320C516A18C117DE02B5669'
  const tinyDelayMs = 200
  const regularDelayMs = 1000
  const largeDelayMs = regularDelayMs * 2

  this.timeout(0)
  this.bail(true)

  before(async function () {
    let extensionUrl
    switch (process.env.SELENIUM_BROWSER) {
      case 'chrome': {
        const extensionPath = path.resolve('dist/chrome')
        driver = buildChromeWebDriver(extensionPath)
        extensionId = await getExtensionIdChrome(driver)
        await delay(regularDelayMs)
        extensionUrl = `chrome-extension://${extensionId}/home.html`
        break
      }
      case 'firefox': {
        const extensionPath = path.resolve('dist/firefox')
        driver = buildFirefoxWebdriver()
        await installWebExt(driver, extensionPath)
        await delay(regularDelayMs)
        extensionId = await getExtensionIdFirefox(driver)
        extensionUrl = `moz-extension://${extensionId}/home.html`
        break
      }
    }
    // Depending on the state of the application built into the above directory (extPath) and the value of
    // METAMASK_DEBUG we will see different post-install behaviour and possibly some extra windows. Here we
    // are closing any extraneous windows to reset us to a single window before continuing.
    const [tab1] = await driver.getAllWindowHandles()
    await closeAllWindowHandlesExcept(driver, [tab1])
    await driver.switchTo().window(tab1)
    await driver.get(extensionUrl)
  })

  beforeEach(async function () {
    await driver.executeScript(
      'window.origFetch = window.fetch.bind(window);' +
      'window.fetch = ' +
      '(...args) => { ' +
      'if (args[0] === "https://ethgasstation.info/json/ethgasAPI.json") { return ' +
      'Promise.resolve({ json: () => Promise.resolve(JSON.parse(\'' + fetchMockResponses.ethGasBasic + '\')) }); } else if ' +
      '(args[0] === "https://ethgasstation.info/json/predictTable.json") { return ' +
      'Promise.resolve({ json: () => Promise.resolve(JSON.parse(\'' + fetchMockResponses.ethGasPredictTable + '\')) }); } else if ' +
      '(args[0].match(/chromeextensionmm/)) { return ' +
      'Promise.resolve({ json: () => Promise.resolve(JSON.parse(\'' + fetchMockResponses.metametrics + '\')) }); } else if ' +
      '(args[0] === "https://dev.blockscale.net/api/gasexpress.json") { return ' +
      'Promise.resolve({ json: () => Promise.resolve(JSON.parse(\'' + fetchMockResponses.gasExpress + '\')) }); } ' +
      'return window.origFetch(...args); };' +
      'function cancelInfuraRequest(requestDetails) {' +
        'console.log("Canceling: " + requestDetails.url);' +
        'return {' +
          'cancel: true' +
        '};' +
     ' }' +
      'window.chrome && window.chrome.webRequest && window.chrome.webRequest.onBeforeRequest.addListener(' +
        'cancelInfuraRequest,' +
        '{urls: ["https://*.infura.io/*"]},' +
        '["blocking"]' +
      ');'
    )
  })

  afterEach(async function () {
    if (process.env.SELENIUM_BROWSER === 'chrome') {
      const errors = await checkBrowserForConsoleErrors(driver)
      if (errors.length) {
        const errorReports = errors.map(err => err.message)
        const errorMessage = `Errors found in browser console:\n${errorReports.join('\n')}`
        console.error(new Error(errorMessage))
      }
    }
    if (this.currentTest.state === 'failed') {
      await verboseReportOnFailure(driver, this.currentTest)
    }
  })

  after(async function () {
    await driver.quit()
  })

  describe('First time flow starting from an existing seed phrase', () => {
    it('clicks the continue button on the welcome screen', async () => {
      await findElement(driver, By.css('.welcome-page__header'))
      const welcomeScreenBtn = await findElement(driver, By.css('.first-time-flow__button'))
      welcomeScreenBtn.click()
      await delay(largeDelayMs)
    })

    it('clicks the "Import Wallet" option', async () => {
      const customRpcButton = await findElement(driver, By.xpath(`//button[contains(text(), 'Import Wallet')]`))
      customRpcButton.click()
      await delay(largeDelayMs)
    })

    it('clicks the "No thanks" option on the metametrics opt-in screen', async () => {
      const optOutButton = await findElement(driver, By.css('.btn-default'))
      optOutButton.click()
      await delay(largeDelayMs)
    })

    it('imports a seed phrase', async () => {
      const [seedTextArea] = await findElements(driver, By.css('textarea.first-time-flow__textarea'))
      await seedTextArea.sendKeys(testSeedPhrase)
      await delay(regularDelayMs)

      const [password] = await findElements(driver, By.id('password'))
      await password.sendKeys('correct horse battery staple')
      const [confirmPassword] = await findElements(driver, By.id('confirm-password'))
      confirmPassword.sendKeys('correct horse battery staple')

      const tosCheckBox = await findElement(driver, By.css('.first-time-flow__checkbox'))
      await tosCheckBox.click()

      const [importButton] = await findElements(driver, By.xpath(`//button[contains(text(), 'Import')]`))
      await importButton.click()
      await delay(regularDelayMs)
    })

    it('clicks through the success screen', async () => {
      await findElement(driver, By.xpath(`//div[contains(text(), 'Congratulations')]`))
      const doneButton = await findElement(driver, By.css('button.first-time-flow__button'))
      await doneButton.click()
      await delay(regularDelayMs)
    })
  })

  describe('Show account information', () => {
    it('shows the correct account address', async () => {
      await driver.findElement(By.css('.account-details__details-button')).click()
      await driver.findElement(By.css('.qr-wrapper')).isDisplayed()
      await delay(regularDelayMs)

      const [address] = await findElements(driver, By.css('input.qr-ellip-address'))
      assert.equal(await address.getAttribute('value'), testAddress)

      await driver.executeScript("document.querySelector('.account-modal-close').click()")
      await delay(largeDelayMs)
    })

    it('shows a QR code for the account', async () => {
      await driver.findElement(By.css('.account-details__details-button')).click()
      await driver.findElement(By.css('.qr-wrapper')).isDisplayed()
      const detailModal = await driver.findElement(By.css('span .modal'))
      await delay(regularDelayMs)

      await driver.executeScript("document.querySelector('.account-modal-close').click()")
      await driver.wait(until.stalenessOf(detailModal))
      await delay(regularDelayMs)
    })
  })

  describe('Log out and log back in', () => {
    it('logs out of the account', async () => {
      const accountIdenticon = driver.findElement(By.css('.account-menu__icon .identicon'))
      accountIdenticon.click()
      await delay(regularDelayMs)

      const [logoutButton] = await findElements(driver, By.css('.account-menu__logout-button'))
      assert.equal(await logoutButton.getText(), 'Log out')
      await logoutButton.click()
      await delay(regularDelayMs)
    })

    it('accepts the account password after lock', async () => {
      await driver.findElement(By.id('password')).sendKeys('correct horse battery staple')
      await driver.findElement(By.id('password')).sendKeys(Key.ENTER)
      await delay(largeDelayMs)
    })
  })

})
