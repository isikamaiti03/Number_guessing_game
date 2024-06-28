import random
generated_num=random.randint(1,100)
g_count=0
while(True):
     user=input("Guess the number(1-100) Or Quit? :")
     if(user=="Quit"):
         break
     else:
         user=int(user)
         if user>generated_num:
             print("Lower number pls.")
         elif user<generated_num:
             print ("Higher number pls.")
         else:
             print("you guessed it right")
             print("you guessed it in",g_count,"attempt.")
             break
     g_count+=1
print("___GAME OVER___")
