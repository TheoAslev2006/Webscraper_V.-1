import json
import os
from src.com.main.Logger import Logger
from src.com.main.Logger.Excepetions import Exceptions


def load():
    try:
        with open(r'C:\Users\Theo Åslev\PycharmProjects\Webscraper_V.-1\src\Resource\Save.json') as file:
            JsonData = json.load(file)
            JsonString = json.dumps(JsonData)
            start = JsonString.find("[") + 1
            end = JsonString.find("]")
            JsonString = JsonString[start:end]
            print(JsonString.find('"'))
            JsonArray = JsonString.split('"')
            newJsonString = ""
            for e in JsonArray:
                newJsonString += e
            return newJsonString
    except FileNotFoundError:
        Logger.Error(Exceptions.ExceptionsType(2))