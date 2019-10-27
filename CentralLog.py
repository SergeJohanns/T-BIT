#!/usr/bin/env python3

import json

personalityCoresDir = "Cores/PersonalityCores/"
localisationDir = "./Localisation/"
localisationSuffix = ".json"
presetFile = "presets.json"

def GetBotToken(personalityCoreFile):
    try:
        with open(personalityCoresDir + personalityCoreFile, 'r') as textFile:
            out = json.loads(textFile.read())["token"]
        return out
    except (FileNotFoundError, IOError): return "" # Cancels operation in bot manager
def NewPreset(name, personalityCore, functionalityCores, clean):
    try:
        with open(presetFile, 'r') as textFile:
            presets = json.loads(textFile.read())
    except (FileNotFoundError, json.decoder.JSONDecodeError): presets = dict([])
    presets[name] = {"personalitycore":personalityCore, "functionalitycores":functionalityCores, "cleanstart":clean}
    with open(presetFile, 'w') as textFile:
        textFile.write(json.dumps(presets, sort_keys = True, indent = 4))
def LoadPreset(name):
    with open(presetFile, 'r') as textFile:
        presets = json.loads(textFile.read())
    if name in presets: return presets[name]
    else: print("Preset does not exist")