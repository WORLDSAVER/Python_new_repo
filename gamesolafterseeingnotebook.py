from random import randint
x=randint(1,100)
guess_list=[]
print("In this game the computer will generate a random number from 1 to 100, you'll have to guess the number, if you are within 10 of the random number in the first guess then Warm will be ouput, else Cold and in the subsequent attempts if your guess is closer than the previous guess then Warmer will be printed else colder, you'll have to guess the number and then the game will stop") 
while True:
    guess=int(input("Please enter your guess.\n"))
    guess_list.append(guess)
    if len(guess_list)==1:
        if guess==x:
            print("Woohoo! You've guessed correctly on {} attempt".format(len(guess_list)))
            break
        elif abs(guess-x)<=10 and guess in range(0,101):
            print("Warm")
        elif guess in range(0,101):
            print("Cold")
        else:
            print("Out of bounds!")
    else:
        if abs(guess-x)<abs(guess_list[-2]-x) and guess in range(0,101) and guess!=x:
            print("Warmer")
        elif abs(guess-x)>abs(guess_list[-2]-x) and guess in range(0,101) and guess!=x:
            print("Colder")
        elif guess==x:
            print("You have guessed correctly in {} attempts".format(len(guess_list)))
            break
        else:
            print("Out of bounds!")
    

    # we can copy the code from above to take an input
    pass