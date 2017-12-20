class Calculator(object):

    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return  a-b
    def multpilication(self, a,b):
        return a * b
    def division(self,a,b):
        return a//b
    def Calc(self):
        x = int(input())
        y = int(input())
        return x,y
C = Calculator()
while True:
    print("Please select the options:\n ADD,SUB,MUL,DIV,Break:")
    Choice = (input())
    if Choice == "ADD":
        num1, num2 = C.Calc()
        print(num1," + ",num2, "=",C.addition(num1,num2))
    elif Choice == "SUB":
        num1, num2 = C.Calc()
        print(num1," - ",num2, "=",C.subtraction(num1,num2))
    elif Choice == "MUL":
        num1, num2 = C.Calc()
        print(num1," * ",num2,"=", C.multpilication(num1,num2))
    elif Choice == "DIV":
        num1, num2 = C.Calc()
        print(num1," // ",num2,"=",C.division(num1,num2))
    elif Choice == "Break":
        print("Exit From the Calculator")
        break
    else:
        print("InValid Output")





