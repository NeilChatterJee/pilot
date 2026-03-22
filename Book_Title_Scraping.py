import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'



response = requests.get(url)
read_file = BeautifulSoup(response.content, "html.parser")
rows = read_file.find_all("div", class_="side_categories" )


new_row = rows[0].find_all('a')
# i =0
for row in new_row:
    print(row.text.strip())
#     attr = row.attrs
#     key = 'title'
#     if key in attr:
#         print(attr[key])
    

# <a class='ret' title='fat'>mat</a>
# a = {'class': , 'title': }
    
