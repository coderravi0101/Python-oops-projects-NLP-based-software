# -*- coding: utf-8 -*-
"""python NLP Based Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s5m3LGFC2nofJ4dgqjdgs_KNe5ZqRjAI
"""



"""#Python project based on nlp cloud"""

#first of all we would inter a command who install pip
!pip install nlpcloud # yah command dalne se hamera pip install ho jyega.

import nlpcloud
''' Overview about this project:- In this project we make a website or application .through this website first of all
    when i run this code see this type of screen.

    How! would you like to proceed.
    1.Register
    2.Login
    3.Exit.
    note:- yah software gui based nhi hai yah same ek ATM ke website jese hai jha hume click kr kr ke kaam krna hoga.

    Yadi user 1 pr click krta hai to woh Register krega esme usko apna NAME,EMAIL,PASSWORD dalnapadega.
    yadi shi se Register ho gya hai to Login krenge
    Login krne ke baad user ko screen pr 4 cheeje dekhi dengi.

    How! would you like to proceed.
    1.NER (Name entity Recogination)paragraph manengaga aur fer uska output de dega
    2.Language detection (kon sa language hai)
    3.Sentiment (Happy text hai or sad)
    4.Logout(fer se phle wale screen pr chle jyenge.)

 Note:-Login , Register ke liye data base ki need hoti hai pr hum apna sara data disconary
       me rekhenge. '''

class NLPApp:
  def __init__(self):
   self.__database={} # ye bhi privaoute hai.
   self.__first_menu()

  def __first_menu(self): # ye bhi privaoue hai

    first_input = input("""
    Hi! Would you like to proceed?
    1. Not a member? Register
    2. Already member? Login
    3. Galti se aa gaye? Exit
    """)

    if first_input=='1':
      self.__register()
    elif first_input=='2':
      self.__login()
    else:
      exit()


  def __second_menu(self): # ye bhi privaoute hai

    second_input=input("""
    Hi! Would you like to proceed?
    1. NER(name intity rechogination)
    2. Language detection
    3. Sentiment Analysis
    4. Logout
    """)

    if second_input=='1':
      self.__ner()
    elif second_input=='2':
      self.__language_detection()
    elif second_input=='3':
      self.sentiment_analysis()
    else:
      exit()




  def __register(self):
    # esme hum register krne ka code likhne wale hai
    name=input('Enter name')
    email=input('Enter  email')
    password=input('Enter password')

    if email in self.__database:
      print('Email already exists')

    else:
      self.__database[email] = [name,password]
      print('registation successfully. Now login')
      print(self.__database)
      self.__first_menu()
  def __login(self):
    email=input('Enter email')
    password=input('Enter password')

    if email in self.__database:
    #  pass
      if self.__database[email][1]==password:#cheak kr rhe data base ka second item password hai ki nhi
       print('Login Successfully')
       self.__second_menu()
      else:
        print('wrong password. Try again')
        self.__login()

    else:
      print('This email is not Registerd')
      self.__first_menu()

  def __sentiment_analysis(self):
    para = input('enter the paragraph')

    client = nlpcloud.Client("distilbert-base-uncased-emotion", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=False, lang="en")
    response = client.sentiment(para)
# now the the second logi n process value
  #THis place we use sir ka nlp ka api key
    L = []
    for i in response['scored_labels']:
      L.append(i['score'])

    index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]

    print(response['scored_labels'][index]['label'])
    self.__second_menu()

obj=NLPApp()
#obj.__register()

d = {'scored_labels': [{'label': 'sadness', 'score': 0.98093181848526}, {'label': 'joy', 'score': 0.001407247269526124}, {'label': 'love', 'score': 0.0004157320945523679}, {'label': 'anger', 'score': 0.01649504341185093}, {'label': 'fear', 'score': 0.00039679379551671445}, {'label': 'surprise', 'score': 0.00035347335506230593}]}

L = []
for i in d['scored_labels']:
  L.append(i['score'])
#enumerate  function ka use whoha kiya jata hai jb uski value ke saath index bhi print karana ho
index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]



d['scored_labels'][index]['label']

import emoji
print(emoji.emojize('Python is :grinning_face:'))

!pip install emoji