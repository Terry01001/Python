from random import sample
class Hand():
    """The cards class has the following:
       - A PRIVATE class attribute "__deck" that holds a list of numbers. This
         attribute must be initialized to hold a randomized list of all of the
         numbers from 0 to 51. It must be initialized using list comprehension.
       - A PRIVATE class attribute "__players" that is initialized to an empty
         list.
       - A classmethod named "new", which: 1) resets the class attribute to a
         new randomized list of 52 numbers, and 2) for each item in __players,
         discard all of that item's cards. 
       - A classmethod named "deal" that returns the value it pops from __deck
         (Recall that __deck is a list, so it has a pop method). If __deck is
         empty, it must not give an error, but instead return the value of 52.
  
    Objects of the Hand class also have the following regular methods defined: 
       __init__, __len__, __str__, __le__, __lt__, __ge__, __gt__, __eq__,
       __ne__, __iter__, __getitem__, __delitem__, sort, display, discard,
       retire.

    They also have a private method __score (which I've written for you).   """

    __deck = [x for x in sample(range(52),52)]#This class attribute holds a list of numbers.
                    #It must be initialized using list comprehension.
                    #It must be initialized as random-ordered #s from 0 to 51.

    __players = []  #This class attribute has a list of all class instances.
                    #It is initially empty. (Teacher did it for you already.)
                    
    @classmethod
    def new(cls):
        """This is a classmethod which: 1) resets the class attribute to a
        new randomized list of 52 numbers, and 2) for each item in __players,
        discard all of that item's cards.                                 """
        cls.__deck= [x for x in sample(range(52),52)]
        for i in cls.__players:
            i.hand=[]
    
    @classmethod
    def deal(cls):
        """This is a classmethod that returns the value it pops from __deck
        (Recall that __deck is a list, so it has a pop method). If __deck is
        empty, it must not give an error, but instead return the value 52."""
        if(len(cls.__deck)==0):
            return 52
        else:
            return cls.__deck.pop()
    
    def __init__(self, num=5): 
        """This creates a new player by:
           1. Adding itSELF to the class attribute "__players".
           2. Creating a normal attribute named "hand". Create it this way:
                - It must be created with a list comprehension.
                - It must get its elements by calling the "deal" class method
                  a total of "num" times.
                - If the card that is return by deal has the value of 52, then
                  do not add that value into "hand".                       """
        Hand.__players.append(self)
        self.hand=[y for x in range(num) if (y:=Hand.deal())!=52 ]

    def __len__(self): 
        """Returns the number of cards in the hand (usually, it is 5).   """
        if self in Hand.__players:
            return len(self.hand)
    
    def __str__(self):
        """This uses the code from the earlier homework to return a string
        describing what the score of this hand is. There are rules that make
        it a little bit more complicated than in the prior homework however:

          1. If the hand does not have exactly five cards, then return:
               "incomplete hand"

          2. If it is just a high card, return "Ace high", "King high", "Queen
               high", "Jack high", "Ten high", "Nine high", etc

          3. If it is one pair, return: "two Aces", "two Kings","two Queens",
               "two Jacks", "two Tens", "two Nines", ... or "two Twos".
        
          4. If it is three of a kind, return: "three Aces", "three Kings",
               "three Queens", ... or "three Twos".
        
          5. If it is two pair, return: "two pair: Aces and Kings", etc
        
          6. If it is full house, return: "full house: Aces and Kings", "full
             house: Sevens and Fours", "full house: Fours and Sevens", etc.
             Note that case the card that had 3 matches must go first (that is
             why the "Sevens and Fours" differs from "Fours and Sevens").

          7. If it is four of a kind, return: "four Aces", "four Kings", "four
             Queens", "four Jacks", "four Tens", "four Nines", etc.

          8. If it is a royal straight flush, return: "royal straight flush".
        
          9. If it is a straight flush, return: "straight flush, King high", or
             "straight flush, Jack high", "straight flush, Nine high", etc.

          10.If it is a flush, return: "flush, King high", "flush Nine high",
             etc.
        
          11. If it is a royal straight, return: "royal straight"

          12.If it is a straight, return: "straight, King high", or "straight
             Jack high", "straight, Nine high", etc.                      """
        if(len(self.hand)<5):
            return "incomplete hand"
        else:
            cards=[]
            for i in self.hand:
                cards+=[[*zip([*range(2,11),*"JQKA"]*13,'♠♣♥♦'*13)][i]]
            faces,suits=[j[0]for j in cards],[j[1]for j in cards]
            for i,v in enumerate(faces):
                if v=='J':  faces[i]=11
                if v=='Q':  faces[i]=12
                if v=='K':  faces[i]=13
                if v=='A':  faces[i]=14
            faces=sorted(faces)
            flush=bool(suits.count(suits[0])==len(suits))
            counts=[]
            for i in faces:
                counts+=[faces.count(i)]
            dic={2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Jack',12:'Queen',13:'King',14:'Ace'}
            
            if(counts.count(2)==2):##3
                return 'two '+dic[faces[counts.index(2)]]+'s'
            elif(counts.count(3)==3):##4
                return 'three' + dic[faces[counts.index(3)]]+'s'
            elif(counts.count(2)==4):##5
                a=[]
                for i,v in enumerate(counts):
                    if v==2:    
                        a.append(faces[i])
                        if a.count(faces[i])==2: del a[len(a)-1]
                return 'two pair: '+dic[a[0]]+'s and ' + dic[a[1]]+'s'
            elif(counts.count(3)==3 and counts.count(2)==2):##6
                return 'full house: '+dic[faces[counts.index(3)]]+'s and '+dic[faces[counts.index(2)]]
            elif(counts.count(4)==4):##7
                return 'four '+dic[faces[counts.index(4)]]+'s'
            elif(faces[0]==10 and flush):
                return 'royal straight flush'
            else:
                if faces[0]==10:
                    if flush:##8
                        return 'royal straight flush'
                    else:##11
                        return 'royal straight'
                elif (faces==list(range(faces[0],faces[0]+len(faces)))) or (faces[0]==2 and faces[1]==3 and faces[2]==4 and faces[3]==5 and faces[4]==14):
                    if flush:##9
                        return 'straight flush, '+dic[faces[4]]+' high'
                    else:##12
                        return 'straight, '+dic[faces[4]]+' high'
                elif flush:##10
                    return 'flush, '+dic[faces[4]]+' high'
                else:##1
                    return dic[faces[4]]+' high'
        
    def __score(self):
        """I am giving you this function. It uses __str__ to score the hand
        as a 3-digit floating point number, according to the rules of poker.
        Technically, there are a few cases where to hand will score the same,
        even though the rules of poker define a tie-breaker. That is not
        important, however, and this function works well enough. """
        S=self.__str__().replace('royal straight','straight Ace high').replace\
                                ('straight Ace high flush','5414').replace\
                                ('straight flush','flush straight')
        if S[0].islower(): S = "one "+S
        code={'Two':'02','Three':'03','Four':'04','Five':'05','Six':'06',
              'Seven':'07','Eight':'08','Nine':'09','Ten':'10','Jack':'11',
              'Queen':'12','King':'13','Ace':'14','incomplete hand':'000',
              'one ':'0','two ':'1','1pair: ':'2','one pair: ':'2',
              'three ':'3','straight':'4','flush':'5','full house: ':'6',
              'four ':'7','s':'',' and ':'.',' high':''}
        for k in code: S=S.replace(k,code[k])
        return float(S.replace(' ','').replace(',',''))

    def __le__(self, otherHand):
        """Returns True if this hand is <= the otherHand.
        (Use __score() to get their values to compare.)   """
        return (self.__score()) <= (otherHand.__score())
    
    def __lt__(self, otherHand):
        """Returns True if this hand is < the otherHand.
        (Use __score() to get their values to compare.)   """
        return (self.__score()) < (otherHand.__score())
    
    def __ge__(self, otherHand):
        """Returns True if this hand is >= the otherHand.
        (Use __score() to get their values to compare.)   """
        return (self.__score()) >= (otherHand.__score())

    def __gt__(self, otherHand):
        """Returns True if this hand is > the otherHand.
        (Use __score() to get their values to compare.)   """
        return (self.__score()) > (otherHand.__score())
    
    def __eq__(self, otherHand):
        """Returns True if this hand is == the otherHand.
        (Use __score() to get their values to compare.)   """
        return (self.__score()) == (otherHand.__score())
    
    def __ne__(self, otherHand):
        """Returns True if this hand is != the otherHand.
        (Use __score() to get their values to compare.)   """
        return (self.__score()) != (otherHand.__score())
        
    def __iter__(self):
       """This allows you to iterate over the cards in the hand, returning on
       each iteration a number between 0 and 51. """
       return iter(self.hand)
       
    def __getitem__(self, pos):
        """This lets you index a card in the hand by its position. If the
        position is out of range or isn't an integer, then raise IndexError."""
        if(pos < len(self.hand) and pos >= 0 and isinstance(pos,int)):
           return self.hand[pos] 
        else:
            raise IndexError
       
    def __delitem__(self, pos):
        """This lets you delete a card from the hand by its position.
        position is out of range or isn't an integer, then raise IndexError."""
        if(pos < len(self.hand) and pos >= 0 and isinstance(pos,int)):
           del self.hand[pos]
        else:
            raise IndexError

    def sort(self):
       """This sorts the hand's cards, in place, based on card values (which
       is to say, based on their numbers from 0 to 51). In the sort, the
       highest card goes on the left (ie, in the zeroeth list-position).    """
       self.hand=sorted(self.hand)

    def display(self):
        """This prints the hand, in this format:
        ┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓
        ┃5♣  ┃   ┃K♠  ┃   ┃10♥ ┃   ┃7♣  ┃   ┃A♠  ┃
        ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃
        ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃
        ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃
        ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   

        Note: the "10" take up 2 characters.
        Note also: there may be any number of cards, but it does not need to
        display properly, if there are more than 9.                        """
        show=[]
        for i in self.hand:
            show+=[[*zip([str(i) for i in (list(range(2,11))+['J','Q','K','A'])*4],[j for j in '♠♣♥♦'*13])][i]]
        for i,v in enumerate(show):
            show[i]=show[i][0]+show[i][1]

        
        print("┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓   ┏━━━━┓")
        print("┃%-4s┃   ┃%-4s┃   ┃%-4s┃   ┃%-4s┃   ┃%-4s┃" % (show[0],show[1],show[2],show[3],show[4]))
        print("┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃")
        print("┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃")
        print("┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃   ┃    ┃")
        print("┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛   ┗━━━━┛")

    def discard(self, pos, replace=True):
        """This removes the card at the indicated position, and then calls
        the deal method to replace the card, if the replace variable is True."""
        del self.hand[pos]
        if(replace==True and (y:=Hand.deal())!=52):
            self.hand.append(y)

    def retire(self):
        """This removes myself from list class attribute holding the list of
        players."""
        Hand.__players.remove(self)

player1,player2,player3=Hand(),Hand(),Hand()
print(player1,":",sep="")    #This is the right way to print this.
player1.display()
print()
print(player2.__str__()+":") #This isn't the "right" way, but it's educational
player2.display()
print()
print(player1<player2)
print()
player2.discard(3)
player2.discard(4)
player2.display()
print()
player2.discard(4,replace=False)
print(len(player2))

player1.retire()
Hand.new()
print(len(player2))
try:
    print(len(player1))
except:
    print("Player 1 retired")
