from random import choice

from src.com.main.JsonSave import Json
from src.com.main.Logger import Logger
from src.com.main.Logger.Excepetions import Exceptions
from com.main.WebScraperMethods import WSMethods
from Utils import Method, Commands
Logger.info("/help to begin")

while True:
    choice = input("/")
    switch = Method
    if switch.CommandSwitch(choice) == 1:
        print(Commands.HelpCommand)
    if switch.CommandSwitch(choice) == 2:
        Logger.info("Provide Valid Url")
        html = "None"
        url = input(">")
        try:
            html = WSMethods.GetWebHTML(url)
        except:
            Logger.Error(Exceptions.ExceptionsType(3))
        Logger.printHTML(html)
        Logger.Spaces()
        Logger.info("Title: " + WSMethods.FindHTMLTitle(html))
    if switch.CommandSwitch(choice) == 3:
        Logger.info("Provide Valid Url")
        html = "None"
        url = input(">")
        try:
            html = WSMethods.GetWebHTML(url)
        except:
            Logger.Error(Exceptions.ExceptionsType(3))
        Logger.printHTML(html)
        Logger.Spaces()
        Logger.info("Title: " + WSMethods.FindHTMLBody(html))






