# PAWT: a Python API Wrapper for Telegram

## AKA Pre-Alpha Wrapper for Telegram

[![Coverage Status](https://coveralls.io/repos/github/jarhill0/pawt/badge.svg?branch=master)](https://coveralls.io/github/jarhill0/pawt?branch=master)

## About

This code is pre-alpha. I believe I have full coverage of the Telegram API, 
but no tests have been written and much of the package hasn't even been used 
at all. 

I'm going to first find obvious bugs either by integrating this package into my 
Telegram bot [A Bot](https://github.com.jarhill0/ABot) or by building a new 
bot with it and running. Once I've eliminated all the bugs that are obvious 
to me, I'll begin writing tests, restructuring the package along the way to 
make more logical sense. 

## Installation

```commandline
python3 -m pip install git+https://github.com/jarhill0/pawt.git
```

## Usage

To use a Telegram instance:

```python
import pawt

tg = pawt.Telegram(token='YOUR TOKEN') # use your token
```

To build a bot class, inherit from `pawt.bots.TelegramBotInterface` and 
override the desired methods. Call `.run()` to run the bot:

```python
from pawt.bots import TelegramBotInterface
from pawt.exceptions import APIException

class MyBot(TelegramBotInterface):
    def message_handler(self, message):
        try:
            message.reply.send_message('Thanks for your message.')
        except APIException:
            # something we can't reply to
            pass
            
bot = MyBot(token='YOUR TOKEN') # use your token
bot.run()
```

Bot classes have a `perform_extra_task()` method that can be overridden to do
a specific task after processing each set of updates, or after timeout. 

## Warnings 

Don't be stupid. Don't use this package yet. I made it for myself, and it's 
likely riddled with bugs. Search for a Python Telegram API Wrapper that's 
established and use that. 

If you are stupid enough to use it, know that methods and names and classes 
and *EVERYTHING* can and will change without warning as I make the package 
more friendly.
