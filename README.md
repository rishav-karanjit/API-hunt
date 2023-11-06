# API-hunt

## Screenshots of the results of each task.

#### Task 1: OpenWeatherMap API
![weatherForecast Screenshot](https://github.com/rishav-karanjit/API-hunt/blob/main/outputs/weatherForecast.png)

#### Task 2: Google Maps API

![Google maps Screenshot](https://github.com/rishav-karanjit/API-hunt/blob/main/outputs/GoogleMaps.png)

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