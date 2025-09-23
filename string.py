a= "python"
print(len(a))
a= "python      is       great.      "
print(a.strip()) 

a = "python"
print(a.upper())
a = "PYTHON"
print(a.lower())
a= "Hello World"
print(a.replace("H","J"))
print(a)
a = "Mashup, Stack"
b = a.split(",") 
print(b)

str_test= "Python has a design philosophy that emphasizes code readability"
a= "Python" not in str_test
print(a)

str_1 = "Hello"
str_2 = "World"

print("str_1+str_2 =" , str_1 + str_2)
print(str_1 *3)