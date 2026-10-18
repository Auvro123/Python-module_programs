import requests

img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvM0G3Kg2D1iGpKktmtGlGWDHXTcfszkQROHhA0NxdAQ&s=10"
r = requests.get(img_url)
with open("pybook1.png","wb") as f:
    f.write(r.content)
   
