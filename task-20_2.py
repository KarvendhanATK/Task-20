import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

driver = webdriver.Chrome()
driver.get("https://labour.gov.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Task 1: Go to "Documents" menu and download the Monthly Progress Report
documents_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Documents")))
ActionChains(driver).move_to_element(documents_menu).perform()

progress_report_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Monthly Progress Report")))
report_url = progress_report_link.get_attribute("href")

response = requests.get(report_url)
with open("Monthly_Progress_Report.pdf", "wb") as file:
    file.write(response.content)
print("Downloaded Monthly Progress Report")

# Task 2: Go to "Media" > "Photo Gallery" and download the first 10 images
media_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Media")))
ActionChains(driver).move_to_element(media_menu).perform()

photo_gallery_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Photo Gallery")))
photo_gallery_link.click()

time.sleep(3)

images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))

folder_name = "Downloaded_Photos"
os.makedirs(folder_name, exist_ok=True)

for i, img in enumerate(images[:10]):
    img_url = img.get_attribute("src")
    if img_url:
        img_data = requests.get(img_url).content
        with open(os.path.join(folder_name, f"photo_{i+1}.jpg"), "wb") as file:
            file.write(img_data)
        print(f"Downloaded photo {i+1}")

driver.quit()
