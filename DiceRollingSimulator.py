import  random
class Dices(object):
    def Random1(self):
        r = list(range(1,7))
        print("You Got:",random.choice(r))

d = Dices()

while True:
    n = input("Press any to Roll a dice..!\n Press X to Exit:")
    if n == 'X' or n == 'x':
        break
    else:
        d.Random1()
