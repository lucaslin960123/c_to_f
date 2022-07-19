driving = input('Have you ever drive a car before? ')
if driving != 'yes' and driving != 'no':
	print('You can only answer yes or no')
	raise SystemExit
age = int(input('What is your age? '))
if driving == 'yes':
	if age >= 18:
		print('You pass the test')
	else:
		print('That is kinda weird')
elif driving == 'no':
	if age >= 18:
		print('Then what are you doing right now?')
	else:
		print('Good,You are able to drive a car in future')
