import requests
import urllib
import json
import time
import datetime, time
from pytz import timezone
import pytz

def GetJSON(lat, lon, epoch, outputFileName):
    url = "https://ms.sc-jpl.com/web/getPlaylist"
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'cache-control': 'no-cache',
        'content-length': '215',
        'content-type': 'application/json',
        'origin': 'https://map.snapchat.com',
        'pragma': 'no-cache',
        'referer': 'https://map.snapchat.com/@51.536538,-0.093255,12.15z',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

    }

    payload = {"requestGeoPoint":{"lat":lat,"lon":lon},"zoomLevel":15.340000000000007,"tileSetId":{"flavor":"default","epoch":epoch,"type":"HEAT"},"radiusMeters":104.4498920486594,"maximumFuzzRadius":0}

    r = requests.post(url, json=payload, headers=headers)

    print url
    print headers
    print payload
    print r
    print str(time.strftime("%Y%m%d-%H%M%S"))
    data =  r.content

    parsed = json.loads(data)

    text_file = open(outputFileName, "w")
    text_file.write(json.dumps(parsed, indent=4, sort_keys=True))
    text_file.close()
