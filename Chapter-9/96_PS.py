word=input("Which word you want to search :")

with open('/workspaces/Python101/Chapter-9/poem.txt','r') as f:
    for line in f:
        if word in line:
            print(line)