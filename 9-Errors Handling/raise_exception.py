def addnumbers(a,b):
    try:
        if(isinstance(a,int) and isinstance(b,int)):
            print(f"{a} + {b} = {a+b}")
        else:
            raise Exception("only integres can add\n")
    except Exception as error:
        print(error)


addnumbers(5,"6")  # this will give an exception because we are trying to add a string with
addnumbers(2,3)