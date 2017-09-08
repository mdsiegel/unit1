#Matthew Siegel
#9/7/17
#binary.py - finding binary numbers

number = int(input('Enter an 8 diget binary: '))

one = number%10
two = one%10
three = 
four = (number//1000)%10000
five = (number//10000)%100000
six = (number//100000)%1000000
seven = (number//1000000)%10000000
eight = (number//10000000)%100000000

totalNumber = (one*2**0)+(two*2**1)+(three*2**2)+(four*2**3)+(five*2**4)+(six*2**5)+(seven*2**6)+(eight*2**7)
print(totalNumber)
