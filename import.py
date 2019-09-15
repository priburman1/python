ans=50
guess=int(input('guess the answer:'))
while guess != ans:
	if guess > ans:
		print('your guess is greater than the answer')
		guess=int(input('guess the answer:'))
	elif guess < ans:
		print ('your guess is less than the answer')
		guess=int(input('guess the answer:'))
		print(ans)
	 
	