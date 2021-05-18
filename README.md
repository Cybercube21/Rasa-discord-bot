# Discord Rasa AI Bot

This Bot can use a local [Rasa](https://rasa.com/) Model to parse Messages and hold conversations

## Dependencies
Use this commands to install all dependencies that are needed


### Windows:

Go to the [Python](https://python.org/downloads/) Website and download the installer (Latest tested Version is 3.8.9)

Install Python3 + Pip3 via the installer (A reboot is maybe required)

Now open a new Terminal (WIN+R + "cmd") and type:

```sh
$ pip3 install rasa 
$ discord.py python_dotenv pytz requests
```
### Linux (Ubuntu):

```sh
$ sudo apt update && sudo apt upgrade &&  sudo apt install python3-dev python3-pip
$ pip3 install -U pip
$ pip3 install rasa
$ pip3 install discord.py python_dotenv pytz requests
```

## How to Set-Up

First, get your Bot's Token via the [Discord Developer Portal](https://discord.com/developers/applications) and copy it into the .env File.

If you want or need to use another Rasa Model, make sure to *NOT* delete or overwrite the "connectors" Folder. It contains the Custom Connector for the [Rasa API](https://rasa.com/docs/rasa/connectors/custom-connectors).

## How to Use

Simply get into the Project Folder and use the following Commands and write a Message in any Channel (Dont forget to invite the Bot ;D):

```sh
$ python3 chatbot.py # To start the Bot

# Then open a new Terminal and go in the model/ Folder
$ rasa run --enable-api --credentials credentials.yml --cors "*" # To Start the Rasa Server
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact 
Join my [Discord Server](https://discord.gg/4XYcD2Jk54) or DM me: Cybercube#0499
