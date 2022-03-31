import random

hangman_pics = ['''
      +---+
          |
          |
          |
         === ''', '''
      +---+
      O   |
          |
          |
         === ''', '''
      +---+
      O   |
      |   |
          |
         === ''', '''
      +---+
      O   |
     /|   |
          |
         === ''', '''
      +---+
      O   |
     /|\  |
          |
         === ''', '''
      +---+
      O   |
     /|\  |
     /    |
         === ''', '''
      +---+
      O   |
     /|\  |
     / \  |
         === ''']

words = "ant babbon badger bat bear beaver camel cat calm cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()

def getRandomWord (wordlist):
      wordIndex = random.randint (0, len(wordlist) -1)
      return wordlist[wordIndex]

def displayBoard (missedletters, correctletters, secretword):
   print(hangman_pics[len(missedletters)])
   print()
   
   print("Missed Letters:", end=" ")
   for letter in missedletters:
      print(letter, end=" ")
   print()

   blanks = "_" *len(secretword)
   for i in range (len(secretword)): 
      if secretword[i] in correctletters:
         blanks = blanks[:i] + secretword[i] + blanks [i+1:]

   for letter in blanks:
      print(letter, end=" ")
      print()

def getguess (alreadyguessed):
   while True:
      print("Guess a letter.")
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
         print ("Please enter a single letter")
      elif guess in alreadyguessed:
         print("You have already guessed that letter.")
      elif guess not in "abcdefghijklmnopqrstuvwxyz":
         print("Please enter a LETTER")
      else:
         return guess

def playagain():
   print ("Do you want to play again? (Y/N)")
   return input().lower().startswith("y")

print ("H A N G M A N")
missedletters = ""
correctletters = ""
secretword = getRandomWord(words)
gameisdone = False

while True:
   displayBoard(missedletters, correctletters, secretword)

   guess = getguess(missedletters + correctletters)

   if guess in secretword:
      correctletters = correctletters + guess

      foundallletters = True
      for i in range(len(secretword)):
         if secretword[i] not in correctletters:
            foundallletters = False
            break
      if foundallletters:
         print("Yes! The secret word is '" + secretword + '" !You have Won!')
         gameisdone = True
   else:
      missedletters = missedletters + guess

      if len(missedletters) == len(hangman_pics) - 1:
         displayBoard(missedletters, correctletters, secretword)
         print("You have run out of guesses! \nAfter" + str(len(missedletters)) + "missed guesses and " + str(len(correctletters)) + "correct guesses, the word was '" + secretword + "'")
         gameisdone = True

      if gameisdone:
         if playagain():
            missedletters = ""
            correctletters = ""
            gameisdone = False 
            secretword = getRandomWord(words)

         else:
            break 




#https://inventwithpython.com/invent4thed/chapter8.html
