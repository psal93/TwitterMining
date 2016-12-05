#Name: miningApp3_0.py
#Author: Patrick Salembier
import io, json
import pandas as pd
import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import time
import sys

#Basic listener that print received tweets stout
class MyListener(StreamListener):

    def on_data(self, data):
        #loading tweet for examination
        json_data = json.loads(data)
        #checking that the tweet has a coordinates field, if not then return true
        if not json_data.get("coordinates"):
            return True

        #loading the coordinates into a variable
        coords = json_data["coordinates"]
        print coords

        #making sure the coordinates field is not null
        if coords is not None:
            print('Got some coords, yo!')
            try:
                with open('ElectionData.json', 'a') as f:
                    f.write(data)
                    return True
            except BaseException as e:
                    print('Shit, BaseException error')
                    return True
        else:
            print "No coords here"
    def on_error(self, status):
        print status
        return True

#Setting up access
consumer_key = 'Your key here'
consumer_secret = 'Your secret here'
access_token = 'Your token here'
access_secret = 'Your secret here'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
#setting api
api = tweepy.API(auth)
#setting stream
stream = Stream(auth, MyListener())
while True:
    try:

        #starting streaming for all tweets with certain filters
        #stream.filter(track=['#bringmesoup','colds','Colds','#sniffles','#Sniffles','sniffles','Sniffles','#sorethroat','#SoreThroat','#nyquil','#NyQuil','#Nyquil','#Buckleys','#buckleys','#BringMeSoup','#sickday','#SickDay','#coldssuck','#ColdsSuck','#feellikedeath','#FeelLikeDeath','#flu','#Iamsick','#IAmSick','#IamSick','#ihatebeingsick','#IHateBeingSick','#ifeeldead','#IFeelDead','#theflu','#TheFlu','#iamsick','#IAmSick','#hopeifeelbettersoon','#HopeIFeelBetterSoon','#hatebeingsick','#HateBeingSick','#colds','#Colds'])
        stream.filter(track=['#election2016','#Election2016','#trump','#Trump','#hillary','#Hillary','#democrat','#Democrat','#republican','#Republican','#voteyourconscience','#donaldtrump','#donaldTrump','#DonaldTrump','#Donaldtrump','#hillaryclinton','#hillaryClinton','#HillaryClinton','#Hillaryclinton','#imwithher','#ImWithHer','#makeamericagreatagain','#MakeAmericaGreatAgain','#fuckhillary','#fucktrump','#nevertrump','#neverhillary','#imnotwithher','#ImNotWithHer','#president','#3rdparty','#election','#Election','#conservative','#Conservative','#liberal','#Liberal','#hillary2016','#Hillary2016','#trump2016','#Trump2016','#donaldTrump2016','#hillaryClinton2016','#hillaryforprison2016','#dumptrump','#libertarian','#Libertarian','#POTUS','#votetrump','#voteTrump','#VoteTrump','#VoteDonaldTrump','#TRUMP','#Benghazi','#clinton','#Clinton','#voteHillary','#VoteHillary','#votehillary','#voteclinton','#Voteclinton','#voteClinton','#VoteClinton','#voterepublican','#voteRepublican','#VoteRepublican','#Voterepublican','#votedemocrat','#voteDemocrat','#VoteDemocrat','#Votedemocrat','#democracy','#lockherup','#getoutandvote','#drumpf','#ElectionDay','#Vote2016'])
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        break
    except:
        print "Unexpected error:", sys.exc_info()[0]
        time.sleep(180)
        continue
