print 'Welcome to Mastermind. The object of the game is to guess a set of four predetermined colors in their correct order. After each guess you will be told how many exact matches(correct color, correct position) and how many partial matches (correct color, incorrect position) you have guessed. The object of the game is to correctly give the code in the least amount of guesses. Keep in mind spelling is important. Have fun!'

import random
secretCode=[]
user=[]
exacts=0
partials=0
i=0
while i<4:
  color=random.randint(0,6)
  if color==0:
    color='blue'
  if color==1:
    color='green'
  if color==2:
    color='red'
  if color==3:
    color='orange'
  if color==4:
    color='yellow'
  if color==5:
    color='pink'
  if color==6:
    color='purple'
  secretCode.append(color)
  i=i+1

print secretCode


while secretCode!=user:
    user=[]
    user1=raw_input('Guess the first color: ')
    user2=raw_input('Guess the second color: ')
    user3=raw_input('Guess the third color: ')
    user4=raw_input('Guess the fourth color: ')
    user.append(user1)
    user.append(user2)
    user.append(user3)
    user.append(user4)

    print "The previous guess was: "
    print user
    l=0
    while l<len(user):
        z=0
        while z<len(secretCode):
            if user[l]==secretCode[z]:
                exacts=exacts+1
            z=z+1
            l=l+1
    	print "Exact matches for this guess:"
   	print exacts
	exacts=0 

    k=0
    while k<len(user):
        q=0
        while q<len(secretCode):
            if user[k]==secretCode[q]:
                partials=partials+1
		partials=partials-exacts
            q=q+1
        k=k+1
    print 'Partial matches for this guess:'
    print partials
    partials=0
    if secretCode==user:
            print 'Congratulations, you have guessed the code!'    