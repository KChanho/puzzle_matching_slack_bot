import json
import os

class KeyManager:
    def __init__(self, path='./json/'):
        self.values = dict()
        with open(os.path.join(path,'config.json')) as f:
            self.values = json.load(f)
    def get_app_token(self):
        return self.values['SLACK_APP_TOKEN']
    def get_bot_token(self):
        return self.values['SLACK_BOT_TOKEN']
