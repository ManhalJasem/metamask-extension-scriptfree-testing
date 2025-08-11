from test_script.metamask_exp.test_script_2508110524_from_import_ui_FASTTEXT_300_SMALL_5_5_3 import show_account_information, add_account, import_account_with_private_key, import_and_remove_account
from test_script.metamask_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    show_account_information(driver_manager.get_driver())
    print("Metamask account information displayed successfully. ✅")
except Exception as e:
    print(f"An error occurred while showing account information: {e}")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    add_account(driver_manager.get_driver())
    print("Metamask account added successfully. ✅")
except Exception as e:
    print(f"An error occurred while adding account: {e}")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    import_account_with_private_key(driver_manager.get_driver())
    print("Metamask account imported successfully. ✅")
except Exception as e:
    print(f"An error occurred while importing account: {e}")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    import_and_remove_account(driver_manager.get_driver())
    print("Metamask account imported and removed successfully. ✅")
except Exception as e:
    print(f"An error occurred while importing and removing account: {e}")
finally:
    # Clean up the driver
    pass
