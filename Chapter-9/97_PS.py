with open('/workspaces/Python101/Chapter-9/Donkey.txt','r') as f:
    content=f.read()

with open('/workspaces/Python101/Chapter-9/Copy_Donkey.txt','w') as f:
    f.write(content)