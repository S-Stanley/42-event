import json, datetime, itertools
from utils import get_events, get_token
from send_email import send_email_gmail

def filter_nonprintable(text):
	nonprintable = itertools.chain(range(0x00,0x20),range(0x7f,0xa0))
	return text.translate({character:None for character in nonprintable})

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

def get_french_date(moment: str):
	year = moment.split('T')[0].split('-')[0]
	mois = moment.split('T')[0].split('-')[1]
	jour = moment.split('T')[0].split('-')[2]
	heure = moment.split('T')[1].split(':')[0]
	minute = moment.split('T')[1].split(':')[1]
	return (f'{jour}/{mois}/{year} - {heure}h{minute}')

def get_today_event():
	'''
		This function get through each event and check if it's today.
		Should be call every 24h
	'''
	with open('events.json', 'r') as f:
		events = json.loads(f.read())
	for event in events:
		now = datetime.datetime.now()
		moment = datetime.datetime.strptime(event['begin_at'].split('.')[0], "%Y-%m-%dT%H:%M:%S")
		if (moment-now).days == 0:
			with open('email_to_send.txt', 'r') as f:
				msg = f.read().format(
				filter_nonprintable(event['name']),
				filter_nonprintable(event['location']),
				filter_nonprintable(get_french_date(event['begin_at'])),
				filter_nonprintable(event['description']),
			)
			send_email_gmail(['stanleyserbin@gmail.com'], msg.replace("’", "'"))

#get_event_and_store_it()
get_today_event()