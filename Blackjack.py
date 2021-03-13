def restart():
    import random
    global chips
    chips = 100
    print("BLACKJACK")
    print('=' * 35)

    def main():
        dealer_cards = []
        dealer_face=['▢']
        player_cards = []
        player_face=[]
        empty = []
        global wager

        def screen():
            return ("Dealers Cards:" + str(dealer_face)+ "\nYour Cards: " + str(player_face))

        if chips < 10:
            print("Chips: " + str(chips))
            reset = input("You do not have enough chips to play, do you want to restart? ").lower()
            if reset == "yes" or reset == "y":
                print("")
                restart()
            else:
                exit()

        print("Chips: " + str(chips))
        wager = input("How many chips do you want to bet: ")
        if wager.isnumeric():
            if int(wager) < 10:
                print("Minimum bet is 10 chips")
                main()
            elif int(wager) > chips:
                print("You do not have enough chips")
                main()
            else:
                print("")
        else:
            print("Invalid response")
            main()

        def playagain():
            play = input("Do you want to play again? ").lower()
            if play == "y" or play == "yes":
                print("")
                main()
            if play =="n" or play=="no":
                print("Chips: " + str(chips))
                exit()
            else:
                print("Invalid response")
                playagain()

        def win(win):
            global chips
            if win == 1:
                print("\n" + screen() + "\nYou win")
                chips = chips + int(wager)
                playagain()
            if win == -1:
                print("\n" + screen() + "\nDealer wins")
                chips = chips - int(wager)
                playagain()
            if win == 0:
                print("\n" + screen() + "\nPush")
                playagain()

        def player_score():
            for i in player_cards:
                if i== "J" or i == "Q" or i == "K" or i == "A":
                    if i =="A":
                        player_cards[player_cards.index(i)]=11
                    else:
                        player_cards[player_cards.index(i)]=10
            total=sum(player_cards)
            if total==21:
                return win(1)
            elif total > 21:
                if 11 in player_cards:
                    player_cards[player_cards.index(11)] = 1
                    return sum(player_cards)
                else:
                    return win(-1)
            else:
                return sum(player_cards)

        def dealer_score():
            for i in dealer_cards:
                if i == "J" or i == "Q" or i == "K" or i == "A":
                    if i == "A":
                        dealer_cards[dealer_cards.index(i)] = 11
                    else:
                        dealer_cards[dealer_cards.index(i)] = 10
            total=sum(dealer_cards)
            if total > 21:
                if 11 in dealer_cards:
                    dealer_cards[dealer_cards.index(11)]=1
                    return sum(dealer_cards)
                else:
                    return win(1)
            elif total == 21:
                return win(-1)
            elif total < 17:
                draw(dealer_cards, dealer_face)
                redraw=dealer_score()
                return redraw
            else:
                return sum(dealer_cards)

        def compare(player_total, dealer_total):
            if player_total > dealer_total:
                return win(1)
            elif player_total < dealer_total:
                return win(-1)
            else:
                return win(0)

        def draw(list, list2):
            card = random.randint(1, 13)
            if card == 11:
                card = "J"
            elif card == 12:
                card = "Q"
            elif card == 13:
                card = "K"
            elif card == 1:
                card = "A"
            list.append(card)
            list2.append(card)
            return card

        def flip():
            dealer_face[0] = draw(empty, empty)
            dealer_cards.append(dealer_face[0])

        def winner():
            player_total = player_score()
            dealer_total = dealer_score()
            win(compare(player_total, dealer_total))

        def hit_stay2():
            player_score()
            hit = input("Do you want to hit or stand: ").lower()
            if hit == 'hit':
                draw(player_cards,player_face)
                player_score()
                print("")
                print(screen())
                hit_stay2()
            elif hit == "stand":
                flip()
                winner()
            else:
                print("Invalid response")
                hit_stay2()

        def hit_stay():
            global wager
            player_score()
            hit = input("Do you want to hit, stand, or double down: ").lower()
            if hit == 'hit':
                draw(player_cards, player_face)
                player_score()
                print("")
                print(screen())
                hit_stay2()
            elif hit == "stand":
                flip()
                winner()
            elif hit == "double down":
                wager = int(wager) * 2
                draw(player_cards, player_face)
                player_score()
                flip()
                winner()
            else:
                print("Invalid response")
                hit_stay()
        draw(player_cards,player_face)
        draw(player_cards,player_face)
        draw(dealer_cards,dealer_face)
        print(screen())
        hit_stay()

    main()
restart()