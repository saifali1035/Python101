with open('/workspaces/Python101/Chapter-9/Donkey.txt','r') as f :
    filedata = f.read()

newdata=filedata.replace('Donkey','#####')

with open('/workspaces/Python101/Chapter-9/Donkey.txt','w') as f :
    f.write(newdata)