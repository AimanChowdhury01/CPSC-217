#studentInfo
#name = Aiman Nawar Chowdhury
#ID = UCID: 30174339
#Version: 10 Oct, 2022. 

print("%50s" %("Dungeon of Doom"))
print()
print()
#opening
play = str(input("Press S to Start the game or Q to end the game: "))
while play not in("Q","q", "s", "S"):
    play = str(input("Press S to Start the game or Q to end the game: "))
if(play == "Q") or (play =="q"):
    print("Game Lost")
    print("Player quits the game")
elif(play == "S") or (play == "s"):
    #menu
    print("Game started")
    game = 1
    menu = 1
    gold = "1"
    silver = "3"
    while(game == 1):
        room1 = str("""                     Entrance:
                 -----------------""") 
        room2 = str("""                     Pantry:
                -----------------""")
        room3 = str("""                     Kitchen:
                -----------------""")
        room4 = str("""                     Inner room:
                -----------------""")
        print()
        print("Player arrives at entrance, the door to the outside disappeared.")
        print()
        print()
        print(room1)
        print("Options:")
        print()
        print("1)Try to open door to the inside")
        print("2)Enter the left entryway")
        print("3)Enter the right entryway")
        print("4)Quit")
        print()
        entranceOptions = str(input("Enter your option (eg:1,2,3,4): "))
        while entranceOptions not in("1","2","3","4"):
            entranceOptions = str(input("Enter your option (eg:1,2,3,4): "))
        if(entranceOptions == "2"):
            print()
            print(room2)
            #pantry
            #Player enters pantry
            print("""A silver lock can be seenm the position of the lock is currently
positioned in the left, it can be turned to center position, right position,
left position, or you can choose to do nothing and go back to the entrance.""")
            print()
            print("1) Press 1 to turn lock to center position and go back to entrance.")
            print("2) Press 2 to turn lock to right position and go back to entrance.")
            print("3) Press 3 to turn lock to left position and go back to entrance.")
            print("4) Do nothing and go back to entrance.")
            silver = str(input("Type in option(eg: 1-4): "))
            while silver not in ("1", "2", "3", "4"):
                silver = str(input("Type in option(eg: 1-4): "))
            menu = 1
            #pantrydone
            #kitchen   
        elif(entranceOptions == "3"):
            print()
            print(room3)
            #Player entered kitchen
            print()
            print()
            print("""A gold lock can be seen the position of the lock is currently
positioned in the center, it can be turned to center position, right position,
left position, or you can choose to do nothing and go back to the entrance.""")
            print()
            print("1) Press 1 to turn lock to center position and go back to entrance.")
            print("2) Press 2 to turn lock to right position and go back to entrance.")
            print("3) Press 3 to turn lock to left position and go back to entrance.")
            print("4) Do nothing and go back to entrance.")
            gold = str(input("Type in option(eg: 1-4): "))
            while gold not in ("1", "2", "3", "4"):
                gold = str(input("Type in option(eg: 1-4): "))
            menu = 1
            #kitchendone
            #innerdoor
        elif(entranceOptions == "1"):
            print()
            print(room4)
            if((gold == "3") and (silver == "2")):
                game = 2
            else:
                print("%33s" %"DOOR IS LOCKED")
                game = 1
            #innerdoordone
        elif(entranceOptions == "4"):
            play = "Q"
            print("Player quits the game")
    if(game == 2):
        print("Player enters inner house")
        print("Congratulations you've won the game.")
    
    
    


   
    
    
