import requests

r = requests.get('https://api.github.com/events')

payload = {'niger1': '30', 'niger2': '20'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)
print(r.content)
