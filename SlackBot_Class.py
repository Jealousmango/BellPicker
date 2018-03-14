import re
import json
from slackclient import SlackClient
import config

class SlackBot(object):
    def __init__(self, bot_name, message_contents, channel):
        super(SlackBot, self).__init__()
        self.bot_name = bot_name
        if bot_name == "bottington":
                slack_client = SlackClient(config.api_key_bottington)
        else:
            slack_client = SlackClient(config.api_key)
            user_list = slack_client.api_call("users.list")
        for user in user_list.get("members"):
            if user.get("name") == bot_name:
                slack_user_id = user.get("id")
                break
        if slack_client.rtm_connect():
            print("Connected to slack as ", bot_name)

        # def connect_to_slack(self, bot_name):
        #     if bot_name == "bottington":
        #         slack_client = SlackClient(config.api_key_bottington)
        #     else:
        #         slack_client = SlackClient(config.api_key)
        #     user_list = slack_client.api_call("users.list")
        #     for user in user_list.get("members"):
        #         if user.get("name") == bot_name:
        #             slack_user_id = user.get("id")
        #             break

        #     if slack_client.rtm_connect():
        #         print("Connected to slack as ", bot_name)

    def send_message(self, message_contents, channel):
        if slack_client.rtm_connect():
            print("Cannot send message before connecting to Slack!")
            return False
        else:
            slack_client.api_call(
            "chat.postMessage",
            channel = channel,
            text = message_contents,
            as_user = True)
        
