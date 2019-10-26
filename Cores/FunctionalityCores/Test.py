def GetCommands(): # Return a list of commandstring-callback tuples
    return [
        ("hi hello", hi)
    ]
def GetMessageHandlers(): # Return a list of message-callback tuples
    return [

    ]

def SetBotInfo(info):
    global bot
    bot = info

def hi(update, context):
    print("Hi")
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hi!")