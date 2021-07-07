import requests
import time
title = """This Is 100% free Source will be on github
found at github.com/tubbytoons
 
Black Jack Auto spin
"""
time.sleep(1)
print(title)
time.sleep(1)
token = str(input("Input your token: "))
channelID = str(input("Input your Black Jack channel ID: "))



def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}

    r = requests.post(url, data=data, headers=header)
    
while True:
    time.sleep(305)
    print("Message Sent.")
    sendMessage(token, channelID, "+spin")
