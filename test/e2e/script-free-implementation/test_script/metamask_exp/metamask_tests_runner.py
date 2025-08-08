from test_script.metamask_exp.test_script_2508080658_metamaskui_FASTTEXT_300_SMALL_5_5_3 import show_qr_code, add_account
from test_script.metamask_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    show_qr_code(driver_manager.get_driver())
    print("Metamask QR Code displayed successfully. ✅")
finally:
    # Clean up the driver
    driver_manager.quit()

driver_manager2 = DriverManager()
try:
    add_account(driver_manager2.get_driver())
    print("Metamask Add Account test completed successfully. ✅")
finally:
    # Clean up the driver
    driver_manager2.quit()
