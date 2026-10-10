import builtins
import math
import datetime
import webbrowser

# print(dir(builtins))


print(math.pi)
print(math.pow(2,4))
print(math.floor(9.22))

today = datetime.date.today()
print(today)
today =datetime.datetime.today()
print(today)
print("\n")

names_list={
    1 : "doremon 3 swordsman movie",
    2 : "pakdam-pakdai",
    3 : "islamic story",
    4 : "ninja-hatori",
    5 : "pokemon-journeys",
    6 : "pokimon-xy",
    7 : "robin-hood",
    8 : "perman"

}

urls_list={
    "doremon 3 swordsman movie" : "https://www.facebook.com/61587184886009/videos/m06-doraemon-the-movie-nobitas-three-magical-swordsmen-in-hindi/894626316256275/",
    "pakdam-pakdai" : "https://www.youtube.com/watch?v=IYpcdvPkeQc",
    "islamic story" : "https://www.youtube.com/watch?v=lS_R1FeGgkg",
    "ninja-hatori"  : "https://www.youtube.com/watch?v=0mkIS5Rq-Bs",
    "pokemon-journeys" : "https://www.youtube.com/watch?v=7L5nNb1jbhA&list=PLHx6e5LqFO7ixggO1CIKbTKPgV729G0LP&index=128",
    "pokimon-xy" : "https://www.youtube.com/watch?v=X_N2--zf5YM&list=PLxjFnCWdSoEUR0iBvTDaTrCVeAn7_fi1E&index=12",
    "robin-hood" : "https://www.youtube.com/watch?v=NCXWqlGj0K8",
    "perman" : "https://www.youtube.com/watch?v=k7SqFtVgYSw"
}


for key,value in names_list.items():
    print(key," : ",value)

coose = int(input("choose any number : "))
name=names_list[coose]
webbrowser.open(urls_list[name])