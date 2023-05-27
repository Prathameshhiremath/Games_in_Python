from tic import *
from bull import *
from rock import *

while True:
    print("1)Rock\n2)Tic\n3)Bull")
    ch=int(input("Enter choices"))

    if ch==1:
      obj= againplay()
      obj.user1()
      obj.result1()
      obj.again()

    elif ch==2:
print(time.time())

        obj1=tic_tac_toe()
    elif ch==3:
        game_type = input("Enter 'S' for single player or 'M' for multiplayer: ")
        if game_type.upper() == 'S':
         game = Game()
         game.play()
        elif game_type.upper() == 'M':
         game = MultiplayerGame()
         game.play()
        else:
         print("Invalid input. Please try again.")
    else:
        print("Enter correct choice")    
      
