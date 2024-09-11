import json
from src.com.main.Logger import Logger
from src.com.main.Logger.Excepetions import Exceptions

def load():
    try:
        with open(r'Resource/Save.json') as file:
            JsonData = json.load(file)
            JsonString = json.dumps(JsonData)
            start = JsonString.find("[") + 1
            end = JsonString.find("]")
            JsonString = JsonString[start:end]
            JsonArray = JsonString.split('"')
            newJsonString = ""
            for e in JsonArray:
                newJsonString += e
            return newJsonString
    except FileNotFoundError:
        Logger.Error(Exceptions.ExceptionsType(2))