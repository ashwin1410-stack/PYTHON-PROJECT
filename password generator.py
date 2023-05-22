import random 
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "[ ] { } ( ) + - . , "

all = lowercase + uppercase + symbol 
length = 16 

password = "" .join(random.sample(all,length))
print("HERE IS YOUR RANDOM PASSWORD : " ,password )