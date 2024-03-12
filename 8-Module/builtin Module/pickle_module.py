import pickle

myname = "my name is umer"

file = open("myinfo.txt","wb")
# file = open("myinfo.txt","rb")

pickle.dump(myname,file)

# data = pickle.load(file)

# print(data)

file.close()