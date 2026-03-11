import requests

requests_bbc = requests.get('https://www.bbc.co.uk')

print(requests_bbc.status_code)

print(requests_bbc.content)