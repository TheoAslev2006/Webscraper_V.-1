from Logger import Logger
from Logger.Excepetions import Exceptions
from WebScraperMethods import WSMethods
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






