# RainTable
Lightweight PyQt6 application that displays weather information in tabular form, envisioned mainly for trip-planning purposes.

Its main features include:

* Add locations to the left-most column.
* Hover over a cell to see more details.

![Screenshot of RainTable app](./img/RainTable%20Example.PNG)

---

### Getting Started

1. Get API keys for the [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview) and for the [OpenWeatherMap API](https://openweathermap.org/api).

2. Clone the repository and create `credentials/creds.py`. Put your API keys in there as variables `geocoder_key` and `weather_key`.

3. Run `python app.py`. Make sure your Python version is 3 and you have PyQt as specificied in `requirements.txt`.

---

### Future Development

This is a quick tool I built for a trip because I want to see weather information in a table to plan my route.

Some future improvement ideas include:

* Save and load locations.
* More information displayed on hover or perhaps on sidebar when cell is clicked.
* Ability to move around and delete locations.
* Styling!

---

## About

*Version*: 0.1

*Last Updated*: August 19th, 2022