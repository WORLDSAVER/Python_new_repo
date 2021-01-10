import random
num=random.randint(0,100)
guess_list=[0]
print("Welcome to my game!")
print("I'm thinking of a number between 1 to 100 and you have to guess it")
print("I'll tell you how many guesses you took to predict my thinking.")
print("If on the first guess you are able to guess within 10 my thought of number then I'll say that you are warm!")
print("If not then I'll say you are cold")
print("If your subsequent guess is closer to my thought of number than your previous guess then I'll tell you that you are getting Warmer.")
print("If it's farther away from my thought of number than your previous guess, I'll say that you are getting colder")
print("The game ends when you guess correctly")
while True:
    guess=int(input("I'm thinking of a number between 1 and 100 please tell your guess."))
    if guess not in range(0,101):
        print("Out of Bounds!")
        continue
    if guess==num:
        print(f"Congratulations you've guessed it correctly in {len(guess_list)} guesses.")
        break
    guess_list.append(guess)
    
    if guess_list[-2]:
        if abs(guess-num)<abs(guess_list[-2]-num):
            print("Warmer!")
        else:
            print("Colder!")
    else:
        if abs(guess-num)<=10:
            print("Warm!")
        else:
            print("Cold!")
        