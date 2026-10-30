with open("file.txt","r") as f:
    text = f.read()
print(text)
import re
print(re.findall(r'^.*?$', text))
print(re.findall(r'^.*?$', text,re.MULTILINE))