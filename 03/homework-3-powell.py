# Monica Powell
# May, 29th, 2016
# Homework 3

countries = ["Jamaica", "Barbados", "Trinidad", "Haiti", "Virgin Islands", "St. Lucia", "Antigua"]

for country in countries:
    print(country)


countries.sort()

print(countries[0])
print(countries[-2])

# http://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value-in-python
countries.remove("Haiti")

for country in countries:
    print(country)

tree = {'name': 'Old Tjikko', 'species': 'Norway Spruce', 'age': 9550, 'location_name':'Sweden', 'latitude': 60.1282, 'longitude': 18.6435}

print(tree['name'], "is a", tree['age'], " year old tree that is in", tree['location_name'])

newyork ={'latitude':40.7128, 'longitude':-74.0059}

if tree['latitude'] < newyork['latitude']:
    print("The tree", tree['name'], "in", tree['location_name'], "is South of NYC")
else:
    print("The tree", tree['name'], "in", tree['location_name'], "is North of NYC")

user_age = input("How old are you?")
user_age = int(user_age)
if user_age > tree['age']:
    print('You are',tree['age'],'years older than',tree['name'])
else:
    print(tree['name'], "was", (tree['age'] - user_age), "years old when you were born.")


# Store the latitude and longitude without the N/S/E/W - if the latitude is
# S, make it negative. If the longitude is W, make it negative. See here for explanation:
# https://answers.yahoo.com/question/index?qid=3D20080211182008AAMdUe8



places = [
{"name": "Moscow", "latitude": 55.7558,"longitude": 37.6173},
{"name": "Tehran", "latitude": 35.6892,"longitude":51.3890},
{"name":"Falkland Islands","latitude": -51.7963,"longitude":59.5236 },
{"name":"Seoul","latitude": 37.5665,"longitude": 126.978},
{"name":"Santiago","latitude": -33.4489,"longitude":-70.6693}
]

for city in places:
    print(city['name'])
    if city['latitude'] > 0:
        print(city['name'],"is above the equator")
    elif city['latitude'] < 0:
        print(city['name'],"is below the equator")
    if(city['name']) == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")

for city in places:
    if city['latitude'] > tree['latitude']:
        print(city['name'], "is North of", tree['name'])
    elif city['latitude'] < tree['latitude']:
        print(city['name'], "is South of", tree['name'])
