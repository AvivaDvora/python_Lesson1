def invetory_summary(dic):
    sum = 0

    for value in dic:
        sum = int(dic[value][0]) * int(dic[value][1]) + sum
    return sum

x={"leben": (20, 10), "det":(3,5)}
print(invetory_summary(x))


def print_args_kwargs(*args , **kwargs):
    for v in args:
        print(f'{v}')
    for key, value in kwargs.items():
        print(f'{key} = {value}')
print(print_args_kwargs(1,2,3,4,a=1,b=2,c=3))