import math

def calcPoints(PPG,PA,FGP):
    PF=PPG+math.pow(PPG-PA,2)+(FGP*2)
    return PF
    
def winStat(X,Y):
    PF = math.pow(X,2.9)
    PA = math.pow(Y,2.9)
    DIV=PF+PA
    win = PF/DIV
    round(win,2)
    winPercentage = win*100
    return round(winPercentage,2)

def winRank(CA,GI,SA,HC,BP,I,TE,TM,SI,HH):
    A=CA*2
    B=GI*1.5
    C=SA
    D=HC*.5
    E=BP*.5
    F=I*.5
    G=TE*.5
    H=TM
    I=SI
    J=HH*1.5
    Win=A+B+C+D+E+F+G+H+I+J
    return Win
    

def getLine(winPercentage):
    S=(winPercentage-50)
    S1=S/2.8
    S1=round(S1,0)
    Spread=S1+(float(.5)*round(S,0))
    Spread=float(-Spread)
    return Spread


#main
#PPG1=input('Team As PPG: ')
#PA1=input('Team As PA:')
#FGP1=input('Team As FG%: ')
#PF1=calcPoints(PPG1,PA1,FGP1)

#Get Stats
#PPG2=input('Team Bs PPG: ')
#PA2=input('Team Bs PA:')
#FGP2=input('Team Bs FG%: ')
#PF2=calcPoints(PPG2,PA2,FGP2)
#calculate Win%
#X=calcPoints(PPG1,PA1,FGP1)
#Y=calcPoints(PPG2,PA2,FGP2)
#WinStat= winStat(X,Y)
#print 'Based on Stats Only:'
#print WinStat

#Get Ratings
#A=input('CA-Rating: ')
#B=input('GI-Rating: ')
#C=input('SA-Rating: ')
#D=input('HC-Rating: ')
#E=input('BP-Rating: ')
#F=input('I-Rating: ')
#G=input('TE-Rating: ')
#H=input('TM-Rating: ')
#I=input('SI-Rating: ')
#J=input('HH-Rating: ')
#Calculate Win%
#WinRank=winRank(A,B,C,D,E,F,G,H,I,J)
#print 'Based on Ratings Only:'
#print WinRank

#Final Spread
#Sum=WinStat+WinRank
#WinAvg=Sum/2
#Line=getLine(WinAvg)
#print 'Final Win Percentage: '
#print WinAvg
#print 'The Point-Spread for Team A is: '
#print Line


