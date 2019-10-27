# T-BIT | Telegram Bots In Terminal
T-BIT is a telegram bot and bot management tool focussed on bot modularity. It helps you build telegram bots in Python with ease and manage larger collections of bots in parallel.

Bots are built out of 'functionality cores', allowing the isolation and reuse of command functionality. These cores can still be connected like regular python modules can, but this is no longer the default, preventing common bugs. This also makes it easier to share bot functionality, as 
you can simply share and run arbitrary cores without having to somehow write them into an existing bot script.

For the full documentation, see the [wiki](https://github.com/SergeJohanns/T-BIT/wiki). Also see [python-telegram-bot](https://python-telegram-bot.org/), which is the Python wrapper that T-BIT builds on and has the documentation for types and methods that also show up in T-BIT, as well as the [official telegram bot API](https://core.telegram.org/bots/api), which has the info on all of the types and methods the API offers.
