#!/usr/bin/env python3

import json

class Logger:
    def __init__(self):
        self.coreDirectory = "./Cores/PersonalityCores/" # Path to the directory where the personality cores are located (including trailing slash)
    def ReadPersonalityCore(self, coreName):
        try:
            with open(self.coreDirectory + coreName) as core:
                out = json.loads(core.read()) # Get the stored json in dictionary form
        except:
            print("Could not load personality core")
            out = dict([]) # Set information to empty dictionary
        return out # Return the core in dictionary form (or an empty dictionary on failure)