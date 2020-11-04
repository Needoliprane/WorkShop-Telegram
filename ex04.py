import json
import time

def master():
    f = open('config.json',) 
    data = json.load(f)
    while (data["stop"] == False):
        print(data["super"])
        time.sleep(1)

master()