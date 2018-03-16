from slackclient import SlackClient
import config
import SlackBot_Class

global slack_client

class Handler(object):
    def __init__(self, bot_name):
        self.bot_name = bot_name
        
        if bot_name == "bottington":
            # Redundant for now.
            slack_client = SlackClient(config.api_key_bottington)
        else:
            slack_client = SlackClient(config.api_key)
        if slack_client.rtm_connect():
            print("Connected!")
            # bottington = SlackBot_Class.SlackBot(bot_name)
        else:
            print("Not connected!")
            
    def ReturnBot(self, slack_bot):
        slack_bot = SlackBot_Class.SlackBot(self.bot_name)
        print("Returning connected bot.")
        return slack_bot
