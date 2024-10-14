# def f(x):
#     y = 3*x
#     return y

# solution= f(40)
# print(solution)

# n= 4
# for i in range (2,n):
#     print(i)


def f(x):
    for d in range(2,x):
        if x %d == 0:
            return d
     
f(15)