# importing the time module
import time
# welcoming the user
name = raw_input("what is your name?")
print('hello',+name,"time to play hangman!")
print("")
# wait for 1 second
time.sleep(1)
print()
"start guessing...."
time.sleep(0.5)
# here we set the secret
word = 'secret'
# creates an variable with an empty value
guesses = ''
# determine the number of turns
turns = 10
# create a while loop
# check if the turns are more than 0
while turns>0:
    # make a counter that starts with zero
    failed = 0
    # for every character in secret_world
    for char in word:
        # see if the letter is in player guess
        if char in guesses:
            # print character
            print(char),

        else:
            # if not found,print a dash
            print('_')
            # and increased the failed counter with one
            failed+=1
            # if failed equals to zero
    # print you won
    if failed == 0:
        print('you won')
# exit the script
break