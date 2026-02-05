def greet():
    print("Hello")
    greet()
try:
    greet()
except RecursionError:
    print("Recursion stops")
