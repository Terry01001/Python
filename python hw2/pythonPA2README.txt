Here is the expected behavior of your homework:
   % python3 PA2.py
   ___________________________________
   deckV1 is an already shuffled list.
   Hand: ['6♠', '2♥', '3♠', 'Q♥', '7♠']
   Two more cards: ['4♠', 'A♥']
   ________________________
   deckV2 is a memory view.
   Hand: ['9♦', '0♥', '3♠', 'K♦', '3♦']
   Two more cards: ['A♣', '2♥']
   _________________________________
   deckV3 is the functional version.
   Hand: ['K♦', '6♠', '3♥', '6♦', '9♦']
   Two more cards: ['Q♠', 'J♣']
   _______________________________________
   deckV4 comes from a generator function.
   Hand: ['2♠', '4♦', 'Q♠', '9♦', '7♠']
   Two more cards: ['3♣', '0♠']
   _________________________________________________
   deckV5 comes from a different generator function.
   Hand: ['3♥', '6♥', '4♥', '6♠', '6♣']
   Two more cards: ['A♥', '3♠']
   %
   % python3 PA2.py 
   ___________________________________
   deckV1 is an already shuffled list.
   Hand: ['A♥', '8♣', '7♦', '8♥', '2♠']
   Two more cards: ['7♥', '5♠']
   ________________________
   deckV2 is a memory view.
   Hand: ['8♣', 'K♦', 'J♠', '4♠', 'Q♥']
   Two more cards: ['2♦', '5♣']
   _________________________________
   deckV3 is the functional version.
   Hand: ['5♠', '0♥', 'A♦', '0♣', '7♣']
   Two more cards: ['8♥', '5♥']
   _______________________________________
   deckV4 comes from a generator function.
   Hand: ['Q♥', '5♦', 'J♣', '3♣', '6♠']
   Two more cards: ['A♥', '0♥']
   _________________________________________________
   deckV5 comes from a different generator function.
   Hand: ['4♥', '4♠', '2♦', 'K♦', '5♥']
   Two more cards: ['2♥', '2♠']
   %

As you see, it creates different cards each time, and the cards in each deck do not repeat.

You will have also seen that the name of the program is PA2.py. Let's look at that:
   % cat PA2.py
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
   %

As you can see, I have given you all of this file; you don't need to change anything or to include this file in your submitted answer. But the first line of the file is the key. In my system, I can use "head" to look at just the first line:
   % head -1 PA2.py
   from decks import NUMCARD,faceOf,deckV1,deckV2,printdeckV3,gendeckV4,gendeckV5
   %

What we see about is that your homework assignment is to implement the decks.py
file. This is the file that you are to submit to the cyberuniversity.

I have already given you a template for it. Read that template file and follow the instructions in it.

To get you started, I remind you that, you should test the 5 different deck-creation codes separately, using interactive mode, before inserting the answers into the template. 

You can also, of course, comment out some of the deck-creation codes, while you work on others (if you also comment out the part of PA2.py that uses them).
