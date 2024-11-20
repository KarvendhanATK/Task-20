#task-20 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.cowin.gov.in/")
time.sleep(3)

main_window_handle = driver.current_window_handle

wait = WebDriverWait(driver, 10)

faq_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "FAQ")))
faq_link.click()
time.sleep(5)
partners_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Partners')]")))
partners_link.click()
time.sleep(5)

window_handles = driver.window_handles

print("All window handles: ", window_handles)
time.sleep(4)

for handle in window_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        print(f"Switching to and closing window with handle: {handle}")
        driver.close()
time.sleep(4)
# Switch back to the main window
driver.switch_to.window(main_window_handle)
print("Switched back to the main window.")
time.sleep(4)

driver.quit()
