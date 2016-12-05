# TwitterMining

A python program used to mine twitter for hashtags relating to either the 2016 presidential election or generic illness

# miningAppSetup.bat

A batch file that sets the proper parameters to mine tweets, run this first when deploying.

# miningApp3_0.py

This is the program that does the meat of the work. To deploy, add in the user's twitter credentials on lines 41-44.

# jsonToGeoJsonIllness.py

This program simply converts the JSON files to GeoJSON

# jsonToGeoJsonElection.py

This program also converts JSON to GeoJSON format and gives the GeoJSON objects an entity called 'alignment' that indicates if the tweet is pro-Trump, pro-Clinton or neutral based on the hashtags within the tweets
