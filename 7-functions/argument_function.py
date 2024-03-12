def add(num1,num2=9):
    print(num1,"+",num2,"=",num1+num2)

add(7)



# not modify the original list
def myhobbies (hobbies):
    hobbies  = hobbies[:]
    hobbies[0] = "basketball"

hobbies = ['Reading','Writing','Coding']

print(hobbies)

myhobbies(hobbies)

print(hobbies)