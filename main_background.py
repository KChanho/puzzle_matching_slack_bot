import os
import re
import json
import time
import csv

from key_manager import KeyManager
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


# Initializes your app with your bot token and socket mode handler
manager = KeyManager()
app = App(token=manager.get_bot_token())
poll = re.compile(r'\bpoll\b')


@app.event("app_mention")  # 앱을 언급했을 때
def who_am_i(event, client, message, say):
    print('message:', event['text'])
    with open('./json/mention_form.json') as f:
        mention_form = json.load(f)
    say(mention_form)


@app.shortcut("open_form")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    with open('./json/puzzle_form.json') as f:
        form_view = json.load(f)
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view=form_view
    )


# Handle a view_submission request
@app.view("open_view")
def handle_submission(ack, body, client, view, logger):
    # Assume there's an input block with `input_c` as the block_id and `dreamy_input`
    name = view["state"]["values"]["name_block"]["name_action"]['value']
    location = view["state"]["values"]["location_block"]["location_action"]['selected_options']
    location = [l["value"] for l in location]
    date = view["state"]["values"]["date_block"]["date_action"]['selected_options']
    date = [d["value"] for d in date]
    user = body["user"]["id"]

    # Validate the inputs
    errors = {}
    if name is not None and len(name) <= 5:
        errors["input_c"] = "The value must be longer than 5 characters"
    if len(errors) > 0: # 숏컷 에러 메세지는 어떻게해야 수정해서 띄울 수 있을까?
        ack(response_action="errors", errors=errors)
        return
    
    # Acknowledge the view_submission request and close the modal
    ack()

    # Message to send user
    msg = ""
    try:
        # Save to DB
        msg = f"{name} 캠퍼님의 \n\n{date} 날짜 \n{location} 지역 \n\n매칭 신청은 성공적으로 접수되었습니다."
    except Exception as e:
        # Handle error
        msg = "매칭 신청에 오류가 있습니다!"

    # Message the user
    try:
        client.chat_postMessage(channel=user, text=msg)
    except e:
        logger.exception(f"Failed to post a message {e}")

    # 데이터 저장
    with open('./data/test.csv', 'a', newline='') as csvfile:
        ar = csv.writer(csvfile)
        for d in date:
            for l in location:
                ar.writerow([user, name, l, d])


@app.shortcut("close_form")
def close_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    with open('./json/close_form.json') as f:
        form_view = json.load(f)
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view=form_view
    )


@app.view("close_view")
def handle_cancel(ack, body, client, view, logger):
    # Assume there's an input block with `input_c` as the block_id and `dreamy_input`
    name = view["state"]["values"]["name_block"]["name_action"]['value']
    user = body["user"]["id"]

    # Validate the inputs
    errors = {}
    if name is not None and len(name) <= 5:
        errors["input_c"] = "The value must be longer than 5 characters"
    if len(errors) > 0: # 숏컷 에러 메세지는 어떻게해야 수정해서 띄울 수 있을까?
        ack(response_action="errors", errors=errors)
        return
    
    # Acknowledge the view_submission request and close the modal
    ack()

    # Message to send user
    msg = ""
    try:
        # Save to DB
        msg = f"{name} 캠퍼님의 매칭 신청은 정상적으로 취소되었습니다."
    except Exception as e:
        # Handle error
        msg = "매칭 취소에 오류가 있습니다!"

    # Message the user
    try:
        client.chat_postMessage(channel=user, text=msg)
    except e:
        logger.exception(f"Failed to post a message {e}")

    # 데이터 저장
    with open('./data/cancel.csv', 'a', newline='') as csvfile:
        ar = csv.writer(csvfile)
        ar.writerow([user, name])


if __name__ == '__main__':
    SocketModeHandler(app, manager.get_app_token()).start()
