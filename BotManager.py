#!/usr/bin/env python3

from Bot import Bot # Import the bot class
import CentralLog # Import central log interface
from CommandLine import CommandLine

class BotInterface:
    # Works with the active bots
    def __init__(self):
        self.bots = dict([])
        self.botIDs = []
        self.botID = 0
    def NewBot(self, personalityCoreFile, functionalityCores, cleanStart):
        # Check the cores
        test = sanityChecker.CheckFuncCores(functionalityCores)
        if not test[0]:
            commandLine.GiveError("Could not load functionality cores {}".format(test[1]))
            return
        # Create and activate a new bot
        token = CentralLog.GetBotToken(personalityCoreFile)
        if not token:
            commandLine.GiveError("Core not found")
            return
        if not token in self.bots: # If the bot token is not already used
            self.bots[token] = Bot(personalityCoreFile, functionalityCores, cleanStart)
            self.bots[token].Start() # Start the bot automatically
            self.botIDs.append((self.botID, token))
            self.botID += 1
        else: # Give an error when the token is already used
            commandLine.GiveError("This bot token is already in use. Bot tokens should not be used multiple times in parallel")
    def StopBot(self, token):
        for bot in self.bots:
            if self.bots[bot].personalityCore["token"] == token: # If the bot is the one to be stopped
                self.bots[bot].Stop() # Halt the bot
                commandLine.Display("Killed bot {}".format(self.bots[token].personalityCore["callname"]))
                del self.bots[bot] # Remove the entry
                for i in range(len(self.botIDs)):
                    if self.botIDs[i][1] == token:
                        del self.botIDs[i]
                        break
                return # Return without checking the others
    def StopBotByID(self, ID): # Translate the ID into a token, then defer to the standard method
        token = ""
        for pair in self.botIDs:
            try: id = int(ID)
            except: id = -1
            if pair[0] == id:
                token = pair[1]
                break
        if not token: commandLine.GiveError("Bot ID not found") # If the token has not been set give an error
        else: self.StopBot(token)
    def Info(self):
        info = "".join(["{} | {}: {}\n".format(bot[0], self.bots[bot[1]].personalityCore["callname"], bot[1]) for bot in self.botIDs]) # Bot IDs, names and tokens
        commandLine.Display(info)

class SanityChecker:
    # Tests argument validity
    def __init__(self):
        self.corePackage = "Cores.FunctionalityCores." # Path to the directory where the personality cores are located (in package form)
    def CheckFuncCores(self, functionalityCores): # Tests whether all functionality cores can be loaded
        import importlib
        passed = True
        errors = []
        for core in functionalityCores:
            try: importlib.import_module(self.corePackage + core)
            except Exception: passed = False; errors.append(core)
        return (passed, errors)

def ShutDown():
    commandLine.Display("Shutting down bots...")
    for bot in botInterface.bots:
        botInterface.StopBot(bot)
    commandLine.Display("Finalising...")
    raise SystemExit

# Global access
language = "EN"
commandLine = CommandLine(None)
sanityChecker = SanityChecker()

# Main
if __name__ == "__main__":
    botInterface = BotInterface()
    managerData = {
        "callbacks":{
            "newbot":botInterface.NewBot,
            "stopbotbyid":botInterface.StopBotByID,
            "info":botInterface.Info,
            "stop":ShutDown
        }
    }
    commandLine = CommandLine(managerData)
    commandLine.Listen()
    #botInterface.NewBot()
