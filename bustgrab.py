
import requests
import shutil
import os

def getpic(username):
    pathFrom = "https://minecraftskinstealer.com/api/v1/skin/download/bust/"+username
    pathTo = "/Users/marvin/Desktop/CODE/MCBUSTS/"+username + ".png"
    res = requests.get(pathFrom, stream = True)
    if res.status_code == 200:
        with open(pathTo,'wb') as f:
            shutil.copyfileobj(res.raw, f) 


getpic(input('username:'))