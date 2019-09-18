import requests
from bs4 import BeautifulSoup


class Weather:
    """The current weather at different times from weather.com. The times passed in (to_work_time & from_work_time)
    are the times which I commute to and from work, these times are used when webscraping in method get_weather. """

    def __init__(self, to_work_time, from_work_time):
        self.to_work_time = to_work_time
        self.from_work_time = from_work_time
        self.to_work_temp = 'error'
        self.to_work_precip = 'error'
        self.from_work_temp = 'error'
        self.from_work_precip = 'error'
        self.web_scraping_error = ''

    def get_weather(self):
        """scrapes weather.com for temp and precipitation values"""
        # Web Scraping with BeautifulSoup
        try:
            r = requests.get(
                'https://weather.com/weather/hourbyhour/l/0ae5212032c6ef6ebb8d0660e1f09218a2e8d973e6145ae120ece05198e1731c')
            soup = BeautifulSoup(r.text, 'html.parser')

            table = soup.find('table', attrs={'class': 'twc-table'})
            tbody = table.find('tbody')
            rows = tbody.findChildren('tr')

            for row in rows:
                time_td = row.find('td', attrs={'headers': 'time'})
                time = time_td.find('span', attrs={'class': 'dsx-date'})
                if time.contents[0] == self.to_work_time:
                    temp_td = row.find('td', attrs={'headers': 'temp'})
                    self.to_work_temp = temp_td.find('span').contents[0]
                    precip_td = row.find('td', attrs={'headers': 'precip'})
                    precip_span = precip_td.find('span', attrs={'class': ''})
                    self.to_work_precip = precip_span.find('span').contents[0]
                if time.contents[0] == self.from_work_time:
                    temp_td = row.find('td', attrs={'headers': 'temp'})
                    self.from_work_temp = temp_td.find('span').contents[0]
                    precip_td = row.find('td', attrs={'headers': 'precip'})
                    precip_span = precip_td.find('span', attrs={'class': ''})
                    self.from_work_precip = precip_span.find('span').contents[0]
        except:
            self.web_scraping_error = 'There was an error web scraping'

# API https://home.openweathermap.org/ zipcode = '64110' res = requests.get(
# 'http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',us&appid=cc20c5db9cf0050f5c2ca2080a340da3')
# json_object = res.json() temp_current_f = convert_k_to_f(float(json_object['main']['temp'])) temp_min_f =
# convert_k_to_f(float(json_object['main']['temp_min'])) temp_max_f = convert_k_to_f(float(json_object['main'][
# 'temp_max'])) print(json_object) print('Current temp (F) = ' + str(temp_current_f)) print('Min temp (F) = ' + str(
# temp_min_f)) print('Max temp (F) = ' + str(temp_max_f))
