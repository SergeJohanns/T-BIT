#!/usr/bin/env python3

import json

personalityCoresDir = "./Cores/PersonalityCores/"
localisationDir = "./Localisation/"
localisationSuffix = ".json"

def GetBotToken(personalityCoreFile):
    with open(personalityCoresDir + personalityCoreFile, 'r') as textFile:
        out = json.loads(textFile.read())["token"]
    return out
def GetLocalisation(language):
    with open(localisationDir + language + localisationSuffix, 'r') as locfile:
        out = json.loads(locfile.read())
    return out