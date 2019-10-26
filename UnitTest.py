#!/usr/bin/env python3

PASS = "pass"
FAIL = "fail"

# Test Bot Structure
from BotLog import Logger as BotLogger
from Bot import Bot

""" TESTS
Loading personality core
Creating bot
Starting bot
Stopping bot
Getting functionality cores
"""

core = "TestCore.json" # Valid personality core with existing token
funcCores = ["Test"]
try: # Loading personality core
    botLog = BotLogger()
    botLog.ReadPersonalityCore(core)
    print(PASS)
except Exception as e: print(FAIL + ": {}".format(e))
try: # Creating bot
    bot = Bot(core, [], True)
    print(PASS)
    try: # Starting bot
        bot.Start()
        print(PASS)
    except Exception as e:
        print(FAIL + ": {}".format(e))
    try: # Stopping bot
        bot.Stop()
        print(PASS)
    except Exception as e:
        print(FAIL + ": {}".format(e))
except Exception as e: print(FAIL + ": {}".format(e)); print(FAIL + ": ^")
try: # Getting cunctionality cores
    bot = Bot(core, funcCores, True)
    if not bot.functionalityCores: print(FAIL + ": cores not imported")
    elif not bot.commands: print(FAIL + ": no commands fetched")
    else: print(PASS)
except Exception as e:
    print(FAIL + ": {}".format(e))

# Test Central Log
import CentralLog

""" TESTS
Fetch token
"""

core = "TestCore.json" # Valid personality core with existing token
language = "EN" # Valid language
try: CentralLog.GetBotToken(core); print(PASS)
except Exception as e: print(FAIL + ": {}".format(e))

# Test Command Line
from CommandLine import CommandLine
commandLine = CommandLine(None)

""" TESTS
Give error
"""

try:
    commandLine.GiveError(PASS)
except Exception as e: print(FAIL + ": {}".format(e))

# Test Bot Manager
import CentralLog
from BotManager import BotInterface

""" TESTS
Creating bot manager
Starting new bot
Stopping new bot
Testing new bot in Telegram
Stopping bot in Telegram
"""

core = "TestCore.json" # Valid personality core with existing token
funcCores = ["Test"]
token = CentralLog.GetBotToken(core)
try: # Creating bot manager
    botInterface = BotInterface()
    print(PASS)
    try: # Starting new bot
        botInterface.NewBot(core, [], True)
        print(PASS)
        try: # Stopping new bot
            botInterface.StopBot(token)
            print(PASS)
        except Exception as e:
            print(FAIL + ": {}".format(e))
    except Exception as e:
        print(FAIL + ": {}".format(e))
    try: # Testing new bot in Telegram
        botInterface.NewBot(core, funcCores, True)
        print(PASS)
        input("Stop bot")
        try: # Stopping bot in Telegram
            botInterface.StopBot(token)
            print(PASS)
        except Exception as e:
            print(FAIL + ": {}".format(e))
    except Exception as e:
        print(FAIL + ": {}".format(e))
except Exception as e: print(FAIL + ": {}".format(e))