#Matthew Siegel
#9/7/17
#binary.py - finding binary numbers

number = int(input('Enter an 8 diget binary: '))

one = number%10
two = (number//10)%10
three = (number//100)%10
four = (number//1000)%10
five = (number//10000)%10
six = (number//100000)%10
seven = (number//1000000)%10
eight = (number//10000000)%10

totalNumber = (one*2**0)+(two*2**1)+(three*2**2)+(four*2**3)+(five*2**4)+(six*2**5)+(seven*2**6)+(eight*2**7)
print(totalNumber)



