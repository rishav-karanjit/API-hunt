# API-hunt

## Screenshots of the results of each task.

#### Task 1: OpenWeatherMap API
![weatherForecast Screenshot](https://github.com/rishav-karanjit/API-hunt/blob/main/outputs/weatherForecast.png)

#### Task 2: Google Maps API

![Google maps Screenshot](https://github.com/rishav-karanjit/API-hunt/blob/main/outputs/GoogleMaps.png)

#### Task 3: REST Countries API

![REST Countries API Screenshot](https://github.com/rishav-karanjit/API-hunt/blob/main/outputs/RESTCountriesAPI.png)

#### Task 4: Currency Converter API

![Currency Converter API Screenshot](https://github.com/rishav-karanjit/API-hunt/blob/main/outputs/CurrencyConverterAPI.png)

## Code snippets used to interact with the APIs for each task

#### Task 1: OpenWeatherMap API

```
import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENWEATHERMAP_API_KEY')
city = 'Tokyo,jp'

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    forecast_data = response.json()
    print(json.dumps(forecast_data, indent=4))
else:
    print(f"Error fetching data from OpenWeatherMap API: Status Code {response.status_code}")
```
#### Task 2: Google Maps API
```
<!DOCTYPE html>
<html>
<head>
    <title>Two Google Maps Instances</title>
    <style>
        /* Set the size of the div elements that contain the maps */
        #nycMap, #routeMap {
            height: 300px;
            width: 100%;
        }
    </style>
</head>
<body>

<h3>Map Centered on New York City</h3>
<div id="nycMap"></div>

<h3>Route from San Francisco to Los Angeles</h3>
<div id="routeMap"></div>

<script>
function initMap() {
    // New York City latitude and longitude
    var nyc = {lat: 40.7128, lng: -74.0060};

    // Create the map centered on New York City
    var nycMap = new google.maps.Map(document.getElementById('nycMap'), {
        zoom: 10,
        center: nyc
    });

    // Set up the directions service and renderer for the route map
    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();

    // Create the route map without a center; it will re-center when the route is rendered
    var routeMap = new google.maps.Map(document.getElementById('routeMap'));

    // Apply the directions renderer to the map
    directionsRenderer.setMap(routeMap);

    // Calculate and display the route
    calculateAndDisplayRoute(directionsService, directionsRenderer);
}

function calculateAndDisplayRoute(directionsService, directionsRenderer) {
    directionsService.route(
        {
            origin: 'San Francisco, CA',
            destination: 'Los Angeles, CA',
            travelMode: 'DRIVING'
        },
        function(response, status) {
            if (status === 'OK') {
                directionsRenderer.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        }
    );
}

function loadScript() {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = `https://maps.googleapis.com/maps/api/js?key=PlaceholderKey&callback=initMap`;
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
}

window.onload = loadScript;
</script>

</body>
</html>

```
#### Task 3: REST Countries API
```
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

```
#### Task 4: Currency Converter API
```
import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('CURRENCY_CONVERTER')

# Function to convert currencies
def convert_currency(from_currency, to_currency, amount, api_key):
    url = f"https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    rate = data[f"{from_currency}_{to_currency}"]
    return rate * amount

# Convert 100 USD to EUR
amount_usd_to_eur = convert_currency('USD', 'EUR', 100, api_key)
print(f"100 USD is {amount_usd_to_eur} EUR")

# Convert 1000 JPY to GBP
amount_jpy_to_gbp = convert_currency('JPY', 'GBP', 1000, api_key)
print(f"1000 JPY is {amount_jpy_to_gbp} GBP")
```

## Self reflection on each API

**OpenWeatherMap API:**

OpenWeatherMap API offers a tremendous amount of weather data, which can be easily accessible through its endpoint. This was not my first time using this API, but I remember that during my first time, the documentation was challenging to navigate. Although it was a little difficult to navigate, when I reached a section I needed on the documentation, it was very clear. So, its documentation is well-written but not well-structured. The use of API was straightforward and simple. With the API endpoint, I could get current weather, forecasts, and historical data. I have used a lot of these data for my research works. This API could be used in various domains like agriculture, smart home systems, etc. The free tier offers a generous amount of calls, but for more extensive applications or commercial use, one might need to invest in a paid plan.

**Google Maps API:**

Google Maps API is a robust API for map-related services. I have used this before. This API's ease of use is little on the more challenging side. It was not easy to navigate on the console just to get the API keys. The website used to generate keys contains a variety of things that will make the timer very. However, the documentation was well written. The potential application of this API is vast. We can use this in any website and software. Some potential uses are showing property in real estate platforms, route optimization in delivery services, travel apps offering navigation functionality and so on. Compared to other APIs, students would be reluctant to use this API as we need to put our credit card info.

**REST Countries API:**

The REST Countries API is remarkably user-friendly, offering a free access to a wide array of data about countries. No API key is required, which simplifies the process of making requests. The information provided, such as country demographics, political structure, geographical data, and economic indicators, has various applications. It can serve educational platforms, demographic studies, global market analysis tools, or even as a backend utility for applications that need to validate or autofill country-related information. While it doesn't offer the complexity or depth of economic and demographic databases like the World Bank API, its simplicity and ease of access make it an excellent choice for straightforward country data retrieval tasks.

**Currency Converter API:**

The Currency Converter API is intuitive and requires minimal setup, which is advantageous for developers needing a quick integration for currency conversion. The API key process is straightforward, and the free tier's limitations are reasonable for smaller applications or development testing. However, it takes some days to get the API keys which is a negative factor of this API. The API can be a critical component for e-commerce platforms, financial apps, or any application that deals with international transactions and needs to provide real-time currency conversion. However, for production systems, especially in the financial sector, reliability and the accuracy of the data are paramount, so understanding the source and update frequency of the exchange rates is crucial.