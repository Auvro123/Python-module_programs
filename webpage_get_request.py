import requests
url = "http://example.com"
response = requests.get(url)
print(response.content)
print(type(response))
print(dir(response))
print(response.reason)
print(response.ok)
print(response.status_code)
print(response.text)