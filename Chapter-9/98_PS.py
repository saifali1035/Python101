first_file=input("What is the first file name :")
second_file=input("What is the second file name :")

full_path_first='/workspaces/Python101/Chapter-9/'+first_file
full_path_second='/workspaces/Python101/Chapter-9/'+second_file
with open(full_path_first,'r') as f :
    content1=f.read()

with open(full_path_second,'r') as f1 :
    content2=f1.read()

if content1==content2:
    print("Files are same")
else:
    print("Files are diff")