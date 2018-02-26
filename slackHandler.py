import re
import json
from slackclient import SlackClient
import config

# Connect slack bot.
# slack_client = SlackClient(config.api_key)
slack_client = SlackClient(config.api_key_bottington)

user_list = slack_client.api_call("users.list")

fantasticGifs = ["https://giphy.com/gifs/excited-the-office-celebrate-Is1O1TWV0LEJi",
                 "https://giphy.com/gifs/news-atl-down-MTclfCr4tVgis",
                 "https://giphy.com/gifs/cheer-cheering-oxW9IXKWP2Ouk",
                 "https://giphy.com/gifs/internet-eoxomXXVL2S0E",
                 "https://giphy.com/gifs/cat-reaction-youtubers-609o8uNjasiJO",
                 "https://giphy.com/gifs/reactionseditor-come-on-you-got-this-3og0IPMeREHpEV0f60",
                 "https://giphy.com/gifs/heyarnold-nickelodeon-hey-arnold-26Ff4Ci2RNT1H1zb2"]
# Used to ping winner.
# winnerNames = ["@lizl", "@charles.mitchell", "@shuggard", "@hubert-j-farnsworth", "@qwerji", "@eddrakee"]
winnerNames = ["@jealousmango", "@krysco",
               "@jealousmango", "@krysco", "@jealousmango", "@krysco"]

winningMessage = winnerHandle
slack_client.api_call(
    "chat.postMessage",
    channel="general",
    text="The winner has been selected...",
    as_user=True)

time.sleep(1)

slack_client.api_call(
    "chat.postMessage",
    channel="general",
    text=winningMessage,
    as_user=True,
    link_names=True)
fantasticGifToPost = random.randint(0, len(fantasticGifs) - 1)

slack_client.api_call(
    "chat.postMessage",
    channel="general",
    text="You must answer the call of duty!",
    as_user=True)

slack_client.api_call(
    "chat.postMessage",
    channel="general",
    text=fantasticGifs[fantasticGifToPost],
    as_user=True)

for user in user_list.get("members"):
    if user.get("name") == "bottington":
        slack_user_id = user.get("id")
        break
if slack_client.rtm_connect():
    print("Connected!")
