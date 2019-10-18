# Main goals

## Bots
Since T-BIT builds on the exellent wrapper [python-telegram-bot](https://python-telegram-bot.org/), a lot of the boilerplate inherent to the telegram bot api is already handled automatically. T-BIT should to extend this mentality, while making sure that functionality does not become unavailable or buried.

## Management
The main goal of T-BIT is not just to be a slightly more extensive bot library, but to facilitate the organised operation of a collection of different bots. For this it is important to achieve the following:

### Modularity
Modularity is reasonable easy to implement, but hard to convince yourself to implement if you feel like it won't matter. Sooner or later, the modules are too interdependent to change out without breaking things and all that's left is a regular, non-modular system. T-BIT should be built with modularity in mind and made to interact with modular systems to keep the system structure overseeable.

### Proper data access
Sometimes data should be shared between bots. Sometimes data should be accessable (and editable) by just one bot, as if the data belonged to it specifically. Although it's always easy to meet one of these conditions, using both, and using them the right way, is the tricky part. T-BIT should organise a central administration as well as a local administration for each bot, meaning data and log files are always sufficiently safe and sufficiently accesible.

### Status insight
In order to oversee a collection of bots, it helps to see the collection of bots. To help with this T-BIT will implement basic monitoring of currently active bots.

### Bot restriction
Although bots should be built with restrictions in place, that's rather like saying buildings should be built in a fire-averse manner. It's certainly true, but it's nice to have a sprinkler system in place. T-BIT should be able to set restrictions on bots including used bandwidth, sent messages, etc. and enforce them proactively.
