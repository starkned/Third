import Texas

str = input()
black_cards = str[6:22]
white_cards = str[28:43]
bool = True

black = Texas.texas_cards(black_cards)
white = Texas.texas_cards(white_cards)

if black.rank > white.rank:
    print("Black Wins")


elif black.rank < white.rank:
    print("White Wins")

else:
    b = sorted(black.size, reverse=True)
    w = sorted(white.size, reverse=True)
    for i in range(0, 5):
        if b[i] > w[i]:
            print("Black Wins")
            bool = False
            break
        if b[i] < w[i]:
            print("White Wins")
            bool = False
            break
    if bool:
        print("Tie")
