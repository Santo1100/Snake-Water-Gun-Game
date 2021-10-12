import random
def gamewin(comp,you):
    if comp==you:
        return None
     #check al possibilities when computer choose s   
    elif comp== "s":
      if you=="w":
          return False
    elif you== "g":
        return True
    #check all possilibilities when computer choose w     
    elif comp== "w":
        if you == "g":
            return False
        elif you == "s":
           return True
    #check all possibilities when computer chose g
    elif comp== "g":
      if you=="s":
          return False
    elif you== "w":
        return True    
        

print("computer turn; snake(s water(w) gun(g)?")
randomno = random.randint(1,3)
print(randomno)
if randomno==1:
    comp="s"
elif randomno==2:
    comp="w"
elif randomno==3:
    comp="g"    

you=input("Your  turn: snake(s water(w) gun(g)?")
a = gamewin(comp,you)

print(f"computer chose{comp}")
print(f"you chose {you}")
if a==None:
    print("This game is tie!!!!!!!")
elif a:
    print("you win")
else:
    print("you lose")     


