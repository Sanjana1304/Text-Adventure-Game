import random
import time
def introduction():
    name=input("Hello hero,whats your name? ")
    print("Okay,", name.title(),"lets start the game !")
    time.sleep(1)
    print("\nYou missed the route to get home.")
    time.sleep(1)
    print("All of a sudden it all turns dark and now...")
    time.sleep(2)
    print("you are in a land full of ALIENS who have",end=" ")
    print("assembled before you to destroy you!")
    time.sleep(2)
    print("\nYou try to escape but you see a")
    time.sleep(2)
    print("1.fireplace behind you ,")
    time.sleep(1)
    print("2.A dragon on your right, asking you to come over there.")
    time.sleep(2) 
def your_option():
    choice=""
    while choice!="dragon" and choice!="fireplace":
          choice=input("\nWhich side do you choose? (dragon/fireplace) : ")
    if choice=="dragon":
              dragon()
    elif choice=="fireplace":
              fireplace()
def fireplace():
    print("Oh my god...")
    time.sleep(1)
    print("You chose the wrong path")
    print("You are burnt !")
    time.sleep(1)
    print("GAME OVER")
def dragon():
    print("\nYou get next to the dragon...")
    time.sleep(1)
    print("The dragon says he will give you a chance")
    print("if you want to escape from these aliens!")
    time.sleep(3)
    print("\n\nDo you beleive the dragon or",end=" ")
    print("you try to kill the dragon?")
    time.sleep(1)
    print("1. I beleive", "2.I\'ll kill" )
    ch=input("Choose 1 or 2 : ")
    if ch=="1":
        secondchance()
    elif ch=="2":
        print("\n\nThe dragon is powerful than you.")
        time.sleep(1)
        print("You are dead")
        time.sleep(1)
        print("GAME OVER")
def secondchance():
    print("\n\nSmart move !")
    time.sleep(1)
    print("The dragon says,\"Hey, hero..")
    print("Now I am going to give you a dice with a number of 1,2,3 hands.")
    time.sleep(2)
    print("\n\n\nYou have to roll the dice and if")
    print("\n1 comes, I will eat you")
    time.sleep(2)
    print("\n2 comes,You have a daunting mission to achieve and thrive")
    time.sleep(2)
    print("\n3 comes, From this location you will flee")
    time.sleep(2)
    dice()
def dice():
    option=input("\n\nWould you like to roll the dice? \(yes/no)")
    if option[0]=="y":
        print("\nCool")
        probabalities()
    else:
        print("\nByee...GAME OVER")
def probabalities():
    n=random.randint(1,3)
    print(" NOW YOU HAVE GOT..",n)
    if n==1:
        print("\n\nOh no,it\'s 1")
        time.sleep(1)
        print("The dragon jumps out in front of you.He opens his jaw...")
        time.sleep(2)
        print("gobbles you in one bite")
        time.sleep(2)
        print("\n\nGAME OVER")
    elif n==2:
        print("\n\nWell, well.You got to go on more adventure")
        time.sleep(2)
        print(" \n\nThe dragon say \"Travel 5 km to the left and you will")
        print("discover it all by yourself !")
        time.sleep(3)
        print("\n\nYou agree to it and walk 5km.")
        time.sleep(2)
        print("\nYou see a cave there that is ")
        print("totally separate from our Earth")
        time.sleep(2)
        print("\n\nNow you are heading to the cave and seeking to locate a way")
        time.sleep(2)
        print("\nOh no!You see a lion there")
        time.sleep(2)
        print("but you do have big stones by you")
        time.sleep(2)
        print("\nAnd what are you going to do now?")
        time.sleep(1)
        print("1. You throw the stone on the lion")
        time.sleep(1)
        print("\n2.You give up")
        tryy=input("\nEnter your choice 1 or 2 ")
        if tryy=="1":
              lion()
        else:
            print(" \nThat\'s okay ! BYE BYE !")
    elif n==3:
        print(" Yayyy! You have finished your adventure")
        print("YOU WON,CONGRATS HERO! ")
def lion():
    print("\nGood throw !")
    time.sleep(2)
    print("but the lion appeared drowsy at first then recovered composure")
    time.sleep(3)
    print("\n\nOH MY GOD,the lion is chasing you now")
    time.sleep(3)
    print("\nThen all of a sudden you see a bucket")
    print("in the center of the field where \"take me\""+ " "+"is written on it")
    time.sleep(2)
    print("\n\nNow what is your choice?")
    time.sleep(1)
    print("1.Take the bucket or")
    print("\n2. go running?")
    last_choice=input("\nChoose 1 or 2 : ")
    if last_choice=="1":
        print("\nOnce you take the bucket...")
        time.sleep(1)
        print("You see a wide vacuum dragging you as you take it and...")
        time.sleep(3)
        print("\n\nSURPRISE! It brought you to your house !")
        time.sleep(1)
        print("YOU SURVIVED!")
        time.sleep(1)
        print("\nCongrats hero")
        time.sleep(2)
    elif last_choice=="2":
        print("\nSry, the lion is faster than you")
        print("\nYou are dead")

        
play="yes"
while play[0]=="y":
    introduction()
    your_option()
    print("\n\nDo you wanna play again? yes/no")
    play=input()
    
