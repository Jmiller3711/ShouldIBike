

def get_message(weather):
    return '\nShould I Bike says: ' + build_message(weather) + '\n' + get_summary(weather) + '\n' + get_error(weather)


def build_message(weather):
    if web_scraping_error(weather):
        return 'There was an error'

    if temp_is_okay(weather) and rain_is_okay(weather):
        return 'Go for it!'
    elif not temp_is_okay(weather) and rain_is_okay(weather):
        return 'Too cold to bike today'
    elif temp_is_okay(weather) and not rain_is_okay(weather):
        return 'Too rainy to bike today'
    else:
        return 'Too cold and wet to bike today'


def temp_is_okay(weather):
    to_work_temp = float(weather.to_work_temp)
    from_work_temp = float(weather.from_work_temp)
    if to_work_temp >= 60 and from_work_temp >= 60:
        return True
    else:
        return False


def rain_is_okay(weather):
    to_work_precip = float(weather.to_work_precip)
    from_work_precip = float(weather.from_work_precip)
    if to_work_precip < 30 and from_work_precip < 30:
        return True
    else:
        return False


def get_summary(weather):
    return str(weather.to_work_time) + '; temp = ' + str(weather.to_work_temp) + ' F; precip = ' + str(weather.to_work_precip) + ' %\n' + str(weather.from_work_time) + '; temp = ' + str(weather.from_work_temp) + ' F; precip = ' + str(weather.from_work_precip) + ' %'


def web_scraping_error(weather):
    if len(weather.web_scraping_error) > 0:
        return True
    else:
        return False

def get_error(weather):
    if len(weather.web_scraping_error) > 0:
        return 'Error: ' + str(weather.web_scraping_error)
    else:
        return ''