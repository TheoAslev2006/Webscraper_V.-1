from src.com.main.JsonSave import Json
from src.com.main.Logger import Logger
from src.com.main.Logger.Excepetions import Exceptions
from Utils import WSMethods


Json.load()
Logger.info("Starting...")
html = "None"
try:
    url = input()
    html = WSMethods.GetWebHTML(url)
    print(html)
except:
    Logger.Error(Exceptions.ExceptionsType(3))
Logger.info(WSMethods.FindHTMLTitle(html))








