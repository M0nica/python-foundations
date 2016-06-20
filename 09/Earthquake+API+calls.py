

earthquake = {
      'rms': '1.85',
      'updated': '2014-06-11T05:22:21.596Z',
      'type': 'earthquake',
      'magType': 'mwp',
      'longitude': '-136.6561',
      'gap': '48',
      'depth': '10',
      'dmin': '0.811',
      'mag': '5.7',
      'time': '2014-06-04T11:58:58.200Z',
      'latitude': '59.0001',
      'place': '73km WSW of Haines, Alaska',
      'net': 'us',
      'nst': '',
      'id': 'usc000rauc'}


# depth_to_words will describe the earthquake's depth

# Shallow earthquakes are between 0 and 70 km deep;
#intermediate earthquakes, 70 - 300 km deep;
#and deep earthquakes, 300 - 700 km deep.

def depth_to_words(earthquake):
    depth = int(earthquake['depth'])
    if depth < 70:
        return("shallow")
    elif 70 < depth < 300:
        return("intermediate")
    elif 300 < depth < 700:
        return("deep")

  # return("The earthquake had a depth of", earthquake['depth'])

depth_to_words(earthquake)


# magnitude_to_words will describe the earthquake's power

def magnitude_to_words(earthquake):
    mag = float(earthquake['mag'])
    if mag < 3.5:
        return("minor")
    elif 3.5 < mag < 7:
        return("moderate")
    elif mag == 7:
        return("major")
    elif 7 < mag < 9:
        return("huge")
    elif 9 < mag < 10:
        return("devastating")

 # return("The earthquake had a depth of", earthquake['rms'])
magnitude_to_words(earthquake)

import dateutil.parser
# should refactor using: http://strftime.net/ instead of custom methods to calculate
# day of the week and month string
timestring = '2014-06-01T11:58:58.200Z'
yourdate = dateutil.parser.parse(timestring)
print("The hour is", yourdate.hour)
print("We can do things with strftime like", yourdate.strftime("%Y %b %d"))

# day_in_words should be the day of the week


date = dateutil.parser.parse(earthquake['time'])


# from dateutil import parser
#return(parser.parse(earthquake['time']).weekday())
#return(parser.parse(earthquake['time']), parserinfo=weekday=True)
def day_in_words(earthquake):
    day = date.weekday()

    #return("the day is", day)
    if day == 6:
        return("Sunday")
    elif day == 0:
        return("Monday")
    elif day == 1:
        return("Tuesday")
    elif day == 2:
        # weekday = "Wednesday"
        return("Wednesday")
    elif day == 3:
        return("Thursday")
    elif day == 4:
        return("Friday")
    elif day == 5:
        return("Saturday")
    # return weekday

day_in_words(earthquake)

# "Wednesday"
#return(earth)


# time_in_words should be "morning", "afternoon", "evening" or "night"

def time_in_words(earthquake):

    time = date.hour
    if 5 < time < 12:
        return("morning")
    elif 12 < time < 17:
        return("afternoon")
    elif 17 < time < 20:
        return("evening")
    else:
        return("night")

time_in_words(earthquake)


# date_in_words should be "Monthname day", e.g. "June 22"
def date_in_words(earthquake):
    date_month = int(date.month)
    date_digits = date.day
    #return(date_ad)
    # return(date_words)
    months = {}
    digit = 1
    for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
        months[digit] = month
        digit = digit + 1

    return(months[date_month]+ " " + str(date_digits))


date_in_words(earthquake)

def eq_to_sentence(earthquake):
    depth = depth_to_words(earthquake)
    # return("hello", depth)
    return("A " + depth + " " + earthquake['mag']+ ", " +magnitude_to_words(earthquake) + " earthquake was reported on " + day_in_words(earthquake) + " " + date_in_words(earthquake) + " of " + earthquake['place'])

print(eq_to_sentence(earthquake))
