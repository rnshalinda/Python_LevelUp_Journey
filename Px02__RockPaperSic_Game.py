import random

rock = '''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a                                         
'''

paper = '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                          
'''

sciscors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''

def compGame(u,pc):
    print(f"\nUser : {u}")
    print(f"\nComputer : {pc}")

    if (u == rock and pc == paper) or (u == paper and pc == sciscors):
        print("You lose!\nPC Win!")
    elif (u == paper and pc == rock) or (u == sciscors and pc == paper):
        print("You Win!\nPC lost!")
    else:
        print("DRAW")



game = [rock,paper,sciscors]

user = (input("Enter R, P or S ->> ")).upper()
z = random.choice(game)

if user == 'R':
    user = rock
    compGame(user,z)

elif user == 'P':
    user = paper
    compGame(user,z)

elif user == 'S':
    user = sciscors
    compGame(user,z)

