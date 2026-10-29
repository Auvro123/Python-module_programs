import re
s = "Afganistan, Bangladesh,canada,denmark,England,Greenland,Iceland,Netherlands$,New Zealand,switzerland"
li  = re.findall(r'(\w+lands*)',s)
print(li)