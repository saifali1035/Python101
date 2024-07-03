list=['word1','word2','word3','word4']

for item in list:
    with open('/workspaces/Python101/Chapter-9/Censor.txt','r') as f:
        filedata=f.read()

    newdata=filedata.replace(item,'#########')

    with open('/workspaces/Python101/Chapter-9/Censor.txt', 'w') as f:
        f.write(newdata)


