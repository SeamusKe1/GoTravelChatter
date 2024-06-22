# Import Flask, request, requests and render_template libraries
import requests
from flask import Flask, render_template, request

# Import chatbot libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# insert API key in following format: "API KEY"
API_key = ""

# Standard code block to run Flask.
app = Flask(__name__)

# chatbot training
my_bot = ChatBot(name="GoTravelBot",
                 read_only=True,
                 logic_adapters=[{
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I am not sure what you mean? Please ask me something like what is the temperature in Cumbria tomorrow?',
                     'maximum_similarity_threshold': 0.95,
                    }])

# basic chatbot greetings
small_talk = [
    'Hello',
    'How are you?',
    'I am well',
    'I am glad',
    'Thank you',
    'You are most welcome',
]

math_talk_1 = [
    'pythagorean theorem',
    'a squared plus b squared equals c squared'
]

math_talk_2 = [
    'law of cosines',
    'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)'
]

# chatbot training block
list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

# Import weather data from external txt file

training_data_weather = open('Data/Weatherdata.txt').read().splitlines()

list_trainer.train(training_data_weather)

# corpus chatbot training block
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')


# declare get requests for API calls
class GetRequests:
    def make_get_request(self, url):
        resp = requests.get(url=url)


# API URLS
urls = {'openweather': 'https://openweathermap.org/'}
my_get = GetRequests()
my_get.make_get_request(urls['openweather'])


# Define kelvin to celsius function for API JSON data interpretation
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


# app route for Home Page
@app.route("/")
def home():
    return render_template("index.html")


