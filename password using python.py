import random

def genratepassword(pwlength):

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  passwords = []

  for i in pwlength:
    password =""
    for j in range(i):
       next_letter = random.randrange(len(alphabet))
       password= password + alphabet[next_letter]

       password =  replacewithnumber(password)
       password =  replacwithuppercaseletter(password)

       passwords.append(password)

    return passwords

def replacewithnumber(pword):
    for i  in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword=pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    return pword

def replacwithuppercaseletter(pword):
   for i in range(random.randrange(1,3)):
      replace_index = random.randrange(len(pword)//2,len(pword))
      pword=pword[0:replace_index] + str(random.randrange(10)).upper() + pword[replace_index+1:]
   return pword  

def main():
   numPassword = int(input("How many passowrd do you want to generated ? "))
   print("Genrating",str(numPassword), "password")

   passwordlength=[]
   print("Minimum password  length should be 3 ")
 
   for i in range(numPassword):
     length = int(input("Enter the length of password" + str(i+1) + " "))
     if length < 3:
      length ==3
      passwordlength.append(length)

   Password = genratepassword(passwordlength)

   for i in range(numPassword):
        print ("Password #"+str(i+1)+" = " + Password[i])
main()        


 
