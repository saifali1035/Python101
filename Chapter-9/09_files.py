r=open("/workspaces/Python101/Chapter-9/sample.txt", "r")
data=r.read()
r.close()
print(data)


w=open('/workspaces/Python101/Chapter-9/sample_2.txt', 'w')
w.write("This new file is created now !")
w.close()


a=open('/workspaces/Python101/Chapter-9/sample_2.txt','a')
a.write("\n Appended this line !")
a.close()


with open('/workspaces/Python101/Chapter-9/sample.txt', 'r') as f:
    f1=f.read()
print(f1)







