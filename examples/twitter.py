from atlas import api
from collections import defaultdict
from pprint import pprint

twithot = api.playlists(uri="http://ref.atlasapi.org/hotness/twitter")
twititems = twithot['playlists'][0]['items'] + twithot['playlists'][0]['playlists']

coll = defaultdict(dict)
for i in twititems:
    coll[i['publisher']['name']][i['title']] = i['uri']

pprint(dict(coll))
