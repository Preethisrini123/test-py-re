import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"

try:
    data = requests.get(url).json() 
    
    current = data["current_condition"][0]
    print(f"Current temperature: {current['temp_C']}°C")
    print(f"Humidity: {current['humidity']}%")
    print(f"Description: {current['weatherDesc'][0]['value']}")

except:
    print("Could not fetch weather data. Check the city name or your internet connection.")
