f=open("this.txt","w+")
print(f.write("this is nice"))
data=f.read()
print(data)
f.close()