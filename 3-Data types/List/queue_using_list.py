
# queue implementation  in pyhton using list

queue = []
while True:
  choice = input("1 to add element\n2 to delete element\n3 see front element\n4 to exit\n5 display queue: ")
  if choice=="1":
    value = int(input("enter  a number:"))
    queue.append(value)
  elif choice=="2":
    if (len(queue)==0):
      print("queue is empty")
    else:
      del  queue[0]
  elif choice == "3":
    if (len(queue)==0):
      print("queue is empty")
    else:
      print(queue[0])
  elif choice=="4":
    break
  elif choice=="5":
    if  len(queue)==0:
      print("empty queue")
    else:
      print(queue)
  else:
    print("invallid choice")      
    

      
