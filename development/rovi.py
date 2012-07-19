#! /usr/bin/python

from encodings import hex_codec
from encodings import ascii
import httplib
import urllib2
import json
import sys
import datetime
import rovi_auth

sig = rovi_auth.sign()
rovi_key = rovi_auth.apikey()

# getting user input
if len(sys.argv) < 2:
    sys.exit(2)

search = sys.argv[1]

#Getting artist info from Rovi
url = "http://api.rovicorp.com/data/v1/name/info?name=%s&duration=10080&inprogress=true&country=US&language=en&format=json&apikey=%s&sig=%s" % (search,rovi_key,sig)
json = urllib2.urlopen(url).read()

# convert to a native python object
(true,false,null) = (True,False,None)
rovi_data = eval(json)

now = datetime.datetime.now()

#Retrieving artist info from the payload
artist_name = rovi_data ['name']['name']
artist_birth = rovi_data ['name']['birth']['date']
artist_birth_year = int(artist_birth.split ('-')[0])
artist_age = now.year - artist_birth_year

#Printing stuff
print "%s was born on: %s" % (artist_name, artist_birth)
print "%s is: %s years old" % (artist_name, artist_age)