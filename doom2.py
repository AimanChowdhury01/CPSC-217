#studentInfo
#name = Aiman Nawar Chowdhury
#Version: 12 nov, 2022. 
#Final Version : 17 October 2023.

###game win menu####
def gamewon():
    print()
    print()
    print("A Vine growing, Players hops on it and reaches paradise.")
    print("Congrats, Game won")
####different menus###
def livingMenu1():
    print("Player options:")
    print("1)Peak into the pot of soil")
    print("2)Pick the ball of string")
    print("3)Go up the stairs")
    print("4)Go into the dark entranceway")
    print("5)Quit Game")
def livingMenu2():
    print("Player options:")
    print("1)Peak into the pot of soil")
    print("3)Go up the stairs")
    print("4)Go into the dark entranceway")
    print("5)Quit Game")    
def atticMenu1():
    print("Player options: ")
    print()
    print("1) Try to drop cheese through hole in the floor")
    print("2) Pick up Cheese")
    print("3) Take stairway that leads back to the living room")
def atticMenu2():
    print("Player options: ")
    print()
    print("1) Try to drop cheese through hole in the floor")
    print("2) Pick up Cheese")
    print("3) Take stairway that leads back to the living room")
    print("4) Try to drop string through the hole")
def bedroomMenu1():
    print("Player options: ")
    print()
    print("Tom cat is staring at the Mouse hole and unwilling to interact")
    print("1) Go back to living room")

def bedroomMenu2():
    print("Player options: ")
    print()
    print("Tom Cat is staring at the Mouse hole")
    print("Player options: ")
    print("1) Use string to try to distract the Cat")
    print("2) Go back to living room")
def bedroomMenu3():
    print("Tom cat left the room due to noise from the string dropped")
    print("Mouse is sitting idly in the room")
    print("Player options: ")
    print("1) Go back to living room")

def bedroomMenu4():
    print("Tom cat left the room due to noise from the string dropped")
    print("Mouse is sitting idly in the room")
    print("Player options: ")
    print("1) Offer the Mouse cheese")
    print("2) Go back to living room")
######attic code####
def attic(string,cheese):
    if(string == "1"):
        attic = "0"
        while(attic == "0"):
            atticMenu2()
            Aoptions = input("Enter your option(eg:1,2,3,4): ")
            while Aoptions not in("1","2","3","4"):
                Aoptions = input("Enter your option(eg:1,2,3,4): ")
            if(Aoptions == "1"):
                if(cheese == "0"):
                    print("PLAYER DOES NOT HAVE CHEESE RIGHT NOW")
                if(cheese == 1):
                    print("CHEESE IS TOO BIG TO DROP THROUGH THIS TINY HOLE")
                    cheese = "0"
                    string = "1"
                    return(cheese,string)
            if(Aoptions == "2"):
                print("Cheese picked")
                cheese = "1"
                string = "1"
                return(cheese,string)
            if(Aoptions == "3"):
                string = "1"
                if(cheese == "0"):
                    cheese = "0"
                    return(string,cheese)
                if(cheese == "1"):
                    cheese = "1"
                    return(string,cheese)
                    attic = "3"
            if(Aoptions == "4"):
                print()
                string = "2"
                print("String dropped")
                if(cheese == "0"):
                    cheese = "0"
                    return(string,cheese)
                if(cheese == "1"):
                    cheese = "1"
                    return(string,cheese)
                    attic = "3"
                
        ######
    if(string == "0"):
        attic = "0"
        while(attic == "0"):
            atticMenu1()
            Aoptions = input("Enter your option(eg:1,2,3,4): ")
            while Aoptions not in("1","2","3","4"):
                Aoptions = input("Enter your option(eg:1,2,3,4): ")
            if(Aoptions == "1"):
                if(cheese == "0"):
                    print("PLAYER DOES NOT HAVE CHEESE RIGHT NOW")
                if(cheese == "1"):
                    print("CHEESE IS TOO BIG TO DROP THROUGH THIS TINY HOLE")
                    cheese = "0"
                    if(string == "0"):
                        string = "0"
                        return(string,cheese)
            if(Aoptions == "2"):
                print("Cheese picked")
                cheese = "1"
                if(string == "0"):
                    string = "0"
                    return(string,cheese)
            if(Aoptions == "3"):
                string = "0"
                if(cheese == "0"):
                    cheese = "0"
                    return(string,cheese)
                if(cheese == "1"):
                    cheese = "1"
                    return(string,cheese)
                
