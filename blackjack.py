from random import randrange
import time

# global variables
chips = 0
card_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
hand = []
dealer_hand = []
deck = []


def draw_card(hand_param):
    global deck
    card = deck.pop(randrange(len(deck)))  # returns and removes a random card from the deck
    if card >= 10:
        # Face card
        hand_param.append(10)
    elif card == 1:
        # Card is an ace
        if sum(hand_param) <= 10:
            hand_param.append(11)
        else:
            hand_param.append(1)
    else:
        hand_param.append(card)

    if sum(hand_param) > 21:
        if 11 in hand_param:
            hand_param.remove(11)
            hand_param.append(1)
    return card


def main():
    global chips, card_names, hand, dealer_hand, deck
    answer = input("Hey you wanna play blackjack? (yes/no): ")
    if answer == "yes":
        playing = True
        chips = 20000
    else:
        playing = False

    while playing:
        # Creating deck
        suit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        deck = suit + suit + suit + suit

        hand = []
        dealer_hand = []
        print("You have %d chips" % chips)

        # Checking if the input value for bet is valid
        askingforbet = True
        while askingforbet:
            bet = input('How much would you like to bet? (Enter a number): ')
            if not bet.isnumeric():
                print("The value you entered was not a number")
            elif int(bet) > chips:
                print("You don't have that many chips")
            elif int(bet) < 1:
                print("You need to bet some chips")
            else:
                askingforbet = False

        new_balance = chips - int(bet)
        print("chip balance:", new_balance)

        # Dealing initial cards
        i = 2
        while i > 0:
            first_card = draw_card(hand)
            time.sleep(0.5)
            if 2 <= first_card <= 10:
                print("Dealer dealt you %d, now you have %d" % (first_card, sum(hand)))
            else:
                print("Dealer dealt you %s, now you have %d" % (card_names.get(first_card), sum(hand)))
            draw_card(dealer_hand)
            i -= 1
        time.sleep(0.5)
        # Dealer gets first cards
        if 2 <= dealer_hand[0] <= 10:
            print("Dealer's first card is %d" % (dealer_hand[0]))
        else:
            print("Dealer's first card is %s" % (card_names.get(dealer_hand[0])))

        print("You're at %d" % sum(hand))

        blackjack = False
        if sum(hand) == 21:
            blackjack = True
        # Starting hitting and staying
        while True:
            user_input = input("Hit or Stay? ")
            if user_input.lower() == "hit":
                card = draw_card(hand)
                time.sleep(0.5)
                if 2 <= card <= 10:
                    print("Drew %d, now you have %d" % (card, sum(hand)))
                else:
                    print("Drew %s, now you have %d" % (card_names.get(card), sum(hand)))

                if sum(hand) > 21:
                    time.sleep(0.5)
                    print("You went over, you lose!")
                    chips = new_balance
                    break
            elif user_input.lower() == "stay":
                print("You have %d" % sum(hand))
                print('dealers hand:', sum(dealer_hand))
                while sum(dealer_hand) < 17:
                    print("Dealer had less than 17, so he hits")
                    dealer_card = draw_card(dealer_hand)
                    time.sleep(0.5)
                    if 2 <= dealer_card <= 10:
                        print("Dealer drew %d, now he has %d" % (dealer_card, sum(dealer_hand)))
                    else:
                        print("Dealer drew %s, now he has %d" % (card_names.get(dealer_card), sum(dealer_hand)))
                time.sleep(0.5)
                if sum(dealer_hand) > 21 or sum(dealer_hand) < sum(hand):
                    print('You win!')
                    if blackjack:
                        print("Blackjack!")
                        new_balance = new_balance + (2.5 * int(bet))
                    chips = new_balance
                elif 22 > sum(dealer_hand) > sum(hand) or sum(hand) > 21:
                    print("Dealer is standing at %d" % sum(dealer_hand))
                    time.sleep(0.5)
                    print('You lose!')
                    chips = new_balance
                elif sum(dealer_hand) == sum(hand):
                    print("Dealer is standing at %d" % sum(dealer_hand))
                    time.sleep(0.25)
                    print('Draw!')
                    chips = new_balance
                break
        time.sleep(0.75)
        print("Current Balance: %d" % chips)

        if chips <= 0:
            print("You're out of chips! Get out of my casino!")
            exit()

        answer = input("Wanna play again? (yes/no): ")
        if answer != "yes":
            playing = False
        # end of while loop

    # Answer was no or something other than yes
    print("Okay then. Bye!")


if __name__ == '__main__':
    main()
