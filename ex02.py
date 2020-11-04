import requests
from telegram import msBotGetText, msBotSendText

def test1():
    res = requests.get("https://this_url_dont_exist.com")
    print(res)


def test2():
    data = {}
    data.append("b")

def test3():
    data = "Je suis une string" + int(12)
    print(data)

def test4():
    data = []
    data["first"] = "b"

def test5():
    data = []
    data[100] = "a"

test1()