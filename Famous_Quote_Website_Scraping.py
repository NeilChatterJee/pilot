from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://nqapflhsmv.nemoqappointment.com/appointments-miami-dade/")

    wait = WebDriverWait(driver, 20)

    # Wait for location dropdown and select a location
    location_select_element = wait.until(
        EC.presence_of_element_located((By.NAME, "location"))
    )
    select_location = Select(location_select_element)
    select_location.select_by_value("8")  # Hialeah Gardens
    print("Selected location.")

    # Now wait for the service dropdown to be filled (watch for more than 1 option)
    def services_loaded(driver):
        service_select = driver.find_element(By.NAME, "service")
        options = service_select.find_elements(By.TAG_NAME, "option")
        time.sleep(30)
        return len(options) > 1  # means JS loaded new options

    wait.until(services_loaded)
    print("Service options loaded.")
    
    # Now select the service
    service_select_element = driver.find_element(By.NAME, "service")
    select_service = Select(service_select_element)
    select_service.select_by_value("2")  # e.g. '1. Renew or Replace'
    print("Selected service.")
    # Now enter the phone number
    phone_field = driver.find_element(By.ID("phone"))
    phone_field.send_keys('111-222-3333')

finally:
    input("Press Enter to close browser...")
    driver.quit()
