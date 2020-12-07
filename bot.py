import os
import slack

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
message = 'new message here from chat_postMessage 12/11/2020'
channel = 'test-infra-alerts'
client.chat_postMessage(channel=channel, text=message)
