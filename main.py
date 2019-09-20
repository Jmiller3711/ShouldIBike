from weather import Weather
from message_builder import get_message
from text_message import text_myself

# get weather info
weather = Weather('7:00 am', '2:00 pm')
weather.get_weather()

# build message
message = get_message(weather)
print(message)

# send text
text_myself(message)