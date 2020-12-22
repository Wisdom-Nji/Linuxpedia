#!/bin/python

import json

# list of keywords is to config paths 
# mouse, touchpad, scrolling -> /etc/<>

def reading( details, keyword ):
        print(f"[ type: reading | keyword: {keyword} ]")
        print("Link:", details["info_link"])
        print()

def config( details, keyword ):
        print(f"[ type: reading | keyword: {keyword} ]")
        print( "Filepath:", details['filepath'] )
        print( "Instruction:", details['instructions'] )
        print()

def search( keyword, os, dictionary ):
    typesDictionary = {
            "reading" : reading,
            "config" : config
    }
    for key in dictionary:
        keywords = key.split( '|' )
        if keyword in keywords:
            for details in dictionary[key]:
                if details["type"] == "reading":
                    typesDictionary["reading"]( details, keyword )

                elif details["type"] == "config" and details["os"] == os:
                    typesDictionary["config"]( details, keyword)

dictionaryFilename = "dictionary.json"
jsonFile = open( dictionaryFilename )
configDictionary = json.load( jsonFile )

# searchTerm = "click"
# os = "manjaro"

searchTerm = "wallpaper"
os = "manjaro"
search( searchTerm, os, configDictionary )
