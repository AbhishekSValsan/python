
def test_function(a,b,*therest):
  print("The numbers are {0}, {1} and {2}.".format(a,b,list(therest)))

test_function(1,2,3,4,5,6,7)