# app route for ChatBot
@app.route('/get', methods=["GET", "POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = my_bot.get_response(msg)
    return str(response)


# following app.routes are for other page locations in nav bar
@app.route('/cumbria')
def cumbria():
    return render_template("cumbria.html",
                           cumbria_celsius=temp_celsius1,
                           cumbria_feels_like=feels_like_celsius1,
                           cumbria_wind_speed=wind_speed1,
                           cumbria_humidity=humidity1,
                           cumbria_description=description1)


# API call URL
weather_url_Cumbria = "https://api.openweathermap.org/data/2.5/weather?lat=54.5000&lon=-3.2500" "&appid=" + API_key
resp1 = requests.get(weather_url_Cumbria).json()

# workings for populating API info received
temp_kelvin1 = resp1['main']['temp']
temp_celsius1 = round(kelvin_to_celsius(temp_kelvin1))
feels_like_kelvin1 = resp1['main']['feels_like']
feels_like_celsius1 = round(kelvin_to_celsius(feels_like_kelvin1))
wind_speed1 = resp1['wind']['speed']
humidity1 = resp1['main']['humidity']
description1 = resp1['weather'][0]['description']


@app.route('/corfe_castle')
def corfe_castle():
    return render_template("corfe_castle.html",
                           corfe_temperature=temp_celsius2,
                           corfe_feels_like=feels_like_celsius2,
                           corfe_wind_speed=wind_speed2,
                           corfe_humidity=humidity2,
                           corfe_description=description2)


weather_url_Corfe_Castle = "https://api.openweathermap.org/data/2.5/weather?lat=50.64&lon=-2.058" "&appid=" + API_key
resp2 = requests.get(weather_url_Corfe_Castle).json()

temp_kelvin2 = resp2['main']['temp']
temp_celsius2 = round(kelvin_to_celsius(temp_kelvin2))
feels_like_kelvin2 = resp2['main']['feels_like']
feels_like_celsius2 = round(kelvin_to_celsius(feels_like_kelvin2))
wind_speed2 = resp2['wind']['speed']
humidity2 = resp2['main']['humidity']
description2 = resp2['weather'][0]['description']


@app.route('/the_cotswolds')
def the_cotswolds():
    return render_template("the_cotswolds.html",
                           cotswold_temperature=temp_celsius3,
                           cotswold_feels_like=feels_like_celsius3,
                           cotswold_speed=wind_speed3,
                           cotswold_humidity=humidity3,
                           cotswold_description=description3)


weather_url_The_Cotswold = "https://api.openweathermap.org/data/2.5/weather?lat=51.7190&lon=-1.9680" "&appid=" + API_key
resp3 = requests.get(weather_url_The_Cotswold).json()

temp_kelvin3 = resp3['main']['temp']
temp_celsius3 = round(kelvin_to_celsius(temp_kelvin3))
feels_like_kelvin3 = resp3['main']['feels_like']
feels_like_celsius3 = round(kelvin_to_celsius(feels_like_kelvin3))
wind_speed3 = resp3['wind']['speed']
humidity3 = resp3['main']['humidity']
description3 = resp3['weather'][0]['description']


@app.route('/cambridge')
def cambridge():
    return render_template("cambridge.html",
                           cambridge_temperature=temp_celsius4,
                           cambridge_feels_like=feels_like_celsius4,
                           cambridge_speed=wind_speed4,
                           cambridge_humidity=humidity4,
                           cambridge_description=description4)


weather_url_Cambridge = "https://api.openweathermap.org/data/2.5/weather?lat=52.2000&lon=0.1167" "&appid=" + API_key
resp4 = requests.get(weather_url_Cambridge).json()

temp_kelvin4 = resp4['main']['temp']
temp_celsius4 = round(kelvin_to_celsius(temp_kelvin4))
feels_like_kelvin4 = resp4['main']['feels_like']
feels_like_celsius4 = round(kelvin_to_celsius(feels_like_kelvin4))
wind_speed4 = resp4['wind']['speed']
humidity4 = resp4['main']['humidity']
description4 = resp4['weather'][0]['description']


@app.route('/bristol')
def bristol():
    return render_template("bristol.html",
                           bristol_temperature=temp_celsius5,
                           bristol_feels_like=feels_like_celsius5,
                           bristol_speed=wind_speed5,
                           bristol_humidity=humidity5,
                           bristol_description=description5)


weather_url_Bristol = "https://api.openweathermap.org/data/2.5/weather?lat=51.4552&lon=-2.5967" "&appid=" + API_key
resp5 = requests.get(weather_url_Bristol).json()

temp_kelvin5 = resp5['main']['temp']
temp_celsius5 = round(kelvin_to_celsius(temp_kelvin5))
feels_like_kelvin5 = resp5['main']['feels_like']
feels_like_celsius5 = round(kelvin_to_celsius(feels_like_kelvin5))
wind_speed5 = resp5['wind']['speed']
humidity5 = resp5['main']['humidity']
description5 = resp5['weather'][0]['description']


@app.route('/oxford')
def oxford():
    return render_template("oxford.html",
                           oxford_temperature=temp_celsius6,
                           oxford_feels_like=feels_like_celsius6,
                           oxford_speed=wind_speed6,
                           oxford_humidity=humidity6,
                           oxford_description=description6)


weather_url_Oxford = "https://api.openweathermap.org/data/2.5/weather?lat=51.752022&lon=-1.257677" "&appid=" + API_key
resp6 = requests.get(weather_url_Oxford).json()

temp_kelvin6 = resp6['main']['temp']
temp_celsius6 = round(kelvin_to_celsius(temp_kelvin6))
feels_like_kelvin6 = resp6['main']['feels_like']
feels_like_celsius6 = round(kelvin_to_celsius(feels_like_kelvin6))
wind_speed6 = resp6['wind']['speed']
humidity6 = resp6['main']['humidity']
description6 = resp6['weather'][0]['description']


@app.route('/stonehenge')
def stonehenge():
    return render_template("stonehenge.html",
                           stonehenge_temperature=temp_celsius7,
                           stonehenge_feels_like=feels_like_celsius7,
                           stonehenge_speed=wind_speed7,
                           stonehenge_humidity=humidity7,
                           stonehenge_description=description7)


weather_url_Stonehenge = ("https://api.openweathermap.org/data/2.5/weather?lat=51.178844&lon=-1.826323" "&appid="
                          + API_key)
resp7 = requests.get(weather_url_Stonehenge).json()

temp_kelvin7 = resp7['main']['temp']
temp_celsius7 = round(kelvin_to_celsius(temp_kelvin7))
feels_like_kelvin7 = resp7['main']['feels_like']
feels_like_celsius7 = round(kelvin_to_celsius(feels_like_kelvin7))
wind_speed7 = resp7['wind']['speed']
humidity7 = resp7['main']['humidity']
description7 = resp7['weather'][0]['description']


@app.route('/norwich')
def norwich():
    return render_template("norwich.html",
                           norwich_temperature=temp_celsius8,
                           norwich_feels_like=feels_like_celsius8,
                           norwich_speed=wind_speed8,
                           norwich_humidity=humidity8,
                           norwich_description=description8)


weather_url_Norwich = "https://api.openweathermap.org/data/2.5/weather?lat=52.630886&lon=1.297355" "&appid=" + API_key
resp8 = requests.get(weather_url_Norwich).json()

temp_kelvin8 = resp8['main']['temp']
temp_celsius8 = round(kelvin_to_celsius(temp_kelvin8))
feels_like_kelvin8 = resp8['main']['feels_like']
feels_like_celsius8 = round(kelvin_to_celsius(feels_like_kelvin8))
wind_speed8 = resp8['wind']['speed']
humidity8 = resp8['main']['humidity']
description8 = resp8['weather'][0]['description']


@app.route('/watergate_bay')
def watergate_bay():
    return render_template("watergate_bay.html",
                           watergate_bay_temperature=temp_celsius9,
                           watergate_bay_feels_like=feels_like_celsius9,
                           watergate_bay_speed=wind_speed9,
                           watergate_bay_humidity=humidity9,
                           watergate_bay_description=description9)


weather_url_Watergate_bay = "https://api.openweathermap.org/data/2.5/weather?lat=50.44456&lon=-5.03987" "&appid=" + API_key
resp9 = requests.get(weather_url_Watergate_bay).json()

temp_kelvin9 = resp9['main']['temp']
temp_celsius9 = round(kelvin_to_celsius(temp_kelvin9))
feels_like_kelvin9 = resp9['main']['feels_like']
feels_like_celsius9 = round(kelvin_to_celsius(feels_like_kelvin9))
wind_speed9 = resp9['wind']['speed']
humidity9 = resp9['main']['humidity']
description9 = resp9['weather'][0]['description']


@app.route('/birmingham')
def birmingham():
    return render_template("birmingham.html",
                           birmingham_temperature=temp_celsius10,
                           birmingham_feels_like=feels_like_celsius10,
                           birmingham_speed=wind_speed10,
                           birmingham_humidity=humidity10,
                           birmingham_description=description10)


weather_url_Birmingham = ("https://api.openweathermap.org/data/2.5/weather?lat=52.489471&lon=-1.898575" "&appid="
                          + API_key)
resp10 = requests.get(weather_url_Birmingham).json()

temp_kelvin10 = resp10['main']['temp']
temp_celsius10 = round(kelvin_to_celsius(temp_kelvin10))
feels_like_kelvin10 = resp10['main']['feels_like']
feels_like_celsius10 = round(kelvin_to_celsius(feels_like_kelvin10))
wind_speed10 = resp10['wind']['speed']
humidity10 = resp10['main']['humidity']
description10 = resp10['weather'][0]['description']

# run app block
if __name__ == "__main__":
    app.run()
