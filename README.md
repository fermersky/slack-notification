# Slack Notifications

Very simple python script for monitoring the specific web-resource and sending notifications in slack if resource is unavailable


```python
@aiocron.crontab("* * * * *")
def ping_server():
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
```
