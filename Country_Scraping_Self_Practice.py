import requests
from bs4 import BeautifulSoup

url = 'https://nqapflhsmv.nemoqappointment.com/appointments-miami-dade/'

response = requests.get(url)
""" ####if response.status_code == 200:
        print("Response content:")
        print(response.text) """

read_file = BeautifulSoup(response.text,'html.parser')
rows = read_file.find_all("div", class_="ea-phone-field-group")
print(rows)

