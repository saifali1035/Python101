import os

#creating dir for user
dir_name=input("Enter your name:")
new_path="/workspaces/Python101/Chapter-9/"+dir_name

#checking if path exists or not
if not os.path.exists(new_path):
    os.makedirs(new_path)

#loop to create files
for i in range(1,11):
    i=str(i)
    file_name=new_path+"/"+i+".txt"
    with open(file_name,'w') as f:
#loop to create tables ( Print function can also write to files )
        for j in range(1,11):
            i=int(i)
            k=i*j
            print(i,'x',j,'=',k, file=f)
            


