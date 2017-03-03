principal = input('Please enter Principal: ')
if principal >1000:
	rate = .15
elif principal >2000:
	rate = .2
else:
	rate =.3

interest = principal * rate
principal = principal + interest
print principal

interest = principal * rate
principal = principal + interest
print principal



