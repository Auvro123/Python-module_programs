lines=["this is first line.","this is second line.","this is third line"]

with open("file.txt","w") as fp:
    for line in lines:
        fp.write(line+"\n")
with open("file.txt","r") as fp:
    content = fp.read()
    print(content)
with open("file.txt","r") as fp:
    for line in fp:
        print(line)
with open("file.txt","r") as fp:
    lines = fp.readlines()
    print(lines)
    for line in lines:
        print(line)