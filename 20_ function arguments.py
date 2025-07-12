# def average(a, b):
#     print("The average is ", (a+b)/2)
 
#     average(4,6)   
#     # average(b=9)
#     # average(a=19, b=21)


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
      sum = sum + i
    # print("Average is: ", sum / len(numbers))
    return sum / len(numbers)
    
c = average(5, 6) 
print(c)


# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])
    
# name(mname = "Buchanan", lname = "Barnes", fname = "James")
    
    