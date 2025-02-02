def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))