import math
import people
import random
import game

players = []
ls = []
lm = []
rs = []
ss = []
hr = []
cr = []
ls2 = []
lm2 = []
rs2 = []
ss2 = []
hr2 = []
cr2 = []

def buy(name,N):
  answer = None
  answers = ['ls','lm','rs','ss','hr','cr','ls2','lm2','rs2','ss2','hr2','cr2','lsa','lma','rsa','ssa','hra','cra','m']
  while (answer is None) or (answer in answers):
    answer = input('%s, What do you want to buy? Answer m to open the menu, or press enter if you do not want to buy anything.\n' % name)
    if answer == 'ls' :
      if ls2[N] == 1:
        players[N].buying(200,500)
      else:
        players[N].buying(100,500)
      lsn = ls[N]
      ls[N] = lsn + 1
    if answer == 'lm':
      if lm2[N] == 1:
        players[N].buying(500,1100)
      else:
        players[N].buying(250,1100)
      lmn = lm[N]
      lm[N] = lmn + 1
    if answer == 'rs' :
      if rs2[N] == 1:
        players[N].buying(1300,2400)
      else:
        players[N].buying(650,2400)
      rsn = rs[N]
      rs[N] = rsn + 1
    if answer == 'ss' :
      if ss2[N] == 1:
        players[N].buying(3200,5300)
      else:
        players[N].buying(1600,5300)
      ssn = ss[N]
      ss[N] = ssn + 1
    if answer == 'hr' :
      if hr2[N] == 1:
        players[N].buying(8000,19000)
      else:
        players[N].buying(4000,19000)
      hrn = hr[N]
      hr[N] = hrn + 1
    if answer == 'cr' :
      if lm2[N] == 1:
        players[N].buying(20000,41000)
      else:
        players[N].buying(10000,41000)
      crn = cr[N]
      cr[N] = crn + 1
    if answer == 'ls2':
      players[N].buying(100*ls[N],2000)
      ls2n = ls2[N]
      ls2[N] = ls2n + 1
    if answer == 'lm2':
      players[N].buying(250*lm[N],5000)
      lm2n = lm2[N]
      lm2[N] = lm2n + 1
    if answer == 'rs2':
      players[N].buying(650*rs[N],12500)
      rs2n = rs2[N]
      rs2[N] = rs2n + 1
    if answer == 'ss2':
      players[N].buying(1600*ss[N],32000)
      ss2n = ss2[N]
      ss2[N] = ss2n + 1
    if answer == 'hr2':
      players[N].buying(4000*hr[N],80000)
      hr2n = hr2[N]
      hr2[N] = hr2n + 1
    if answer == 'cr2':
      players[N].buying(10000*cr[N],176000)
      cr2n = cr2[N]
      cr2[N] = cr2n + 1
    if answer == 'lsa':
      players[N].buyall(100,500)
    if answer == 'lma':
      players[N].buyall(250,1100)
    if answer == 'rsa':
      players[N].buyall(650,2400)
    if answer == 'ssa':
      players[N].buyall(1600,5300)
    if answer == 'hra':
      players[N].buyall(4000,19000)
    if answer == 'cra':
      players[N].buyall(10000,41000)
    if answer == 'm' :
      game.helping.menu()
print('Rules:')
print('Recommended to play in full screen. To play in full screen you will need to click the box with an arrow pointing out of it that says open in a new tab if you hover over it.')
print('You can have as many players as you want but it is the most fun with 3-4 players.')
print('The goal of the game is to be the first to reach  $100,000 in revenue.')
print('But you can play to whatever you want, $100,000 usually takes about 15 minutes.')
print('At the end of every turn you get a number between 1 and 20, and that number corresponds to how much percent of your revenue you get.')
print('The worst percentage you can get 30% of your revenue. The best is you can get is 100% of your revenue.\n') 
playerask = input('How many people are playing?\n')
numplayer = int(playerask)

for player in range(numplayer):
  player += 1
  playername = input('Player%s what is your name?\n' % player)
  print('Hi, %s.' % playername)
  players.append(people.Player(playername))

for randoms in range(numplayer):
  ls.append(1)
  lm.append(0)
  rs.append(0)
  ss.append(0)
  hr.append(0)
  cr.append(0)
  ls2.append(0)
  lm2.append(0)
  rs2.append(0)
  ss2.append(0)
  hr2.append(0)
  cr2.append(0)
toot = 5
while toot == 5:
  for N in range(numplayer):
    print ("---------------------------------------------------------------")
    name = players[N].name
    print ('You have $%s\n ' %players[N].money)
    print ('Your revenue is $%s\n ' % players[N].rev)
    buy(name,N)
    per = random.randint(1,20)
    print ('You rolled a %s \n' % per)

    if per >= 8:
      numper = per/2
      totals = numper*10
    if per == 8:
      totals = 45
    if per == 7:
      totals = 40
    if per == 6:
      totals = 40
    if per == 5:
      totals = 40
    if per == 4:
      totals = 35
    if per == 3:
      totals = 35
    if per == 2:
      totals = 35
    if per == 1:
      totals = 30
    moneyper = totals * players[N].rev / 100
    nowest = players[N].money
    players[N].money = moneyper + nowest
    print ('money you earned this turn ')
    print ('$%s\n' % moneyper)
    print ('you have ')
    print ('$%s' % players[N].money)