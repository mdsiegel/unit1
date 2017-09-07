#Matthew Siegel
#9/7/17
#change.py - getting the amount of change

cents = int(input('Enter the amount of cents you have: '))
quarters = cents//25
dimes = (cents-(quarters*25))//10
nickles = (cents-(quarters*25)-(dimes*10)
