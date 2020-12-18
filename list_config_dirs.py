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
                    print( details['filepath'] )


dictionaryFilename = "dictionary.json"
jsonFile = open( dictionaryFilename )
configDictionary = json.load( jsonFile )

searchTerm = "click"
os = "manjaro"
search( searchTerm, os, configDictionary )
