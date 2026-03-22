from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def getLocationValue(location):
    dictionary = {'Hialeah Gardens': '8',
                  'Coral Reef': '10',
                  'Northside': '13',
                  'Miami Gardens': '17',
				  'Margate': '2'}

    return dictionary[location]

def bookAppointment(request):
	options = webdriver.ChromeOptions()
	options.add_argument('--start-maximized')
	driver = webdriver.Chrome(options=options)
	wait = WebDriverWait(driver, 80)

	first_name =  "Vijender"
	last_name = "C"
	dob = '12/10/2002'
	email = "vijender4312@gmail.com"
	phone = "5522719697"
	location = "Margate"
	license = 'N/A'
	# service_type = request[6]

	try:
		driver.get("https://nqapflhsmv.nemoqappointment.com/appointments/")

		# Select location
		location_select_element = wait.until(
		EC.presence_of_element_located((By.NAME, "location"))
		)
		select_location = Select(location_select_element)
		select_location.select_by_value(getLocationValue(location))  # Your helper function
		print("Selected location.")

		# Wait for first name field & set it
		first_name_field = wait.until(EC.presence_of_element_located((By.ID, "first_name")))
		first_name_field.send_keys(first_name)
		print(f"Entered first name: {first_name}")

		last_name_field = wait.until(EC.presence_of_element_located((By.ID, "last_name")))
		last_name_field.send_keys(last_name)
		print(f"Entered last name: {last_name}")

		dob_field = wait.until(EC.presence_of_element_located((By.ID, "dob")))
		dob_field.send_keys(dob)
		print(f"Entered DOB: {dob}")

		email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
		email_field.send_keys(email)
		print(f"Entered email: {email}")

		license_field = wait.until(EC.presence_of_element_located((By.ID, "license")))
		license_field.send_keys(license)
		print("Entered license: N/A")

		phone_field = wait.until(EC.presence_of_element_located((By.ID, "phone")))
		phone_field.send_keys(phone)
		print(f"Entered phone: {phone}")

		service_select_element = driver.find_element(By.NAME, "service")
		select_service = Select(service_select_element)
		select_service.select_by_value("6")  # e.g. '1. Renew or Replace'
		print("Selected service.")
		
		state_select_element = driver.find_element(By.NAME, "state")
		state_service = Select(state_select_element)
		state_service.select_by_value("NJ")  # e.g. '1. Renew or Replace'
		print("Selected state.")
		
		wait = WebDriverWait(driver, 40)	
		clickable_days = driver.find_elements(By.XPATH, "//table[contains(@class,'ui-datepicker-calendar')]//td[a]")
		
		freeSlot = False
		for td in clickable_days:
			day_text = td.find_element(By.TAG_NAME, "a").text
			
			td_classes = td.get_attribute("class")
			if "free" in td_classes:
				freeSlot = True
				td.find_element(By.TAG_NAME, "a").click()
				wait = WebDriverWait(driver, 40)
				
				time_links = driver.find_elements(By.XPATH, "//div[contains(@class,'time')]//a[contains(@class,'time-value')]")
				print(time_links)
				time_slots = [link.text for link in time_links]

				print(f"\nAvailable slots on {td_classes}: {time_slots}")
		

		
	finally:
		input("Press Enter to close browser...")
		driver.quit()
        
bookAppointment([])