import json
from utils import get_events, get_token

def get_event_and_store_it():
	'''
		This function get every new event, should be call every 24h
		1. Get access token
		2. Get all events
		3. Store it in a file
	'''
	token = get_token()
	new_events = get_events(token['access_token'])
	with open('events.json', 'w') as f:
		f.write(json.dumps(new_events))

get_event_and_store_it()
