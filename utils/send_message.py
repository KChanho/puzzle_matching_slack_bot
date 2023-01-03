import re
import os
import json
from key_manager import KeyManager
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
manager = KeyManager()
app = App(token=manager.get_bot_token())

def send_as_puzzle(channel, msg=None,block=None):
    app.client.chat_postMessage(channel=channel,text=msg,blocks=block)

if __name__ == '__main__':
    puzzle_channel = 'C04GTGWME1X' # 퍼즈리-지역기반매칭
    test_channel = "C04GD37D6DN" # puzzle-test
    with open(os.path.join('json','test_message.json')) as f:
        block = json.load(f)['blocks']
    send_as_puzzle(test_channel,block=block)