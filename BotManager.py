#!/usr/bin/env python3

from Bot import Bot # Import the bot class
import CentralLog # Import central log interface

# Global access
language = "EN"
localisation = CentralLog.GetLocalisation(language) 

class BotInterface:
    # Works with the active bots
    def __init__(self):
        self.bots = dict([])
    def NewBot(self, personalityCoreFile, functionalityCores, cleanStart):
        # Create and activate a new bot
        token = CentralLog.GetBotToken(personalityCoreFile)
        if not token in self.bots or self.bots[token] is None: # If the bot token is not already used
            self.bots[token] = Bot(personalityCoreFile, functionalityCores, cleanStart)
        else: # Give an error when the token is already used
            CommandLine.GiveError(localisation.botduplicateerror)
    def StopBot(self, token):
        for bot in self.bots:
            if self.bots[bot].personalityCore["token"] == token: # If the bot is the one to be stopped
                return self.bots[bot].Stop() # Halt the bot and return

if __name__ == "__main__":
    botInterface = BotInterface()
    botInterface.NewBot()