marks = [12, 56, 32, 98, 12, 45, 1, 4]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Harry, awesome!")
#     index +=1  

for index, marks in enumerate(marks):
    print(marks)
    if(index == 3):
        print("Harry, awesome!")
    index +=1  
