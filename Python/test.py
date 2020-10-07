def get_foo():
    return (1,2,3,4,5)

a,*_,c = get_foo()

print(a,c)