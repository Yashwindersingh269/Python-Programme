import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
name = input(" Enter your name ")
print(name)
# print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
if(hour>=17 and hour<0):
    print("Good Night Sir!")
        