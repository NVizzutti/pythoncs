import random
#Generating Car Company
def getWord():
	possible=['Audi','Chevy','Ford','Lexus','BMW','Chrysler','Ferrari','Bentley','Acura','Jeep','Cadillac','Bugatti','Lotus','GMC','Rolls-Royce', 'Buick', 'Toyota','Honda','Dodge','Infinite']
	number=random.randint(0,len(possible))
	word=possible[number]
	return word
#Check Guesses
def checkLetter(word,guess,secretString):
	i=0
	while i<len(word):
		if word[i]==guess:
			secretString=secretString[0:i]+guess+secretString[i+1:len(word)]
		i=i+1
	return secretString

#Main
print 'The game is HANGMAN. You will have ten attempts to correctly guess the word.'
secretString=""
word=getWord()
j=1
i=0
while i<len(word):
	secretString=secretString+'*'
	i=i+1
print 'Your secret word is:' 
print secretString
while j<11:
	guess=raw_input('Guess a Letter: ')
	secretString=checkLetter(word,guess,secretString)
	print 'Your PROGRESS: '
	print secretString
	print 'Your ATTEMPTS: '
	print j
	if secretString==word:
		print 'GAME OVER, YOU WIN!'
		break
	if j==10:
		print 'SORRY YOURE DEAD!'
	j=j+1
	
	
