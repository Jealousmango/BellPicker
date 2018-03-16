import re
import json
from slackclient import SlackClient
import config
import SlackBot_Handler 

class SlackBot(object):
    slack_client = SlackClient(config.api_key_bottington)
    def __init__(self, bot_name):
        slack_client = SlackClient(config.api_key_bottington)
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
        # while True:
        #     for message in slack_client.rtm_read():
        #         if "text" in message and message["text"].startswith("<@%s>" % slack_user_id):
        #             print("Message received: %s" % json.dumps(message, indent=2))
        #             message_text = message['text']. \
        #                 split("<@%s>" % slack_user_id)[1]. \
        #                 strip()

        #             if re.match(r'.*(ding).*', message_text, re.IGNORECASE):
        #                 slack_client.api_call(
        #                     "chat.postMessage",
        #                     # channel = "general",
        #                     channel="alert",
        #                     text="Selecting a winner...",
        #                     as_user=True)

    def send_message(self, message_contents, channel):
        if slack_client.rtm_connect() == "False":
            print("Cannot send message before connecting to Slack!")
            return False
        else:
            slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=message_contents,
                as_user=True)

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
