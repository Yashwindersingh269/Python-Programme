# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)


tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
# res = tuple1.index(3, 4, 8)
print('Count of 3 in tuple1 is:', res)