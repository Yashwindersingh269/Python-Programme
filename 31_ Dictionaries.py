# dic = {
#     # "Harry": "Human being",
#     # "Spoon": "Object"
#     344: "Harry",
#     56: "Shubam",
#     678: "Zakir",
#     567: "Neha"
# }

# print(dic["567"])


info = {'name':'Karan', "age":19, 'eligible':True}
# print(info)
# # print(info['name'])
# # print(info.get('name2'))

# print(info.keys()) 
# print(info.values()) 

# for key in info.keys():
#     print(info[key])

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
