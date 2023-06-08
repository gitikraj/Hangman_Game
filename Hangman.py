import random as r
word_list = ["aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

a=r.randint(0,2)
choosen_word = word_list[a]
print(choosen_word)
choosen_word_list=[]
for i in choosen_word:
  choosen_word_list.append(i)
# print(choosen_word_list)
a=[]
for i in range(0,len(choosen_word_list)):
  a.append("_")
print(''.join(a))

end_of_game=False
lives=6
d=0
while not end_of_game:
  
  b=(input("Entre your guessed letter \n")).lower()
  # print(b)
  
  
  for j in range(0,len(choosen_word_list)):
    letter=choosen_word_list[j]
    if letter==b:
      a[j]=b
    else:
      d+=1
  # print(d)
  if d==len(choosen_word_list):
    lives=lives-1
    print(stages[lives])
  else:
    print(stages[lives])
  print(''.join(a))
  if "_" not in a:
    end_of_game=True
    print("You won the game!!!")
  elif lives==0:
    print("You lost")
    end_of_game=True
  d=0
