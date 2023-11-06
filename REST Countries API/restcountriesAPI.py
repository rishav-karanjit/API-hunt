import requests

# Retrieve information about Brazil
url_brazil = 'https://restcountries.com/v3.1/name/brazil'
response_brazil = requests.get(url_brazil)
brazil_data = response_brazil.json()
brazil_info = brazil_data[0]

print("Information about Brazil:")
print(f"Population: {brazil_info['population']}")
print(f"Area: {brazil_info['area']} square kilometers")
# Note: The official language is within the 'languages' dictionary.
# Sometimes there can be more than one official language.
official_languages = ', '.join(brazil_info['languages'].values())
print(f"Official Languages: {official_languages}")

# Retrieve a list of all countries in Africa
url_africa = 'https://restcountries.com/v3.1/region/africa'
response_africa = requests.get(url_africa)
africa_data = response_africa.json()

print("\nCountries in Africa:")
for country in africa_data:
    print(country['name']['common'] + ",", end = "")
