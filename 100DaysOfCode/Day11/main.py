import random
import art
card_set = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Function for continuing the game
def game():
        game_on=True
        flag=input("Do you want to continue playing? Press 'y' or 'n': ")
        if flag=='n':
            game_on=False
            print("Thanks for playing with us")
        return game_on

def set_cards():
    #Define no. of decks of card to start with
    decks=(input("How many deck of cards you want? (By default it is 2 decks) "))
    if(decks==""):
        decks=2

    cards=card_set*int(decks)*4
    random.shuffle(cards)
    return cards

#gives out a random card
def random_card():
    random.shuffle(cards)
    return cards.pop()

#gives one card to player or house
def give_card(to):
    to.append(random_card())
    return

#printing cards to screen
def print_cards(who,playerFlag=2,move=2):
        if playerFlag==1 and move==1:
            print(f"House cards: [{who[0]}"+", *]")
        elif playerFlag==1:
            print(f"House cards: {who}. Sum={sum(who)}")
        else:
            print(f"Your cards {who}. Sum={sum(who)}")

#at start both will get 2 cards each
def gameStart():
    give_card(cards_house)
    give_card(cards_player)
    give_card(cards_house)
    give_card(cards_player)

#check bust condition with sum printing
def check_bust(who,player):
    flag=True
    if sum(who)>21 and (11 in who):
        cards.remove(11)
        cards.append(1)
        flag= False
    elif sum(who)>21:
        flag= True
        if(player=="House"):
            print_cards(cards_house,1)
            print("BUST! Player won")
        else:
            print("BUST! House won")
    else:
        flag= False
    
    return flag

def check_blackJack():
    if sum(cards_player)==21:
        print("Black Jack !!! You won!")
        return True
    return False

def compare():
        if (sum(cards_player)==sum(cards_house)==21):
            print_cards(cards_house,1)
            print_cards(cards_player)
            print("Sorry! House Won")
        elif(sum(cards_player)==sum(cards_house)):
            print_cards(cards_house,1)
            print_cards(cards_player)
            print("Pass! No one won")
        elif(sum(cards_player)>sum(cards_house)):
            print_cards(cards_house,1)
            print_cards(cards_player)
            print("Player Won")
        else:
            print_cards(cards_house,1)
            print_cards(cards_player)
            print("House Won")


game_on=True
while(game_on):

    #start new game
    print(art.logo)
    cards=set_cards()
    cards_player=[]
    cards_house=[]
    gameStart()


    
    print_cards(cards_house,1,1)
    print_cards(cards_player)
    check_bust(cards_player,"Player")
    if check_blackJack():
        game_on=game()
    else:
        
        hors=1
        while(hors==1):
            hors=int(input("1:Hit or 2:Stand? "))

            if(hors==1):
                give_card(cards_player)
                print_cards(cards_house,1,1)
                print_cards(cards_player)
                if (check_bust(cards_player,"Player")):
                    game_on=game()
                    break
            else:
                hors=2
                
        else:
            print_cards(cards_house,1)
            print_cards(cards_player)
            if (check_bust(cards_house,"House")):
                game_on=game()
            else:
                while(sum(cards_house)<16):
                    give_card(cards_house)
                    if (check_bust(cards_house,"House")):
                        game_on=game()
                        break
                else:
                    compare()
                    game_on=game()
            
            
    
        



    #end of game question
    #print("\n"*100)
    
    

