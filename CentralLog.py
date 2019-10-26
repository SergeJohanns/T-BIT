#!/usr/bin/env python3

import json

personalityCoresDir = "Cores/PersonalityCores/"
localisationDir = "./Localisation/"
localisationSuffix = ".json"

def GetBotToken(personalityCoreFile):
    try:
        with open(personalityCoresDir + personalityCoreFile, 'r') as textFile:
            out = json.loads(textFile.read())["token"]
        return out
    except (FileNotFoundError, IOError): return "" # Cancels operation in bot manager
def GetLocalisation(language):
    with open(localisationDir + language + localisationSuffix, 'r') as locfile:
        out = json.loads(locfile.read())
    return out