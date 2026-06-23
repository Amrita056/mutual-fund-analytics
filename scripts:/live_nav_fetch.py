import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print(response.status_code)