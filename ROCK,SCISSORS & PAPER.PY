import random
choices = ["Rock","Paper","Scissor"]
computer = random.choice(choices)
player =False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock,Paper & Scissor ?").capitalize()
    if player == computer:
        print("Tie!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!",computer,"cover",player)
            cpu_score += 1
        else:
            print("You win!!",player,"Smashes",computer)
            player_score+=1
    elif player=="Paper":
        if computer=="Scissor":
            print("You lose!!",player,"cut the",computer)
            cpu_score+=1
        else:
            print("You win",computer,"covers",player)   
            player_score+=1
    elif player=="Scissor":
        if computer=="Rock":
            print("You lose!!",computer,"Break",player)
            cpu_score+=1
        else:
            print("You win",player,"cover",computer)  
            player_score+=1                
    elif player=="End":
        print(f"Final scores{cpu_score},{player_score}")   
        break     