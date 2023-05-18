name = input("Ente your Name : ")
print("Welcome to this adventure", name , "!") 
   
answer = input("You are on dead End. You have to take left or right to save ypurself. Which would you take left/Right..? ").lower()

if answer == "left":
    answer = input("You came to river, you can walk around or swim to save yourself ???")
   
    if answer == "swim":
        print("You swim across and died ! RIP ")
    elif answer == "walk":
        print("You walk till your death!! ")    
    else:
     print("Not a valid option")    

elif answer == "right":
     answer = input("You came to bridge and you can go back or across there is only 2 option ")  
     if answer == "back":
         print("you are going to dead now bye !!!")

     elif answer == "across":
            print("you have won this adventure and he gave yo gold")
            
else:
    print("invalid option1")                 