myinformation = {
    "name":"anees ur rehman",
    "age":22,
    "add":"Islamabad Pakistan",
    "email":"aneesurrehman47@gmail.com"
}


# for key in myinformation:
#     print(key,"\t:",myinformation[key])


# print("\n",myinformation["email"])

# print("\n=============dictionary functions===============\n")

# print("\n=============get functions===============\n")

# # it is work on key
# print(myinformation.get("name"))

# print("\n=============keys functions===============\n")

# # it is use to get keys from dictionary
# for k in myinformation.keys():
#     print(k)

# print("\n=============values functions===============\n")

# # it is use to get values from dictionary
# for v in myinformation.values():
#     print(v)

# print("\n=============values functions===============\n")

# it is use to get both keys and values from dictionary
# for k,v in myinformation.items():
#     print(k,":",v)



# print("\n=============del and pop functions===============\n")

# del not return the deleted value
# del myinformation["add"] 
# print(myinformation)

# # pop return deleted value
# deletd_value = myinformation.pop("email") 
# print("deleted value : ",deletd_value)

# print("\n=============update functions===============\n")

# myinformation.update({'name':'umer'})
# print(myinformation)
