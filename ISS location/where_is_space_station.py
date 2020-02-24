import json
import urllib.request
import turtle
import time
from datetime import datetime

url_people_in_space = 'http://api.open-notify.org/astros.json'
url_response_people_in_space = urllib.request.urlopen(url_people_in_space)
result_url_response_people_in_space = json.loads(url_response_people_in_space.read())

print('Currently onboard ISS : \n', str(result_url_response_people_in_space["people"][0]["name"]), '\n', str(result_url_response_people_in_space["people"][1]["name"]), '\n', result_url_response_people_in_space["people"][2]["name"])

url_iss_position = 'http://api.open-notify.org/iss-now.json'
url_response_iss_position = urllib.request.urlopen(url_iss_position)
result_iss_position = json.loads(url_response_iss_position.read())
timestamp_to_int = int(result_iss_position["timestamp"])
readable_date_and_time = datetime.utcfromtimestamp(timestamp_to_int).strftime('%Y-%m-%d %H:%M:%S')

print('Current location : ', '\n' , 'Longitude : ', result_iss_position['iss_position']['longitude'], '\n' , 'Latitude : ', result_iss_position['iss_position']['latitude'],'\n','Time : ', readable_date_and_time)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.register_shape('iss.gif')
screen.bgpic('map.gif')

iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()

iss.goto(float(result_iss_position['iss_position']['longitude']), float(result_iss_position['iss_position']['latitude']))
turtle.Screen().exitonclick()

#Displaying ISS on map solved using : https://projects.raspberrypi.org/en/projects/where-is-the-space-station