import sys

def send_message_to_slack(text):
    from urllib import request, parse
    import json
 
    post = {"text": "{0}".format(text)}
    
    try:
        json_data = json.dumps(post)
        req = request.Request("Your Slack URL goes here",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
if len(sys.argv) <= 0:
    print("you did not give any arguments")
else:
	send_message_to_slack(sys.argv[1:])
