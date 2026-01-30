def wrapper(f):
    def inner():
        print("before")
        f()
        print("after")
    return inner()
@wrapper
def hi():
    print("hi")

hi()


