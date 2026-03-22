from bs4 import BeautifulSoup

# Read HTML file
with open("Creating_A_Table_Using HTML.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Get all rows (skip header row)
rows = soup.find_all("tr", class_="okay")
print(rows)

# Loop through each student row
# for row in rows:
#     tds = row.find_all("td")
#     name = tds[0].text.replace("Name:", "").strip()
#     tds = tds[2:]
#     marks = 0
#     for td in tds:
#         marks += int(td.text)
#     total = marks
#     print(f"{name}: {total}")