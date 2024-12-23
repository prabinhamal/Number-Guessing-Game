def a():
    print("function a()")
    b()
def b():
    print("function b()")
    a()
a()