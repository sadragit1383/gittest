def func():
    def func1():
        print('inside in func 1 ')
    def func2():
        print('inside in func 2')
    return func1() , func2()


print(func())