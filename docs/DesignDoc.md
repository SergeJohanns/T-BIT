# Main goals

## Bots
Since T-BIT builds on the exellent wrapper [python-telegram-bot](https://python-telegram-bot.org/), a lot of the boilerplate inherent to the telegram bot api is already handled automatically. T-BIT should to extend this mentality, while making sure that functionality does not become unavailable or buried.

## Management
The main goal of T-BIT is not just to be a slightly more extensive bot library, but to facilitate the organised operation of a collection of different bots. For this it is important to achieve the following:

### Modularity
Modularity is reasonable easy to implement, but hard to convince yourself to implement if you feel like it won't matter. Sooner or later, the modules are too interdependent to change out without breaking things and all that's left is a regular, non-modular system. T-BIT should be built with modularity in mind and made to interact with modular systems to keep the system structure overseeable.

### Single-session flexability
While it is important to design the system in such a way that subsystems are modular and flexible, it should be kept in mind that merely being able to load any arbitrary module is insufficient. Since T-BIT is a management system for multiple bots, not just a framework for singular bot objects, it should not be necissary to reboot the system for simple changes to take effect. Rebooting should be necissary as little as possible.

### Proper data access
Sometimes data should be shared between bots. Sometimes data should be accessable (and editable) by just one bot, as if the data belonged to it specifically. Although it's always easy to meet one of these conditions, using both, and using them the right way, is the tricky part. T-BIT should organise a central administration as well as a local administration for each bot, meaning data and log files are always sufficiently safe and sufficiently accesible.

### Parallelism
Since bots should be able to run independently from oneanother, it would be useful if they could be run in parallel to allow for large collections of bots. This means requires the use of the multiprocessing module, as wel as making sure that all central systems are thread-safe.

### Status insight
In order to oversee a collection of bots, it helps to see the collection of bots. To help with this T-BIT will implement basic monitoring of currently active bots.

### Bot restriction
Although bots should be built with restrictions in place, that's rather like saying buildings should be built in a fire-averse manner. It's certainly true, but it's nice to have a sprinkler system in place. T-BIT should be able to set restrictions on bots including used bandwidth, sent messages, etc. and enforce them proactively.

# Structure
## Main modules and classes
### Bot Manager
The Bot Manager acts as a central control point for all active bots.

### Command Line
The Command Line is a class that controls the terminal command line, including command parsing and argument forwarding.

### Central Log
The Central Log writes to and reads from the global data files, taking requests from and passing data on to the other modules.

### Data files and logs
#### Phonebook
The phonebook is a central .json file containing known user:id and chat:id pairs, along with relevant data.

## Bots
### Bot
The main Bot script builds the connection with the API, manages the command handler and includes some universal bot commands.

### Bot logger
The bot logger serves as the interface between the bot class and it's personal logs, as well as fetching the personality cores.

### Personality core
A personality core is a .json file that includes information for a unique bot. This means information such as the API key, name and description. A bot only has one personality core.

### Functionality core
A functionality core is a python module that includes a set of commands and their corresponding functions. These can be used to give a bot extended functionality, and a bot can have multiple functionality cores.

### Data files and logs
#### Bot log
The bot log is a .csv file containing event logs for the bot, including timestamps.

#### Bot state
The bot state is a .json file for persistent storage of data such as flags and other states.
