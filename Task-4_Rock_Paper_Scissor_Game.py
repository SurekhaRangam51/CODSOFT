#Rock-Paper-Scissors Game
import random
play=True
while play:
    computer_choice=random.randint(0,2)
    user_choice=int(input("enter the number \n 0-rock \n 1-paper \n 2-scissor \n :" ))
    print(f"User_choice ={user_choice}")
    print(f"Computer_choice ={computer_choice}")
    if(user_choice<0 or user_choice>2):
        print("choose correct  number")
        
    else:
        if(computer_choice==user_choice):
            print("The game is draw")
            
        elif(user_choice==0 and computer_choice==2):
            print("good,you won game")
            
        elif( user_choice==2 and computer_choice==0):
            print("sorry,you lose the game")
            
        elif(computer_choice>user_choice):
            print("sorry,you lose the game")
        
        elif(computer_choice<user_choice ):
            print("good,you won game")
            
    a=input("Do you want play another round(yes/no)\n:")
    if a=="no":
        break

