# a = input("Enter the number:")
# print(f"Multiplication table of {a} is:")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("Invalid Input")   
# print("Some inportant lines of code")
# print("End of programme")



try:
    num = int(input("Enter an integer:"))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not integer.")
    
except IndexError:
    print("Index Error")
    


