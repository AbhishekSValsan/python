number_int = 123
number_str = "456"

print("number_int", type(number_int))
print("number_str", type(number_str))

number_str = int(number_str)
print("number_str", type(number_str))
number_sum = number_int+number_str

print("sum of int and nmber out", number_sum)
print("data Type",type(number_sum))


