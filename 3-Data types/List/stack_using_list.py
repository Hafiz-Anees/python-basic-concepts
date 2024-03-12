
# stack implementation in python using list (LIFO)

stack = []
while True:
  choice = input("1 to push element\n2 to pop element\n3 to peek element\n4 to exit\n5 display stack: ")
  if choice == "1":
    value = int(input("Enter the value to push: "))
    stack.append(value)
  elif choice=="2":
    if len(stack) == 0:
      print("Stack is empty\n")
    else:
      stack.pop()
  elif choice=="3":
    if len(stack) == 0:
      print("Stack is empty\n")
    else:
      print("\n",stack[-1],"\n")
  elif choice=="4":
    break
  elif choice=="5":
    if(len(stack)==0):
      print("\nStack is empty\n")
    else:
      print("\n",stack)
  else:
    print("\nInvalid choice")

