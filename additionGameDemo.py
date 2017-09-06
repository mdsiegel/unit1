#Matthew Siegel
#9/6/17
#additionGameDemo.py - our first "game"

from random import randint
numberOne = randint(1,10)
numberTwo = randint(1,10)
answer = int(input(str(numberOne)+'+'+ str(numberTwo)+'?'+' ' ))

print(answer == numberOne + numberTwo)

