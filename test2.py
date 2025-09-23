python = {"akash","akshay","john"}
data_science = {"alex","sam","aswin","sandeep","john"}

python.add("adwait")
print(python)

data_science.remove("sam")
print(data_science)

print(python & data_science)

print(python - data_science)

print(python | data_science)

course = {

"python" : 4 ,
"data_science" : 4, 

}
print(course)

if "python" in course:

 print("course:python,students:4")

 mycourse = dict(course)
 print(mycourse)

 square = {x: x*x for x in range(6)}
 print(square)