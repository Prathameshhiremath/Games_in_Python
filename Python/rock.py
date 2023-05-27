import random

Cchoice = ["Rock", "Paper", "Scissor"]

class diagram:
    def draw_diagrams(self, ch):
        if (ch == 1) or (ch == "Rock"):
            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
        elif (ch == 2) or (ch == "Paper"):
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
        elif (ch == 3) or (ch == "Scissor"):
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)
        else:
            print("WRONG INPUT! CHOOSE AGAIN PLEASE!\n")

class user(diagram):
    def rules(self):
        print("\tHELLO THERE! WELCOME TO ROCK PAPER SCISSORS GAME!")
        print("INSTRUCTIONS:\nBoth the players have three choices namely rock, paper and scissors.")
        print("\nGAME RULES:")
        print("\tSCISSORS beats PAPER")
        print("\tPAPER beats ROCK")
        print("\tROCK beats SCISSORS")
        print("--------------------------------------------------------------------------")
   
    def user1(self):
        self.a = input("Enter Your Name: ")
        self.youwin = 0
        self.computerwin = 0
        for i in range(1, 6):  # 5 Round game
            try:
                print("Round", i, "Start:")
                print("Please select any one option:")
                print("1.Rock", "2.Paper", "3.Scissor", sep="\n")  # choice any option but in number 1,2,3
                self.uch = int(input("Enter Choices: "))
                self.cch = random.choice(Cchoice)
                print(f"\n{self.a} CHOICE: ")
                super().draw_diagrams(self.uch)
                print("\nCOMPUTER's CHOICE: ")
                super().draw_diagrams(self.cch)
                result.results(self)
            except ValueError:
                print("Sorry you Enter Wrong Input Please choose 1, 2, or 3")
            
   

            
class result(user):
    
    def results(self):
        if (self.uch==1 and self.cch=="Rock") or (self.uch==2 and self.cch=="Paper") or(self.uch==3 and self.cch=="Scissor"):
            self.youwin += 1
            self.computerwin += 1
            print("This Round is Draw:")
        elif (self.uch == 2 and self.cch == "Rock") or (self.uch == 1 and self.cch == "Scissor") or  (self.uch == 3 and self.cch == "Paper"):
            self.youwin += 1
            print(f"{self.a} win this Round")
        else:
            self.computerwin += 1
            print("Computer win this Round")
        
    def result1(self):
        if self.youwin > self.computerwin:
            print(f"{self.a} Win the game:")
            print("Score is:", f"{self.a} score:", self.youwin, "Computer score:", self.computerwin, sep=" ")
        elif self.computerwin > self.youwin:
            print(f"{self.a} Lose the game. Computer win the game:")
            print("Score is:", f"{self.a} score :", self.youwin, "Computer score:", self.computerwin, sep=" ")
        else:
            print("Match Draw")
            print("Score is:", f"{self.a} score:", self.youwin, ",Computer score:", self.computerwin, sep=" ")
class againplay(result):
    def again(self):
        self.user_choice = input("Want to Play again?(Yes/Exit)")
        if self.user_choice == 'yes' or self.user_choice == 'Yes' or self.user_choice == 'YES':
            obj=againplay()
            obj.user1()
            obj.result1()
            obj.again()
           
        else:
            print("Bye")
            

