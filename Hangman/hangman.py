import random
import ascii
words=[] #list of words for the game
f = open("words.txt", "r") 
for x in f:
    x= x.rstrip("\n") # to remove the \n from all the words 
    #We will only take words which is atleast 6 char long for this game
    if len(x)>6:  
        words.append(x)

# for each game we will have one word which player have to guess
word_choice=random.choice(words)

# to display the word with letters which player have guessed
display=["_" for _ in word_choice] #It will create blanks for each letter in the word
comments=["Maar dala","Gaya yeh toh","Hints le le but isko bacha le","Tujhse na ho payega","Bhai sahi se khel mar jayega woh","Oops galat ho raha h","Your man is in danger"]

'''keeping a track of all the letters player already entered so that if he does 
enter same word agian, it will give him the warning without affecting his life'''
player_letters=[]
player_life=6
print(ascii.logo, end="\n\n")

print("\nWord: ",display)

#Taking player's guess word
while ("_" in display)==True:
    print("\n")
    player_guess=input("Please enter your guesss \n").lower()
    if player_guess in player_letters:
        print(f"Opps you already entered {player_guess}! Please focus")
    elif(len(player_guess)>=2):
        print(f'{player_guess} is not a letter! Are you high?')
    elif ord(player_guess) not in range(97,123):
        print(f"Dude {player_guess} is not a letter")
    elif(player_guess in word_choice):
        print("Lucky guess")
        player_letters.append(player_guess)
        for i in range(len(word_choice)):
            if word_choice[i]==player_guess:
                display[i]=player_guess
    else:
        player_letters.append(player_guess)
        print(f"No! {player_guess} is not in the word")
        print(ascii.stages[player_life])
        print(comments[player_life])
        player_life-=1
        if(player_life==0):
            break
    print("\nWord: ",display)   
            
if "_" in display:
    print("You hanged the man! you murdered an innocent man!")
else:
    print("Cool! You saved the man from being hanged")



