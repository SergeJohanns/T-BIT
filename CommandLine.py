#!/usr/bin/env python3

class CommandLine:
    # Serves as the command line interface for the system
    def __init__(self, managerData):
        self.commandChar = ":"
        self.commands = dict([])
        self.rawcommands = {"q quit exit shutdown": self.Stop,
                            "b bot newbot": self.Bot,
                            "k kill killbot": self.Kill,
                            "p preset botpreset":self.Preset,
                            "l load loadpreset":self.LoadPreset,
                            "h help": self.Help,
                            "i info": self.Info,
                            "c credit credits": self.Credit}
        self.managerData = managerData
        for rawcommand in self.rawcommands: # Split space-seperated synonyms
            for command in rawcommand.split(" "):
                self.commands[command] = self.rawcommands[rawcommand]

    # Command Parsing
    def Listen(self): # Start listening for commands in the terminal
        while True:
            self.Parse(input("> "))
    def Parse(self, entered): # Parse user input
        if not entered: return # If the input is an empty string
        elif entered[0] == self.commandChar: # if the user entered a command
            if ' ' in entered: commandEnd = entered.index(' ') # If there is a space that is where the command ends
            else: commandEnd = len(entered) # else the entire string is a command
            command = entered[1:commandEnd] # Get the command string between the command char and the command end
            if command in self.commands: self.commands[command](entered[commandEnd + 1:]) # Execute the command with everything after the command end as an arg string
            else: self.UnknownCommand(command)

    # Display 
    def Splash(self): # Show splashscreen
        print("T-BIT Terminal Interface\n")
    def GiveError(self, errorString): # Display an error
        self.Display(errorString)
    def Display(self, message): # Show a message
        print(message)

    # Command Methods
    def Bot(self, args):
        args = args.split(" ")
        args = [arg for arg in args if arg] # Remove all empty string entries
        if not args: return
        clean = args[0] == "-c" # Set clean to whether the clean flag is set
        if clean: # If the clean start flag is set
            args = args[1:] # Start after this
        if not args: return
        personalityCore = args[0]
        functionalityCores = args[1:]
        self.managerData["callbacks"]["newbot"](personalityCore, functionalityCores, clean)
    def Kill(self, args):
        name = args
        self.managerData["callbacks"]["stopbotbyid"](name)
    def Preset(self, args):
        args = args.split(" ")
        args = [arg for arg in args if arg] # Remove all empty string entries
        if not args: return
        name = args[0]
        args = args[1:]
        if not args: return
        clean = args[0] == "-c" # Set clean to whether the clean flag is set
        if clean: # If the clean start flag is set
            args = args[1:] # Start after this
        if not args: return
        personalityCore = args[0]
        functionalityCores = args[1:]
        self.managerData["callbacks"]["preset"](name, personalityCore, functionalityCores, clean)
    def LoadPreset(self, args):
        data = self.managerData["callbacks"]["loadpreset"](args.strip())
        self.managerData["callbacks"]["newbot"](data["personalitycore"], data["functionalitycores"], data["cleanstart"])
    def Info(self, args):
        self.managerData["callbacks"]["info"]()
    def Help(self, args):
        self.Display("q | shut down manager\nb | new bot\nk | kill bot\nh | help\ni | manager info\nc | credit")
    def Credit(self, args):
        self.Display("Made by Serge Johanns. Features inspired in part by Remco Johanns.")
    def Stop(self, args):
        try: self.managerData["callbacks"]["stop"]() # Try to exit through the manager
        except: raise SystemExit # Force exit if not possible
    
    def UnknownCommand(self, args):
        self.Display("This command is not recognised")

if __name__ == "__main__": # Default command line
    commandLine = CommandLine(None)
    commandLine.Splash()
    commandLine.Listen()