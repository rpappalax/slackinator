import os
import json

import requests
import slack


webhook = os.environ['SLACK_WEBHOOK']

# TBD: add a function to generate a dynamic message
message = 'new message here 12/11/2020-  B'

#slack_data = {'text': "This is a test message 12/11/2020"}
slack_data = {'text': message } 

response = requests.post(
    webhook, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
