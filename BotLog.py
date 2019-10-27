#!/usr/bin/env python3

import json
import atexit

class Logger:
    def __init__(self):
        self.coreDirectory = "./Cores/PersonalityCores/" # Path to the directory where the personality cores are located (including trailing slash)
        atexit.register(self.ExitLog)
    def ReadPersonalityCore(self, coreName):
        self.stashedCore = coreName
        try:
            with open(self.coreDirectory + coreName) as core:
                out = json.loads(core.read()) # Get the stored json in dictionary form
        except:
            print("Could not load personality core") # To be replaced by more integrated logging
            out = dict([]) # Set information to empty dictionary
        try:
            with open(self.coreDirectory + "p_" + coreName) as persistent:
                self.logData = json.loads(persistent.read())
        except:
            self.logData = dict([])
        self.core = out
        return out # Return the core in dictionary form (or an empty dictionary on failure)
    def PersistentLog(self, logPath, payLoad):
        self.LogRecurse(self.logData, logPath, payLoad)
    def LogRecurse(self, datadict, path, payLoad):
        if len(path) == 1: datadict[path[0]] = payLoad # If there is only one key left, write the payload to the slot
        elif path[0] in datadict: self.LogRecurse(datadict[path[0]], path[1:], payLoad) # If the current key does exist, repeat the function one place further in the path
        else: # Else, create an empty dictionary at that key and repeat
            datadict[path[0]] = dict([])
            self.LogRecurse(datadict[path[0]], path[1:], payLoad)

    def PersistentLogRead(self, logPath):
        self.ReadRecurse(self.logData, logPath)
    def ReadRecurse(self, datadict, path):
        try:
            if len(path) == 1: return datadict[path[0]] # If there is only one key left, read the value from the slot
            else: self.LogRecurse(datadict[path[0]], path[1:]) # Else, repeat the function one place further in the path
        except KeyError: # If a key is missing
            return None
            if path: print("Could not find key " + path[0] + " in persistent bot log")
    def ExitLog(self):
        try:
            with open(self.coreDirectory + "p_" + self.stashedCore, 'r') as core:
                backup = json.loads(core.read())
        except FileNotFoundError:
            backup = dict([])
        try:
            with open(self.coreDirectory + "p_" + self.stashedCore, 'w') as core:
                core.write(json.dumps(self.logData, sort_keys = True, indent = 4))
        except Exception as e:
            print(e)
            with open(self.coreDirectory + "p_" + self.stashedCore, 'w') as core:
                core.write(json.dumps(backup, sort_keys = True, indent = 4))