# Discord Rasa AI Bot

This Bot can use a local Rasa Model to parse Messages and hold conversations

## Dependencies
Use this commands to install all dependencies that are needed


Windows:
Go to the [Python](https://python.org/downloads/) Website and download the installer (Latest tested Version is 3.8.9)

Install Python3 + Pip3 via the installer (A reboot is maybe required)

Now open a new Terminal (WIN+R + "cmd") and type:

```sh
$ pip3 install rasa discord.py python_dotenv pytz requests
```

```sh
$ Linux (Ubuntu):
$ sudo apt update && sudo apt upgrade &&  sudo apt install python3-dev python3-pip
$ pip3 install -U pip
$ pip3 install rasa
$ pip3 install discord.py python_dotenv pytz requests
```

## How to Set-Up

First, get your Bot's Token via the [Discord Developer Portal](https://discord.com/developers/applications) and copy it into the .env File.

If you want or need to use another Rasa Model, make sure to *NOT* delete or overwrite the "connectors" Folder. It contains the Custom Connector for the [Rasa API](https://rasa.com/docs/rasa/connectors/custom-connectors).

## How to Use

Simply get into the Project Folder and use the following Command:

```sh
$ python3 chatbot.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
