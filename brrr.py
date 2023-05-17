import random

b=round(random.uniform(2,40),2)

print(b)

try:

    if b != int:

        print("error")

except(ValueError):

    if b == 50:

        print("not error")



