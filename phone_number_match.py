import re
text = "phone number : 01746200230"
match = re.search('\d+',text)
print(match.group())

text = "house : 1 ,phone number:01746200230"
match = re.search('\d+', text)
print(match.group())

text = "house : 1 ,phone number:01746200230"
match = re.search('\d{11}', text)
print(match.group())

text = "house : 1 ,phone number:01746200230"
match = re.search('\d{11}', text)
print(match)

text = "house : 1 ,phone number:01746200230"
match = re.search('\d{3}\s*\d{8}', text)
print(match.group())

text = "multipule phone number,00000000000,12345678910,12343333333,17888888888,10101010910  123-123"
result = re.findall(r'\d{3}\s*\d{8}',text)
print(result)

text = "multipule phone number,00000000000,12345678910,12343333333,17888888888,10101010910  123-123"
result = re.findall(r'01[56789]\s*\d{8}',text)
print(result)

s = "Bangla english Bangla"
print(re.findall(r'english',s))
print(re.findall(r'^english',s))
print(re.findall(r'english$',s))
print(re.findall(r'^Bangla',s))
print(re.findall(r'bangla$',s))
