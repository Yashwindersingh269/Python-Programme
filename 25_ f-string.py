letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country} ")
print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollar! "
print(txt)
# print(txt.format(price = 49.099999))
print(type(f"{2 * 30}"))