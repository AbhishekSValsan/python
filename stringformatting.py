a ="dogs"
print("I Love {0}".format(a))

print("I Love {a}".format(a='cats'))

a= "cats"
b= "ferrets"
print("I love %s and %s" %(a,b))

age = 50
test= "walter is {} years old"
print(test.format(age))


language = "Python"
framework = "Django"
version_django = 2 
stack = "  Framework is {1} , ,and its version is  {2:.1f} , {0} is a programming language."
print(stack.format(language, framework, version_django))

greeting = "welcome to {company}, and {motto} "
print(greeting.format(company="mashupstack",motto="skill up. get hired"))