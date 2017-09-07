#Matthew Siegel
#9/7/17
#change.py - getting the amount of change

cents = int(input('Enter the amount of cents you have: '))
quarters = cents//25
dimes = (cents-(quarters*25))//10
nickles = (cents-(quarters*25)-(dimes*10))//5
pennies = (cents-(quarters*25)-(dimes*10)-(nickles*5))//1
print('You have',quarters,'quarters',dimes,'dimes',nickles,'nickles',pennies,'pennies')
