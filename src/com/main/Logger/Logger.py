from datetime import date
from datetime import datetime
from inspect import currentframe, getframeinfo
import os
current_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

def info(string):
        print(f"[-- INFO --] {string} [--Date/Time:{current_date}--]")

def Error(Exeption):
        print(f"[-- ERROR --] Exeption:{Exeption}  [--Date/Time:{current_date} --]")
def printHTML(html):
        print(f"""
        [-- HTML --]
        {html}
        [--Date/Time:{current_date} --]
        """)
