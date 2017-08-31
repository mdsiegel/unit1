#Matthew Siegel
#8/31/17
#nameAge.py - Getting info based on input

Name = input('Enter your first and last name ' )
FirstName, LastName = Name.split()
Age = int(input('Enter your age '))
print('Your first name has', len(FirstName), 'letters')
print('Your last name has', len(LastName), 'letters')
print('Next year you will be ', Age + 1, 'years old')



