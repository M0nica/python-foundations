

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
        print("shallow")
    elif 70 < depth < 300:
        print("intermediate")
    elif 300 < depth < 700:
        print("deep")

  # print("The earthquake had a depth of", earthquake['depth'])

depth_to_words(earthquake)


# magnitude_to_words will describe the earthquake's power

def magnitude_to_words(earthquake):
    mag = float(earthquake['mag'])
    if mag < 3.5:
        print("minor")
    elif 3.5 < mag < 7:
        print("moderate")
    elif mag == 7:
        print("major")
    elif 7 < mag < 9:
        print("huge")
    elif 9 < mag < 10:
        print("devastating")

 # print("The earthquake had a depth of", earthquake['rms'])
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
#print(parser.parse(earthquake['time']).weekday())
#print(parser.parse(earthquake['time']), parserinfo=weekday=True)
def day_in_words(earthquake):
    day = date.weekday()

    #print("the day is", day)
    if day == 6:
        print("Sunday")
    elif day == 0:
        print("Monday")
    elif day == 1:
        print("Tuesday")
    elif day == 2:
        # weekday = "Wednesday"
        print("Wednesday")
    elif day == 3:
        print("Thursday")
    elif day == 4:
        print("Friday")
    elif day == 5:
        print("Saturday")
    # return weekday

day_in_words(earthquake)

# "Wednesday"
#print(earth)


# time_in_words should be "morning", "afternoon", "evening" or "night"

def time_in_words(earthquake):

    time = date.hour
    if 5 < time < 12:
        print("morning")
    elif 12 < time < 17:
        print("afternoon")
    elif 17 < time < 20:
        print("evening")
    else:
        print("night")

time_in_words(earthquake)


# date_in_words should be "Monthname day", e.g. "June 22"
def date_in_words(earthquake):
    date_month = int(date.month)
    date_digits = date.day
    #print(date_ad)
    # print(date_words)
    months = {}
    digit = 1
    for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
        months[digit] = month
        digit = digit + 1

    print(months[date_month]+ " " + str(date_digits))


date_in_words(earthquake)

def eq_to_sentence(earthquake):
    depth = depth_to_words(earthquake)
    print("hello",depth)
    return(depth, magnitude_to_words(earthquake), earthquake['mag'])

eq_to_sentence(earthquake)
