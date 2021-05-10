import requests

__INTRA_42_URL__ = 'https://api.intra.42.fr'
__42_PARIS_ID__ = '42'
__CLIENT_ID__ = '21281d0f6367b3851dc2419e163ec791cbac92f943feb7ba989897693f61d854'
__CLIENT_SECRET__ = '3a6deb21b02945771acb618f1b0eb18edf80815fd03286de1866ecfd47197add'
__REDIRECT_URI__ = 'http://localhost:8000/42/callback'
__STATE__ = '42EVENTS'

def get_token():
	try:
		data = {
			'grant_type': 'client_credentials',
			'client_id': __CLIENT_ID__,
			'client_secret': __CLIENT_SECRET__,
		}
		req = requests.post('https://api.intra.42.fr/oauth/token', data=data)
		if req.status_code != 200:
			raise Exception('get_token function, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False

def get_campus(access_token: str):
	try:
		headers = {
			'Authorization': f'Bearer {access_token}',
		}
		req = requests.get(f'{__INTRA_42_URL__}/v2/campus', headers=headers)
		if req.status_code != 200:
			raise Exception('get_campus function, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False

def get_events(access_token: str):
	try:
		headers = {
			'Authorization': f'Bearer {access_token}',
		}
		print(headers)
		url = f'{__INTRA_42_URL__}/v2/cursus/{__42_PARIS_ID__}/events'
		req = requests.get(url, headers=headers)
		if req.status_code != 200:
			raise Exception('get_event function, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False

def get_event_by_id(access_token: str, event_id: str):
	try:
		headers = {
			'Authorization': f'Bearer {access_token}',
		}
		url = f'{__INTRA_42_URL__}/v2/events/{event_id}'
		req = requests.get(url, headers=headers)
		if req.status_code != 200:
			raise Exception('get_event_by_id function, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False

def get_user_access_token(access_token: str, code: str):
	try:
		headers = {
			'Authorization': f'Bearer {access_token}',
		}
		url = f'{__INTRA_42_URL__}/oauth/token?grant_type=authorization_code&client_id={__CLIENT_ID__}&client_secret={__CLIENT_SECRET__}&code={code}&redirect_uri={__REDIRECT_URI__}&state={__STATE__}'
		req = requests.post(url, headers=headers)
		if req.status_code != 200:
			raise Exception('get_user_access_token error, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False

def get_all_events_by_user(user_token: str, uid: str):
	try:
		headers = {
			'Authorization': f'Bearer {user_token}',
		}
		url = f'{__INTRA_42_URL__}/v2/users/{uid}/events_users'
		req = requests.get(url, headers=headers)
		if req.status_code != 200:
			raise Exception('get_user_access_token error, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False

def get_all_participants(access_token: str, event_id: str):
	try:
		headers = {
			'Authorization': f'Bearer {access_token}',
		}
		url = f'{__INTRA_42_URL__}/v2/events/{event_id}/events_users'
		req = requests.get(url, headers=headers)
		if req.status_code != 200:
			raise Exception('get_user_access_token error, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return Fals