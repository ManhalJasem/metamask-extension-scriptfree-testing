from test_script.metamask_exp.test_script_2508120618_incremental_security_FASTTEXT_300_SMALL_5_5_3 import first_time_flow
from test_script.metamask_exp.driver_manager import DriverManager


# Create a driver instance
driver_manager = DriverManager()

try:
    first_time_flow(driver_manager.get_driver())
    print("Metamask first time flow completed successfully. ✅")
except Exception as e:
    print(f"metamaskui: Metamask first_time_flow Failed. ❌")
finally:
    # Clean up the driver
    driver_manager.quit()

