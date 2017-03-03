atbats = input ('Please enter the players at-bats: ')
hits = input ('Please enter the players humber of hits: ')
walks = input ('Please enter the number of times the player has been walked: ')

battingavg = float (hits)/float (atbats)
onbasepct = float (hits + walks)/float (atbats)
print battingavg
print onbasepct



