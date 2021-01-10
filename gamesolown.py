from random import randint
number=randint(0,100)
guess=int(input("Please enter your guess!\n"))
guess_count=1
if guess in (range(number+1,number+11) or range(number-10,number)):
    print("WARM!")
elif guess==number:
    print("You have guess correctly in just a single time.")
else:
     print("COLD!")
while guess!=number:
    guess_new=int(input("Please enter new guess\n"))
    guess_count+=1
    if guess_new in (range(guess+1,number) or range(number+1,guess)):
        print("WARMER!")
    elif guess_new==number:
        print("WOOHO!CORRECT GUESS!YOu took {} guesses to guess correctly".format(guess_count))
    else:
        print("COLDER!")
    x=guess_new
    guess=x
else:
    print("You have guessed correctly in {} guesses.".format(guess_count))
            