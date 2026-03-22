from bs4 import BeautifulSoup

# Read HTML file
with open("Mr.Vijender_Scraping_Countries_Website_Data.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")



country_div_list=soup.find_all('div', class_="col-md-4 country")
# Country_Div_List is a list of all the information with the tag div whose class is col-md-4 country;
# [div1, div2, div3]
'''
<div class="col-md-4 country">
    <h3 class="country-name">
        <i class="flag-icon flag-icon-ad"></i>
        Andorra
    </h3>
    <div class="country-info">
        <strong>Capital:</strong> <span class="country-capital">Andorra la Vella</span><br>
        <strong>Population:</strong> <span class="country-population">84000</span><br>
        <strong>Area (km<sup>2</sup>):</strong> <span class="country-area">468.0</span><br>
    </div>
</div>
'''
for country_info in country_div_list:
    country_name = country_info.find('h3', class_='country-name').text.strip()
    country_capital = country_info.find('span', class_='country-capital').text.strip()
    
    country_population = int(country_info.find('span', class_="country-population").text.strip())
    country_area = country_info.find('span', class_="country-area").text.strip()
    print(country_name, country_capital, country_population, country_area)