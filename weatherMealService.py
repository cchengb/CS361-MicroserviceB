from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Replace with your actual API key from a weather service like OpenWeatherMap
API_KEY = "5d9fc7196273dddd13a428000b50db49"
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data from the weather API."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()
    return data

def suggest_meals(weather):
    """Suggest meals based on the weather condition."""
    if weather in ['Rain', 'Drizzle']:
        return ["Hot soup", "Tea and Samosas"]
    elif weather == 'Snow':
        return ["Hot Chocolate", "Stew"]
    elif weather == 'Sunny':
        return ["Salad", "Grilled chicken"]
    elif weather == 'Clouds':
        return ["Chowder", "Baked potatoes"]
    elif weather == 'Windy':
        return ["Mac and cheese", "Pot roast"]
    elif weather == 'Humid':
        return ["Gazpacho", "Sushi"]
    elif weather == 'Foggy':
        return ["Clam chowder", "Risotto"]
    elif weather == 'Stormy':
        return ["Jambalaya", "Chili"]
    elif weather == 'Extreme Heat':
        return ["Cold noodle salad", "Gazpacho"]
    elif weather == 'Extreme Cold':
        return ["Beef stew", "Pea soup"]
    else:
        return ["Pasta", "Pizza"]

def suggest_snacks(weather):
    """Suggest snacks based on the weather condition."""
    if weather in ['Rain', 'Drizzle']:
        return ["Hot pakoras", "Coffee"]
    elif weather == 'Snow':
        return ["Marshmallows", "Warm brownies"]
    elif weather == 'Sunny':
        return ["Ice cream", "Fruit salad"]
    elif weather == 'Clouds':
        return ["Pretzels", "Hot cocoa"]
    elif weather == 'Windy':
        return ["Popcorn", "Trail mix"]
    elif weather == 'Humid':
        return ["Smoothies", "Yogurt"]
    elif weather == 'Foggy':
        return ["Steam buns", "Hot tea"]
    elif weather == 'Stormy':
        return ["Nachos", "Hot chocolate"]
    elif weather == 'Extreme Heat':
        return ["Frozen grapes", "Watermelon slices"]
    elif weather == 'Extreme Cold':
        return ["Gingerbread cookies", "Hot cider"]
    else:
        return ["Chips", "Dip"]


@app.route('/meal_suggestions', methods=['GET'])
def meal_suggestions():
    city = request.args.get('city', 'London')  # Default to London if no city provided
    weather_data = get_weather(city)
    weather_condition = weather_data.get('weather', [{}])[0].get('main', 'Clear')
    meals = suggest_meals(weather_condition)
    return jsonify({
        'weather': weather_condition,
        'meals': meals
    })

@app.route('/snack_suggestions', methods=['GET'])
def snack_suggestions():
    city = request.args.get('city', 'London')  # Default to London if no city provided
    weather_data = get_weather(city)
    weather_condition = weather_data.get('weather', [{}])[0].get('main', 'Clear')
    snacks = suggest_snacks(weather_condition)
    return jsonify({
        'weather': weather_condition,
        'snacks': snacks
    })

if __name__ == '__main__':
    app.run(debug=True, port=3000)
