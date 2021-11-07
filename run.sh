#!/bin/bash

# ================================================================================
# FOR MORE REFERENCE SEE https://api.slack.com/messaging/sending#sending_methods
# ================================================================================


# you have to make a GET request to https://slack.com/api/conversations.list with hour Bearer token
# to see the conversations list
channel="channel-id"

# token can be found in the Slack app page https://api.slack.com/apps [APP NAME] -> OAuth & Permissions
token="oauth token"

# resrouce url
observable_resource="https://example.org"

echo "🐱‍👤 Monitoring background task is watching 🦅 $observable_resource 🦅"

# & notation to run task in background
export observable_resource=$observable_resource channel=$channel token=$token && py main.py &