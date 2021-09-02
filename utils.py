import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_token():
	try:
		data = {
			'grant_type': 'client_credentials',
			'client_id': os.environ.get("CLIENT_ID"),
			'client_secret': os.environ.get("CLIENT_SECRET"),
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
		req = requests.get(f'{os.environ.get("INTRA_URL")}/v2/campus', headers=headers)
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
		url = f'{os.environ.get("INTRA_URL")}/v2/cursus/{os.environ.get("PARIS_ID")}/events'
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
		url = f'{os.environ.get("INTRA_URL")}/v2/events/{event_id}'
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
		url = f'{os.environ.get("INTRA_URL")}/oauth/token?grant_type=authorization_code&client_id={os.environ.get("CLIENT_ID")}&client_secret={os.environ.get("CLIENT_SECRET")}&code={code}&redirect_uri={os.environ.get("REDIRECT_URI")}&state={os.environ.get("STATE")}'
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
		url = f'{os.environ.get("INTRA_URL")}/v2/users/{uid}/events_users'
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
		url = f'{os.environ.get("INTRA_URL")}/v2/events/{event_id}/events_users'
		req = requests.get(url, headers=headers)
		if req.status_code != 200:
			raise Exception('get_user_access_token error, status_code != 200')
		return (req.json())
	except Exception as e:
		print(e)
		return False
