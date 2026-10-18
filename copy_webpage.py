import requests
import os
import webbrowser as wb

url = "https://github.com/Auvro123"
response =requests.get(url)

with open("github.html","w",encoding=response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath("github.html")
print(file_path)
wb.open("file://"+file_path)