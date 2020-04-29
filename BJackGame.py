import random

cards = {'Hearts':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11},
         'Diamonds':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11},
         'Spades':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11},
         'Clubs':
         {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}}

playing = True

class Deck():
    def __init__(self,deck = 0):
        self.deck = []
        for outer_key in cards:
            'Outer Key = ',outer_key
            for inner_key,inner_value in cards[outer_key].items():
                self.deck.append(('{} of {}'.format(inner_key,outer_key)))

    def __str__(self):
        x = ''
        for card in self.deck:
            x += '\n' + card
        return 'The deck has: ' + x

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()



class Hand():

    def __init__(self,hand=[],values=0,aces=0):
        self.hand = hand
        self.values = 0
        self.aces = 0

    def add_card(self,x_card):
        self.hand.append(x_card)
        for outer_key in cards:
            for inner_key,inner_value in cards[outer_key].items():
                if f'{inner_key} of {outer_key}' == x_card:
                    self.values += inner_value
                if x_card == 'Aces':
                    self.aces +=1

    def adjust_aces(self):
        if self.hand > 21 and 'Aces':
            self.values -= 10
            self.aces -=1

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0


    def win_bet(self):
        self.total += self.bet


    def loose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            bet = input("How many chips would you lke to bet?: ")
        except ValueError:
            print('Please, you need to enter an amount in number!')
        else:
            if chips.bet > chips.total:
                print ("Sorry, provide an amount greater than the amount in your purse!")
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal)
    hand.adjust_aces


def hit_or_stand(deck,hand):
    global playing

    while True:
        play_hit_stand = input('Do you want to hit or stand, enter h for hit and s for stand! ')

        if play_hit_stand[0].lower() == 'h':
            hit(deck,hand)
        elif play_hit_stand[0].lower() == 's':
            print('The player is standing, dealer, it is your turn')
            playng = False
        else:
            print('Please try again')
            continue
        break


def show_some(player,dealer):

    print("\nDealer Hand: ")
    print('<Dealer second card hidden>')
    print(f'{dealer.hand[1]}')
    print("\nPlayer's Hand:", *player.hand, sep='\n ')

def show_all(player,dealer):
    print(f'\nDealer Hand:{dealer.hand}')
    print(f'Dealer Value: {dealer.values}')
    print(f'\nPlayer Hand:{player.hand}')
    print(f'Player Value:{player.values}')

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")



while True:

    print('Welcome to Blackjack game')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)


    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.values > 21:
            player_busts(player_hand,dealer_hand,player_chips)
        break

    if player_hand.values <= 21:
        while dealer_hand.values < 17:
            hit(deck,dealer_hand)

            # Show all cards
        show_all(player_hand,dealer_hand)

            # Run different winning scenarios
        if dealer_hand.values > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.values > player_hand.values:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.values < player_hand.values:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

        # Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)

        # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

























# test_deck = Deck()
# test_deck.shuffle()
# #print(test_deck)
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# print(test_player.values)
