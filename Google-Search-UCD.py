import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# --- START THE BROWSER ---
driver = uc.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()

# --- PERFORM GOOGLE SEARCH ---
search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
time.sleep(1)  # Small wait to ensure the input box is ready (WebDriverWait is more reliable)

search_box.send_keys("Tech With Tim")
search_box.send_keys(Keys.RETURN)

# --- CLICK ON THE SEARCH RESULT LINK ---
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

# --- WAIT TO VIEW RESULTS BEFORE EXITING ---
time.sleep(5)  # Give time to observe the result page before quitting
driver.quit()
