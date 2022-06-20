import json

#%% json

s = '''{"coord":{"lon":4.3833,"lat":51.9167},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"base":"stations","main":{"temp":15.64,"feels_like":14.98,"temp_min":14.4,"temp_max":17.76,"pressure":1014,"humidity":66},"visibility":10000,"wind":{"speed":5.66,"deg":280},"clouds":{"all":40},"dt":1654092745,"sys":{"type":1,"id":1541,"country":"NL","sunrise":1654054148,"sunset":1654113106},"timezone":7200,"id":2747595,"name":"Gemeente Schiedam","cod":200}'''

r = json.loads(s)

temperature = r['main']['temp']
