# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1, s2) 


# cities = {"Tokyo", "Madrid","Berlin","Delhi"}
# cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)


cities = {"Tokyo", "Madrid","Berlin","Delhi"}
cities2 = {"Tokyo", "Seoul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))
print(cities3.issuperset(cities))
