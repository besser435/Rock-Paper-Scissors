import random

playerInput = input('Enter rock, paper, or scissors: ')

pcompPlay = ['rock', 'paper', 'scissors']
compChoice = random.choice(pcompPlay) 


print('I choose '+ compChoice)

#outcome logic
if playerInput == 'rock' and compChoice == 'rock': print("It's a draw!")

if playerInput == 'rock' and compChoice == 'paper': print('I win!')
 
if playerInput == 'rock' and compChoice == 'scissors': print('I loose :(')

if playerInput == 'paper' and compChoice == 'rock': print('I loose :(')

if playerInput == 'paper' and compChoice == 'paper': print("It's a draw!")

if playerInput == 'paper' and compChoice == 'scissors':
    print('I win!')
if playerInput == 'scissors' and compChoice == 'rock':
    print('I win!')
if playerInput == 'scissors' and compChoice == 'paper':
    print('I loose :(')
if playerInput == 'scissors' and compChoice == 'scissors':
    print("It's a draw!")

input('press any key to close') #makes it so the program doesnt close instantly once its done being run