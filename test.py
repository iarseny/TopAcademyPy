import requests

response = requests.get('https://google.com')

#print(response.content.decode())
print(response.text)
print(response.headers)