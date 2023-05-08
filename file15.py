import requests

def first_func():
    pass
class Human:
    pass

rq=requests
first=first_func
nick=Human

print(requests.__name__)
print(rq.__name__)
print(first.__name__)
print(first_func.__name__)
print(Human.__name__)
print(nick.__name__)
print(__name__)

print(type(2))
print(type(2.1))
print(type(2==2))
print(type("hfd"))

into_list=[]
for method in dir(into_list):
    print(method)

into_dict={}
for method in dir(into_dict):
    print(method)


