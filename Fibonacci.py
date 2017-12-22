class Fibonacci(object):
    def fib(self,n):
        a,b =0,1
        for i in range(n):
            a,b=b,a+b
        return a
while True:
        n1 = input("Enter the Fibonacci number, Press X to Exit:")
        if n1 == 'x' or n1 == 'X':
            break
        else:
            try:
                n = int(n1)
                F = Fibonacci()
                print(F.fib(n))
            except:
                print("Please Enter Integers only")




