#Name: jsonToGeoJsonIllness
#Author: Patrick Salembier
import json
import io
import re
import string

# Tweets are stored in "fname"
tweetsFile = 'Z:\Geog428Project\development\data.json'
with open(tweetsFile, 'r') as f:
    geoData = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        alignment = 0
        tweet = json.loads(line)
        if tweet['coordinates']:
            geoJsonFeature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geoData['features'].append(geoJsonFeature)

# Save geo data
with open('Illness_geo_data.json', 'w') as fout:
    fout.write(json.dumps(geoData, indent=4))
