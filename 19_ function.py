def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a, b):
  if(a>b):
    print("First number is grater ")
  else:
    print("Second number is grater or equal")

a = 9
b = 8
calculateGmean(a, b)
isGreater(a, b)

c = 10
d = 10
calculateGmean(c, d)
isGreater(c, d)
