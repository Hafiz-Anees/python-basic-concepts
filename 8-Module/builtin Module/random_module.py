import random


print("================For integr value=========================\n")
print(random.randint(1,10)) # both 1 and 10 included

print(random.randrange(1,10)) # 1 include but 10 not included


print("================For float value=========================\n")

print(random.random()) # returns a float number between 0 to 1

print(random.uniform(1,9)) # returns a float number between 1 to 9

print("================For list values=========================\n")

print(random.choice(["apple","banana","cherry"])) # select item from list randomly

print(random.sample([1,2,3,4,5,6],3)) 

numbers = [1,2,3,4,5,6,7]

random.shuffle(numbers) # shuffles the numbers in place (changes the original list

print(numbers)