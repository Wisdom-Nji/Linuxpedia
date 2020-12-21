#!/bin/python

import json

# list of keywords is to config paths 
# mouse, touchpad, scrolling -> /etc/<>

def search( keyword, os, dictionary ):
    for key in dictionary:
        keywords = key.split( '|' )
        if keyword in keywords:
            for details in dictionary[key]:
                if details['os'] == os:
                    print( "filepath:", details['filepath'] )
                    print( "instruction:", details['instructions'] )
                    print()

dictionaryFilename = "dictionary.json"
jsonFile = open( dictionaryFilename )
configDictionary = json.load( jsonFile )

# searchTerm = "click"
# os = "manjaro"

searchTerm = "wallpaper"
os = "manjaro"
search( searchTerm, os, configDictionary )
