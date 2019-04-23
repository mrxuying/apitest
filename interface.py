import requests

url = "http://127.0.0.1:8000/api/get_event_list/"
request = requests.get(url,params = {'eid':'1'})
result = request.json()
