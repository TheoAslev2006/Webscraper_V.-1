from inspect import getframeinfo, currentframe

from src.com.main.Logger import Logger
from urllib.request import urlopen

from src.com.main.Logger.Excepetions import Exceptions


def LogWebHTML(url):
    Logger.info(f"Getting Html code from{url}")
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    Logger.printHTML(html)
def GetWebHTML(url):
    Logger.info(f"Getting Html code from{url}")
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html
def FindHTMLTitle(HTML):
    try:
        startIndex = HTML.find("<title>") + len("<title>")
        endIndex = HTML.find("</title>")
        titel = HTML[startIndex:endIndex]
        return titel
    except:
        Logger.Error(Exceptions.ExceptionsType(1))
def FindHTMLBody(HTML):
    try:
        startIndex = HTML.find("<body>") + len("<body>")
        endIndex = HTML.find("</body>")
        body = HTML[startIndex:endIndex]
        return body
    except:
        Logger.Error(Exceptions.ExceptionsType(4))





