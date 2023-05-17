# my_list=[1,2,3,4,5,6]
# iterator=iter(my_list)
# for elem in iterator:
# print(elem)

class Counter:
    def __init__(self, max_number):

        self.i = 0

        self.max_number = max_number

    def __iter__(self):
        self.i = 0

        return self

    def __next__(self):
        self.i += 1

        if self.i > self.max_number:
            raise StopIteration
        return self.i
count = Counter(5)
for elem in count:
    print(elem)

def raise_to_the_dergees(number, max_dergees):
    i = 0

    for _ in range(max_dergees):
        yield number ** i
        i += 1
res = raise_to_the_dergees(122345, 500)
print(res)
for _ in res:
    print(_)