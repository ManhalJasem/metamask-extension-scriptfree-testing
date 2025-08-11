from test_script.metamask_exp.test_script_2508110709_metamaskui_FASTTEXT_300_SMALL_5_5_3 import show_qr_code, add_account
from test_script.metamask_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    show_qr_code(driver_manager.get_driver())
    print("Metamask QR code displayed successfully. ✅")
except Exception as e:
    print(f"metamaskui: Metamask show_qr_code Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()

# Create a driver instance
driver_manager = DriverManager()

try:
    add_account(driver_manager.get_driver())
    print("Metamask account added successfully. ✅")
except Exception as e:
   print(f"metamaskui: Metamask add_account Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()

