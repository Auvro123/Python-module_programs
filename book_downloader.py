import requests
import sys

base_url = input("Please enter url: ", ) or "https://bugs.python.org/file47781/Tutorial_EDIT.pdf"
name = input("Please enter name of the book: ", ) or "cpbook"

info_dt = {"name":"auvro","email":"book@subeen.com","country":"Bangladesh"}

response = requests.get(base_url)

if response.ok is False:
    print(response.status_code)
    sys.exit("Error downloading the file .")
    
with open(f"{name}.pdf","wb") as fp:
    fp.write(response.content)
print("✨ Book download completed Successfully ✔✨!")
    