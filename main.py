import os
import requests
import json
import aiocron
import asyncio


channel = os.getenv("channel")
token = os.getenv("token")
observable_resource = os.getenv("observable_resource")


data = {
    "channel": channel,
    "text": "<!channel> [PRODUCTION} server is down!",
    "icon_emoji": ":x:",
}

json_data = json.dumps(data)


@aiocron.crontab("* * * * *")
def ping_server():
    """
    Function pings the specific resource every minute 
    If resource is unavailable then send message to Slack
    """

    try:
        requests.get(f"{observable_resource}")
    except requests.exceptions.RequestException:
        requests.post(
            "https://slack.com/api/chat.postMessage",
            data=json_data,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )


asyncio.get_event_loop().run_forever()
