def restart():
    import random
    global chips #allows variable 'chips' to be used in entire program
    chips = 100 #sets players initial amount of chips to 100
    print("BLACKJACK")
    print('=' * 35)

    def main():
        #clears users and dealers deck
        #the dealer and player each have 'cards' and 'face', with 'cards' being the value of the their hand, and 'face' being the representation of their hand(ie 'face' has face cards as a number while 'cards' has face cards as their corresponding numeric value)
        dealer_cards = []
        dealer_face=['▢'] #adds square to dealers hand as one of their cards is hidden
        player_cards = []
        player_face=[]
        empty = []
        global times_hit
        times_hit = 0
        global wager

        if chips < 10: #minimum bet is 10 chips, if a player has less than this amount, they have to restart
            print("Chips: " + str(chips))
            reset = input("You do not have enough chips to play, do you want to restart? ").lower()
            if reset == "yes" or reset == "y":
                print("")
                restart()
            else:
                exit()

        print("Chips: " + str(chips))
        wager = input("How many chips do you want to bet: ")
        
        if wager.isnumeric(): #if the players bet is a number
            if int(wager) < 10: #if wager is below 10 chips
                print("Minimum bet is 10 chips")
                main()
            elif int(wager) > chips: #if wager is more than how many chips the player has
                print("You do not have enough chips")
                main()
            else:
                print("")
        else: #if players bet is not a number
            print("Invalid response")
            main()
            
        def screen(): #shows player their cards and the dealers card in the command line
            return ("Dealers Cards:" + str(dealer_face)+ "\nYour Cards: " + str(player_face))

        def playagain(): #whther player wants to play another game
            play = input("Do you want to play again? ").lower()
            if play == "y" or play == "yes": #player does want to play again
                print("")
                main()
            if play =="n" or play=="no": #player doesnt want to play again
                print("Chips: " + str(chips))
                exit()
            else: #player inputs an invlaid response(not 'y','yes','n', or 'no'
                print("Invalid response")
                playagain()

        def win(win): #prints out who the winner is (1 is player, -1 is dealer, and 0 is a tie)
            global chips
            if win == 1: #player wins
                print("\n" + screen() + "\nYou win")
                chips = chips + int(wager)
                playagain()
            if win == -1: #dealer wins
                print("\n" + screen() + "\nDealer wins")
                chips = chips - int(wager)
                playagain()
            if win == 0: #push/tie
                print("\n" + screen() + "\nPush")
                playagain()

        def player_score(): #determines the players current score
            for i in player_cards:
                if i== "J" or i == "Q" or i == "K" or i == "A": #sets value for face cards
                    if i =="A": #if player has an ace
                        player_cards[player_cards.index(i)]=11
                    else: #if player has faces cards aside from ace
                        player_cards[player_cards.index(i)]=10
            total=sum(player_cards)
            
            if total==21: #players hits blackjack
                return win(1)
            elif total > 21:#if player busts
                if 11 in player_cards: #if player has an ace, it value changes from 11 to 1
                    player_cards[player_cards.index(11)] = 1
                    return sum(player_cards)
                else: #player has lost
                    return win(-1)
            else:#if player doesnt bust or hit blackjack, the sum of their cards are returned to be compared to the dealers
                return sum(player_cards)

        def dealer_score():#determines the dealers current score
            for i in dealer_cards:
                if i == "J" or i == "Q" or i == "K" or i == "A": #if the dealer has a face card
                    if i == "A": #if dealer has an ace
                        dealer_cards[dealer_cards.index(i)] = 11
                    else: #if dealer has a face card aside from an ace
                        dealer_cards[dealer_cards.index(i)] = 10
            total=sum(dealer_cards)
            if total > 21: #if dealer busts
                if 11 in dealer_cards: #if ace in deck, its value changes from 11 to 1
                    dealer_cards[dealer_cards.index(11)]=1
                    return sum(dealer_cards)
                else: #dealer busts
                    return win(1)
            elif total == 21: #dealer has blackjack
                return win(-1)
            elif total < 17: #dealer hits until they hit 17
                draw(dealer_cards, dealer_face) #draws another card
                redraw=dealer_score() #dealers new score is assessed, and returned as a win value
                return redraw
            else:
                return sum(dealer_cards) #if dealer doesnt bust or hit blackjack, the sum of their cards are returned to be compared to the players

        def compare(player_total, dealer_total): #determines who wins between dealer and player
            if player_total > dealer_total: #player has a higher socre and wins
                return win(1)
            elif player_total < dealer_total: #dealer has a higher score and wins
                return win(-1)
            else: #dealer and players score is equal
                return win(0)

        def draw(list, list2): #draws a new card at random
            card = random.randint(1, 13) #picks number between 1 and 13, and if the card is a face card it is assigned its corresponding letter
            if card == 11:
                card = "J"
            elif card == 12:
                card = "Q"
            elif card == 13:
                card = "K"
            elif card == 1:
                card = "A"
            list.append(card)#adds card to 'cards'
            list2.append(card)#adds cards to 'face'
            return card

        def flip(): #shows(and draws) dealers hidden first card
            dealer_face[0] = draw(empty, empty)
            dealer_cards.append(dealer_face[0])

        def winner(): #runs functions to determine winner and show who has won
            player_total = player_score()
            dealer_total = dealer_score()
            win(compare(player_total, dealer_total))

        def hit_stay(): #asks player they want to hit or stay
            global wager
            global times_hit
            if times_hit == 0: #gives player the option to double down if this is their first time hitting/staying
                hit = input("Do you want to hit, stand, or double down: ").lower()
            else: #player cannot double down if they have already hit/stayed
                hit = input("Do you want to hit or stand: ").lower()
            times_hit=+1#keeps track of how many times the player has hit/stayed

            if hit == 'hit': #if player wants to hit
                draw(player_cards, player_face)
                player_score()
                print("")
                print(screen())
                hit_stay()
            elif hit == "stand":#if player wants to stand
                flip()
                winner()
            elif hit == "double down": #if player wants to double down
                wager = int(wager) * 2
                draw(player_cards, player_face)
                player_score()
                flip()
                winner()
            else: #if player inputs an invalid command
                print("Invalid response")
                hit_stay()
                
        draw(player_cards,player_face) #2 players cards are drawn, and one dealer card is drawn
        draw(player_cards,player_face)
        draw(dealer_cards,dealer_face)
        print(screen()) #displays cards on command line
        hit_stay() #asks player to hit or stay

    main()
restart()
