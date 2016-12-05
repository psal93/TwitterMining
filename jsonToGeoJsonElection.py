#Name: jsonToGeoJson
#Author: Patrick Salembier
import json
import io
import re
import string
#function to determine if tweet is pro-trump, pro-hillary or neutral
def parseAndSort(str):
    track=['#election2016','#Election2016','#trump','#Trump','#hillary','#Hillary','#democrat','#Democrat','#republican','#Republican','#voteyourconscience',
           '#donaldtrump','#donaldTrump','#DonaldTrump','#Donaldtrump','#hillaryclinton','#hillaryClinton','#HillaryClinton','#Hillaryclinton','#imwithher','#ImWithHer',
           '#makeamericagreatagain','#MakeAmericaGreatAgain','#fuckhillary','#fucktrump','#nevertrump','#neverhillary','#imnotwithher','#ImNotWithHer','#president','#3rdparty','#election',
           '#Election','#conservative','#Conservative','#liberal','#Liberal','#hillary2016','#Hillary2016','#trump2016','#Trump2016','#donaldTrump2016','#hillaryClinton2016','#hillaryforprison2016',
           '#dumptrump','#libertarian','#Libertarian','#POTUS','#votetrump','#voteTrump','#VoteTrump','#VoteDonaldTrump','#TRUMP','#Benghazi','#clinton','#Clinton','#voteHillary','#VoteHillary',
           '#votehillary','#voteclinton','#Voteclinton','#voteClinton','#VoteClinton','#voterepublican','#voteRepublican','#VoteRepublican','#Voterepublican','#votedemocrat','#voteDemocrat',
           '#VoteDemocrat','#Votedemocrat','#democracy','#lockherup','#getoutandvote','#drumpf','#ElectionDay','#Vote2016']
    trumpTags = ['#trump','#Trump', '#republican', '#Republican','#donaldtrump','#donaldTrump','#DonaldTrump','#Donaldtrump','#makeamericagreatagain','#MakeAmericaGreatAgain',
                   '#fuckhillary','#neverhillary','#imnotwithher','#ImNotWithHer','#conservative','#Conservative','#trump2016','#Trump2016','#donaldTrump2016','#hillaryforprison2016',
                   '#votetrump','#voteTrump','#VoteTrump','#VoteDonaldTrump','#TRUMP','#Benghazi','#voterepublican','#voteRepublican','#VoteRepublican','#Voterepublican','#lockherup']
    clintonTags = ['#hillary','#Hillary','#democrat','#Democrat','#hillaryclinton','#hillaryClinton','#HillaryClinton','#Hillaryclinton','#imwithher',
                     '#ImWithHer','#Imwithher','#fucktrump','#nevertrump','#liberal','#Liberal','#hillary2016','#Hillary2016','#hillaryClinton2016','#HillaryClinton2016','#dumptrump','#clinton','#Clinton','#voteHillary',
                     '#VoteHillary','#votehillary','#voteclinton','#Voteclinton','#voteClinton','#VoteClinton','#votedemocrat','#voteDemocrat','#VoteDemocrat','#Votedemocrat','#drumpf']
    neitherTags = ['#election2016','#Election2016','#voteyourconscience','#president','#3rdparty','#elecion','#Election','#libertarian','#Libertarian','#POTUS','#democracy','#getoutandvote','#ElectionDay','#Vote2016','#teamhillary']

    tokenizedTweet = []
    # filter for printable characters then
    a= str
    a = ''.join(filter(lambda x: x in string.printable, a))

    for tweet in a.split(' '):
        if tweet.startswith('#'):
            tokenizedTweet.append(tweet.strip(',.?!'))

    trumpTweet = set(tokenizedTweet) & set(trumpTags)
    clintonTweet = set(tokenizedTweet) & set(clintonTags)
    neitherTweet = set(tokenizedTweet) & set(neitherTags)
    if(trumpTweet):
        return 1
    if(clintonTweet):
        return 2
    return 0


# Tweets are stored in "fname"
tweetsFile = 'C:\Users\Patrick\Documents\GEOG428\development\ElectionData.json'
neutralTweets = 0
proTrumpTweets = 0
proClintonTweets = 0
with open(tweetsFile, 'r') as f:
    geoData = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        alignment = 0
        tweet = json.loads(line)
        
        if tweet['text']:
            tweetText = tweet['text']
            alignment = parseAndSort(tweetText)
            if alignment == 0:
                neutralTweets = neutralTweets + 1
            elif alignment == 1:
                proTrumpTweets = proTrumpTweets + 1
            elif alignment == 2:
                proClintonTweets = proClintonTweets + 1
        if tweet['coordinates']:
            geoJsonFeature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at'],
                    "alignment": alignment
                }
            }
            geoData['features'].append(geoJsonFeature)

#Print out number of each kind of tweet
print "Neutral Tweets: " + str(neutralTweets)
print "Pro-Trump Tweets: " + str(proTrumpTweets)
print "Pro-Clinton Tweets: " + str(proClintonTweets)

# Save geo data
with open('Election_geo_data.json', 'w') as fout:
    fout.write(json.dumps(geoData, indent=4))
