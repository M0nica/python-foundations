
import config
import requests


key = config.mailgun_key
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox6e6a92af0098467b96a693d5b2941ec4.mailgun.org/messages",
        auth=("api", key),
        data={"from": "Mailgun Sandbox <postmaster@sandbox6e6a92af0098467b96a693d5b2941ec4.mailgun.org>",
              "to": "Monica <mmp2181@columbia.edu>",
              "subject": "Hello Monica",
              "text": "Congratulations Monica, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})


send_simple_message()
# import requests
#import config
# key = config.mailgun_key
# sandbox = 'https://api.mailgun.net/v3/sandbox6e6a92af0098467b96a693d5b2941ec4.mailgun.org/'
# recipient = 'mmp2181@columbia.edu'
#
# request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
# request = requests.post(request_url, auth=('api', key), data={
#     'from': 'hello@example.com',
#     'to': recipient,
#     'subject': 'Hello',
#     'text': 'Hello from Mailgun'
# })
#
# print 'Status: {0}'.format(request.status_code)
# print 'Body:   {0}'.format(request.text)
#
