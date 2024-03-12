

'''
A function can take one or more functions as parameters

'''
print("\n=======================Function as a argument=======================\n")
def sum_numbers(nums):
    return sum(nums)    

def higher_order_function(call, lst): # call is getting sum_number function as an argument
    summation = call(lst)   # calling sum_number function using call 
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15



