s ="Afganistan, Bangladesh,canada,denmark,England,Greenland,Iceland,Netherland,New Zealand,switzerland"
countries = s.split(",")
print(countries)
li = [item for item in countries if item.endswith("land")]
print(li)