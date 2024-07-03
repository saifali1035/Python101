with open('/workspaces/Python101/Chapter-9/poem.txt') as f:
    words=f.read()

if "twinkle" in words:
    print("Word Found !")
else:
    print("Word not Found !")