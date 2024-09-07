
print('''

https://ascii.co.uk/art
                               88         
  ,d                           88         
  88                           88         
MM88MMM ,adPPYYba, 8b,dPPYba,  88   ,d8   
  88    ""     `Y8 88P'   `"8a 88 ,a8"    
  88    ,adPPPPP88 88       88 8888[      
  88,   88,    ,88 88       88 88`"Yba,   
  "Y888 `"8bbdP"Y8 88       88 88   `Y8a  
''')

print('''
                                                     _..----.._                                   
                                                    ]_.--._____[                                  
                                                  ___|'--'__..|--._                               
                              __               """    ;            :                              
                            ()_ """"---...__.'""!":  /    ___       :                             
                               """---...__\]..__] | /    [ 0 ]      :                             
                                          """!--./ /      """        :                            
                                   __  ...._____;""'.__________..--..:_                           
                                  /  !"''''''!''''''''''|''''/' ' ' ' \"--..__  __..              
                                 /  /.--.    |          |  .'          \' ' '.""--.{'.            
             _...__            >=7 //.-.:    |          |.'             \ ._.__  ' '""'.          
          .-' /    """"----..../ "">==7-.....:______    |                \| |  "";.;-"> \         
          """";           __.."   .--"/"""""----...."""""----.....H_______\_!....'----""""]       
        _..---|._ __..--""       _!.-=_.            """""""""""""""                   ;"""        
       /   .-";-.'--...___     ." .-""; ';""-""-...^..__...-v.^___,  ,__v.__..--^"--""-v.^v,      
      ;   ;   |'.         """-/ ./;  ;   ;\P.        ;   ;        """"____;  ;.--""""// '""<,     
      ;   ;   | 1            ;  ;  '.: .'  ;<   ___.-'._.'------""""""____'..'.--""";;'  o ';     
      '.   \__:/__           ;  ;--""()_   ;'  /___ .-" ____---""""""" __.._ __._   '>.,  ,/;     
        \   \    /"""<--...__;  '_.-'/; ""; ;.'.'  "-..'    "-.      /"/    `__. '.   "---";      
         '.  'v ; ;     ;;    \  \ .'  \ ; ////    _.-" "-._   ;    : ;   .-'__ '. ;   .^".'      
           '.  '; '.   .'/     '. `-.__.' /;;;   .o__.---.__o. ;    : ;   '"";;""' ;v^" .^        
             '-. '-.___.'<__v.^,v'.  '-.-' ;|:   '    :      ` ;v^v^'.'.    .;'.__/_..-'          
                '-...__.___...---""'-.   '-'.;\     'WW\     .'_____..>."^"-""""""""    fsc       
                                      '--..__ '"._..'  '"-;;"""                                   
                                             """---'""""""                   
''')

print("""
Welcome to Treasure Island. 
Your mission is to find the treasure.
""")

print('''
You are at a cross road. Where do you wanna go?
''')

choice = input("Type 'L'-left or 'R'-right ->> ").upper()

if choice == 'R' or choice != 'L':
    print("Fall into a hole, Game Over..")
elif choice == 'L':
    choice = input("SWIM or WAIT? ->> ").upper()
    if choice =='SWIM' or choice != 'WAIT':
        print("Attacked by trout. Game Over..")
    elif choice == 'WAIT':
        print("Good choice")
        choice = input("Which door? R or B or Y ->> ").upper()
        if choice == 'R':
            print("Too bad, Burn by fire, Game Over")
        elif choice == 'B':
            print("Eaten by beasts. Game Over.")
        elif choice != 'R' and choice != 'B' and choice != 'Y':
            print("Game Over...")
        elif choice == 'Y':
            print("Congrats. You Win!")
