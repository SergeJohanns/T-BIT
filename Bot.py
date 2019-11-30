from telegram.ext import Updater # The Updater class polls the telegram API for new commands and messages
from telegram.ext import CommandHandler # The CommandHandler class couples command strings to functions in the script
from telegram.ext import MessageHandler # The MessageHandler class allows functions to reply to plain messages
from telegram.ext import Filters # Filters allow commands and messages to fall through under certain conditions 

class Bot:
    """The core of the bot model, containing all api information and special methods to interact with the api."""

    def __init__(self, personalityCore : dict, functionalityCores : [str], commands : [(str, callable)], logger):
        """Set up the api connection and set all of the necessary properties."""
        self.logger = logger
        self.data = logger.Restore()
        self.personalityCore = personalityCore
        self.functionalityCores = functionalityCores
        self.updater = Updater(self.personalityCore.token, use_context=True)
        for (command, callback) in commands:
            self.updater.dispatcher.add_handler(CommandHandler(command, callback))

    def SendMessage(self, target : str, message : str):
        """Send a message to a target chat."""
        self.updater.bot.send_message(chat_id=target, text=message)
