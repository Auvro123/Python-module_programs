import re 
match = re.search('Bangla','Bangladesh')
print(match)
print(match.group())
match  = re.search('desh','Bangladesh')
print(match.group())
match = re.search('des','Bangladesh')
print(match.group())
print(match)
print(type(match))
print(match is None)

s = "Bangladesh"
match =re.search('.',s)
print(match.group())
match = re.search('B.n',s)
print(match.group())
match = re.search('B.n...',s)
print(match.group())
s = "Bangladesh is my homeland"
match = re.search('..............',s)
print(match.group())
 
s = "Bangladesh is my homeland"
match = re.search("o\w\w",s)
print(match.group())
match = re.search("i\w\w",s)
print(match)

s = "Bangladesh is my homeland"
match = re.search('B\w+h',s)
print(match.group())

match = re.search('B.+h',s)
print(match.group())

match = re.search('B.+?h',s)
print(match.group())