#####bedrooom code###
def bedroom(string, cheese):
    bdroom = "0"
    while(bdroom == "0"):
        print()
        print("Player arrives at the bedroom")
        print()
        if(string == "0"):
            bedroomMenu1()
            Boptions = input("Enter your option(eg:1,2,3): ")
            while Boptions not in("1"):
                Boptions = input("Enter your option(eg:1,2,3): ")
            if(Boptions == "1"):
                bdroom = "3"
        if(string == "1"):
            bdroom = "2"
            while(bdroom == "2"):
                bedroomMenu2()
                Boptions = input("Enter your option(eg:1,2,3): ")
                while Boptions not in("1", "2"):
                    Boptions = input("Enter your option(eg:1,2,3): ")
                if(Boptions == "1"):
                    print("Cat is not distracted")
                    bdroom = "2"
                if(Boptions == "2"):
                    bdroom = "3"
        if(string == "2"):
            if(cheese == "0"):
                bedroomMenu3()
                Boptions = input("Enter your option(eg:1,2,3): ")
                while Boptions not in("1"):
                    Boptions = input("Enter your option(eg:1,2,3): ")
                if(Boptions == "1"):
                    livingroom()
            elif(cheese == "1"):
                bedroomMenu4()
                Boptions = input("Enter your option(eg:1,2,3): ")
                while Boptions not in("1","2"):
                    Boptions = input("Enter your option(eg:1,2,3): ")
                if(Boptions == "1"):
                    print("Mouse eats the cheese and runs towards livingroom")
                    soil = "1"
                    return(soil)
                if(Boptions == "2"):
                    bdroom = "3"

####livingroom codeee###             
def livingroom():
    game = "0"
    while(game == "0"):
        string = "0"
        soil = "0"
        cheese = "0"
        while(string == "0"):
            livingMenu1()
            Loptions = input("Enter your option(eg:1,2,3): ")
            while Loptions not in("1","2","3","4","5"):
                Loptions = input("Enter your option(eg:1,2,3): ")
            if(Loptions == "1"):
                if(soil != "0"):
                    print("The soil is Fertilized")
                    gamewon()
                    game = "1"
                    return(game)
                if(soil == "0"):
                    print("The soil is unfertilized")
            if(Loptions == "2"):
                print("String is picked")
                string = "1"
            if(Loptions == "3"):
                (string,cheese) = attic(string,cheese)
            if(Loptions == "4"):
                soil = bedroom(string,cheese)
            if(Loptions == "5"):
                print("Player quits the game")
                game = "1"
                return(game)
        while(string == "1"):
            livingMenu2()
            Loptions = input("Enter your option(eg:1,2,3): ")
            while Loptions not in("1","2","3","4","5"):
                Loptions = input("Enter your option(eg:1,2,3): ")
            if(Loptions == "1"):
                if(soil != "0"):
                    print("The soil is Fertilized")
                    gamewon()
                    game = "1"
                    return(game)
                if(soil == "0"):
                    print("The soil is unfertilized")
            if(Loptions == "3"):
                (string,cheese) = attic(string,cheese)
            if(Loptions == "4"):
                soil = bedroom(string,cheese)
            if(Loptions == "5"):
                print("Player quits the game")
                game = "1"
                return(game)
        while(string == "2"):
            livingMenu2()
            Loptions = input("Enter your option(eg:1,2,3): ")
            while Loptions not in("1","2","3","4","5"):
                Loptions = input("Enter your option(eg:1,2,3): ")
            if(Loptions == "1"):
                if(soil != "0"):
                    print("The soil is Fertilized")
                    gamewon()
                    game = "1"
                    return(game)
                if(soil == "0"):
                    print("The soil is unfertilized")
            if(Loptions == "3"):
                (string,cheese) = attic(string,cheese)
            if(Loptions == "4"):
                soil = bedroom(string,cheese)
            if(Loptions == "5"):
                print("Player quits the game")
                game = "1"
                return(game)
def intro():
    livingroom()

intro()
    
