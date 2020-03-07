may_list = [1,2,3,4,5]
def f(x):
    return x ** 2

result = map(f,may_list)
print(result)
print(type(result))
print(list(result))