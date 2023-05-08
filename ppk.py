#print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
#print(f"ImportError - {type(ImportError)} - {issubclass(ImportError, BaseException)}")
print("hi")
try:
    print("start")
    print(10/0)
    print("no error")
except (ZeroDivisionError, NameError):
    print("we have an error")
    print("code after capsule")

def checker(var_1):
    if type(var_1)!=str:
        raise TypeError(f"Sorry,we can't work with {type(var_1)}", f"we need class str")
    else:
        return var_1
first_var=10
checker(first_var)