artist_name = input("What artist would you like to look up?")
# print ("Hello," + artist_name)


import requests


response = requests.get('https://api.spotify.com/v1/search?query='+ artist_name +'&type=artist&limit=50&market=US&offset=50')
response = response.json()
#print(smallresponse)
#
#print(smallresponse['artists']['items'])

artists = response['artists']['items']
counter = 0

if len(artists) == 0:
    print("No artists exist with that name.")
    artist_name = input("Try again. Please tell me which artist would you like to look up?")
    response = requests.get('https://api.spotify.com/v1/search?query='+ artist_name +'&type=artist&limit=50&market=US&offset=50')
    response = response.json()
    artists = response['artists']['items']

for artist in artists:
    counter = counter + 1
    print(counter, artist['name'])

# print(artists[0]['name'])

artist_num = input("What number is associated with the artist you are interested in?")
artist_of_interest = artists[int(artist_num) - 1]['name']
#print("Are you interested in",artist_of_interest , "?")

artist_of_interest_id = artists[int(artist_num)-1]['id']


#il_wayne_id = '55Aa2cqylxrFIXC767Z865'

top_tracks_response = requests.get('https://api.spotify.com/v1/artists/'+ artist_of_interest_id+'/top-tracks?country=US')
toptracksdata = top_tracks_response.json()

toptracks = toptracksdata['tracks']
print("The top tracks by", artist_of_interest, "are:")
for track in toptracks:
    print(track['name'])


albumsresponse = requests.get('https://api.spotify.com/v1/artists/' + artist_of_interest_id + '/albums')
album_data = albumsresponse.json()
albulms = album_data['items']

if len(albulms) > 1:
    most_pop = 0
    least_pop = 100
    for albulm in albulms:
        print("albulm name:", albulm['name'])
        popresponse = requests.get('https://api.spotify.com/v1/albums/' + albulm['id'])
        pop_data = popresponse.json()
        pop = pop_data['popularity']
        if pop > most_pop:
            most_pop = pop
            popular_albulm = albulm['name']
        if pop < least_pop:
            least_pop = pop
            least_albulm = albulm['name']
        print(albulm['name'], "has a popularity of", pop)
    print("Their most popular albulm is", popular_albulm, "and their least popular albulm is", least_albulm)

        #albulm['id']
else: print("This artist only has one albulm.")



# smallresponse = requests.get('https://api.spotify.com/v1/search?query=lil&type=artist&limit=50&market=US&offset=50')
# smallresponse = smallresponse.json()
# print(smallresponse)


#testing testing testing#
