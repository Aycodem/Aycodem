from calendar import week
import requests
import pandas as pd
from bs4 import BeautifulSoup

page=requests.get("https://forecast.weather.gov/MapClick.php?lat=34.052230000000066&lon=-118.24367999999998#.Yx3w9GzMIdU")

soup=BeautifulSoup(page.content,"html.parser")
# print(soup.findAll("a"))

weeks =soup.find(id="seven-day-forecast-body")

# print(weeks)
items=weeks.find_all(class_='tombstone-container')

# print(items[0])

# print(items[0].find(class_="period-name").get_text())
# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

peroid_name=[item.find(class_="period-name").get_text() for item in items ]

short_description=[item.find(class_="short-desc").get_text() for item in items ]
temperatures=[item.find(class_="temp").get_text() for item in items ]


# print(peroid_name)
# print(short_description)
# print(temperatures)

weather_stuff=pd.DataFrame(
    {"period":peroid_name,
    "short desc":short_description,
    "temperatures":temperatures
    }

)

print(weather_stuff)


# weather_stuff.to_csv("weather.csv")

