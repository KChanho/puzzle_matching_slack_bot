import os
import re
import json
import time
from key_manager import KeyManager
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
manager = KeyManager()
app = App(token=manager.get_bot_token())
poll = re.compile(r'\bpoll\b')

def open_chatroom(users:list):
    response = app.client.conversations_open(users=users)
    room_channel = response["channel"]["id"]
    app.client.chat_postMessage(channel=room_channel,text='Open Chat Room Successful!')

if __name__ == '__main__':
    user_list = ['userids']
    open_chatroom(user_list)
