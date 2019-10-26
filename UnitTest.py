#!/usr/bin/env python3

PASS = "pass"
FAIL = "fail"

# Test Bot Structure
from BotLog import Logger as BotLogger
from Bot import Bot

""" TESTS
Loading personality core
Starting bot
Stopping bot
"""

core = "J4S0N.json" # Valid personality core with existing token
try: # Loading personality core
    botLog = BotLogger()
    botLog.ReadPersonalityCore(core)
    print(PASS)
except Exception as e: print(FAIL + ": {}".format(e))
try: # Starting bot
    bot = Bot(core, [], True)
    print(PASS)
    try: # Stopping bot
        bot.Stop()
        print(PASS)
    except Exception as e:
        print(FAIL + ": {}".format(e))
except Exception as e: print(FAIL + ": {}".format(e)); print(FAIL + ": ^")

# Test Central Log
import CentralLog

""" TESTS
Fetch localisation
Fetch token
"""

core = "J4S0N.json" # Valid personality core with existing token
language = "EN" # Valid language
try: CentralLog.GetLocalisation(language); print(PASS)
except Exception as e: print(FAIL + ": {}".format(e))
try: CentralLog.GetBotToken(core); print(PASS)
except Exception as e: print(FAIL + ": {}".format(e))

# Test Bot Manager
import CentralLog
from BotManager import BotInterface

""" TESTS
Creating bot manager
Starting new bot
Stopping new bot
"""

core = "J4S0N.json" # Valid personality core with existing token
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
except Exception as e: print(FAIL + ": {}".format(e))