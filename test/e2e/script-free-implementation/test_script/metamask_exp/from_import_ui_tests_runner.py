from test_script.metamask_exp.test_script_2508110728_from_import_ui_FASTTEXT_300_SMALL_5_5_3 import show_account_information, add_account, import_account_with_private_key, import_and_remove_account
from test_script.metamask_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    show_account_information(driver_manager.get_driver())
    print("from_import_ui: account information displayed successfully. ✅")
except Exception as e:
    print(f"from_import_ui: Metamask show_account_information Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    add_account(driver_manager.get_driver())
    print("from_import_ui: account added successfully. ✅")
except Exception as e:
    print(f"from_import_ui: Metamask add_account Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    import_account_with_private_key(driver_manager.get_driver())
    print("from_import_ui: Metamask account imported successfully. ✅")
except Exception as e:
    print(f"from_import_ui: Metamask import_account_with_private_key Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    import_and_remove_account(driver_manager.get_driver())
    print("from_import_ui: Metamask account imported and removed successfully. ✅")
except Exception as e:
    print("from_import_ui: Metamask import_and_remove_account Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()
