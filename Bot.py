#!/usr/bin/env python3

# Local Imports
import BotLog

# Dependencies
import importlib # Importlib facilitates importing modules by name, allowing the importing of variably named local modules
from telegram.ext import Updater # The Updater class polls the telegram API for new commands and messages
from telegram.ext import CommandHandler # The CommandHandler class couples command strings to functions in the script
from telegram.ext import MessageHandler # The MessageHandler class allows functions to reply to plain messages
from telegram.ext import Filters # Filters allow commands and messages to fall through under certain conditions 

class Bot:
    shutDownTimeOut = 10 # Maximum time to wait for the updater to stop running on shutdown (in seconds)
    corePackage = "Cores.FunctionalityCores." # Path to the directory where the personality cores are located (in package form)

    # The bot is initialised with references to a personality core .json file and functionality core .py files
    def __init__(self, personalityCoreFile, functionalityCores, cleanStart):
        self.logger = BotLog.Logger() # The logger serves as an intermediate between the bot and it's personal files
        self.personalityCore = self.logger.ReadPersonalityCore(personalityCoreFile)) # The personality core contains information such as the authentication token of the bot
        self.functionalityCores = [importlib.import_module(corePackage + core) for core in functionalityCores]
        self.updater = Updater(self.personalityCore.token, use_context = True) # The Updater takes the authentication token as an argument, allowing it to build the API connection. use_context = True is used to specify that we are using the new context system of the python-telegram-bot library
        self.dispatcher = self.updater.dispatcher
        self.cleanStart = cleanStart
        self.commands = []
        self.messageHandlers = []
        for core in functionalityCores:
            # Add all of the commands and message handlers belonging to the functionality cores to the command list
            self.commands.extend(core.GetCommands())
            self.messageHandlers.extend(core.GetMessageHandlers())
        for pair in self.commands:
            # Add all of the handlers for the commands, making sure the commands are piped through to the right functions
            self.dispatcher.add_handler(CommandHandler(pair[0], pair[1]))
        for pair in self.messageHandlers:
            # Add all of the handlers for the messages, making sure the messages are piped through to the right functions
            self.dispatcher.add_handler(MessageHandler(pair[0], pair[1]))
        self.dispatcher.add_handler(CommandHandler(Filters.command, self.unknowncommand)) # Add a final catch-all
        self.dispatcher.add_handler(CommandMessage(Filters.text, self.unknownmessage)) # Add a final catch-all

    # Standard bot methods
    def unknowncommand(self, update, context):
        # Bot-implemented catch-all
        for core in self.functionalityCores:
            # Tell every core a command was not recognised
            try: core.unknowncommand(update, context) # Try to call the function 'unknowncommand' on the core
            except NameError: pass # If the function doesn't exist move on to the next
    def unknownmessage(self, update, context):
        # Bot-implemented catch-all
        for core in self.functionalityCores:
            # Tell every core a message was not filtered
            try: core.unknownmessage(update, context) # Try to call the function 'unknownmessage' on the core
            except NameError: pass # If the function doesn't exist move on to the next
    def Start(self):
        self.updater.start_polling(clean = self.cleanStart) # If clean = True all updates from before the bot was turned on will be ignored 
    def Stop(self):
        self.updater.stop(10) # Tell the updater to stop running, time out after 10 seconds
        if self.updater.running: # If the updater is then still running
            raise SystemExit # Kill the thread by force