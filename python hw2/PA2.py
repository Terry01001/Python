from decks import NUMCARD,faceOf,deckV1,deckV2,printdeckV3,gendeckV4,gendeckV5

from random import shuffle, randrange, sample

A="\ndeckV1 is an already shuffled list."
print(format(A,"_>"+str(2*len(A)-1)))
hand,deckV1 = deckV1[:5],deckV1[5:]
print("Hand:",[*map(faceOf,hand)])
take2 = [z for j in 'ab' if (z:=deckV1.pop(0))<52]
print("Two more cards:",[*map(faceOf,take2)])

# Have you ever considered the determinism of a deck of cards? For example,
# suppose the above code had produced:
#  Hand: ['10♠', 'J♠', 'A♥', '2♦', '3♦']
#  Two more cards: ['Q♠', 'K♠']
#
# Such an output reminds if homework #1, where we might have chosen to
# discard the '2♦' and '3♦', thus taking two more cards to finally get:
#     a.10♠  b. J♠  c. A♥  d. Q♠  e. K♠
#
# This is a royal straight, so you decice to not discard any cards. But what
# you then found out that the card on the top of the undealt deck was 'A♠'?
# Knowing this, you would now say that you should have discarded c, to get
# a royal straight flush.
#
# And you are correct that you should have done that, because the order of a
# shuffled deck of cards is predetermined (and so is the order of our shuffled
# list, deckV1, that was created above).
#
# In contrast to deckV1, each of the following decks cards are not determined
# until they are dealt. 

A="\ndeckV2 is a memory view." # Wait for Lecture 11 before building this one.
print(format(A,"_>"+str(2*len(A)-1)))
print("Hand:",[*map(faceOf,deckV2[:5])])
shuffle(deckV2[5:]) #The undealt cards get a reshuffle (ie, not deterministic)
print("Two more cards:",[*map(faceOf,deckV2[5:7])])

#This uses functional programming, so we'll just call the deck's function:
A="\ndeckV3 is the functional version."
print(format(A,"_>"+str(2*len(A)-1)))
printdeckV3()

#This uses a generator function:
A="\ndeckV4 comes from a generator function."
print(format(A,"_>"+str(2*len(A)-1)))
g4=gendeckV4()
hand = [next(g4) for i in 'a'*5]
print("Hand:",[*map(faceOf,hand)])
take2=[next(g4),next(g4)]
print("Two more cards:",[*map(faceOf,take2)])

#This uses a different generator function:
A="\ndeckV5 comes from a different generator function."
print(format(A,"_>"+str(2*len(A)-1)))
g5=gendeckV5()
hand,take2 = [],[]
for i in range(5):
    hand.append(next(g5))
print("Hand:",[*map(faceOf,hand)])
take2.append(next(g5));take2.append(next(g5))
print("Two more cards:",[*map(faceOf,take2)])
