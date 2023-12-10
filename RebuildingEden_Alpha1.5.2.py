## REBUILDING EDEN ALPHA 0.5.5 - JACKSON HERMSMEYER -
## DEC 9 '23 RELEASE
###########################################
##############################################
###############################################
#################################################
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import sys
import os
import random
import time

class Game:
    def __init__(self, day):
        self.day = day
        self.Locations = ["House(-8,9)", "House(-7,9)", "House(-6,9)"]
        
##slowly puts out text

    def slow_print(self, str, delay = 0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
    print("\n")


## clears console for neater screen
    def reset_console(self):
        print("\n")
        os.system('cls||clear')


## print replacement
    def fprint(self, str, delay = 0):
        print("\n" + str )
        time.sleep(delay)

    def sprint(self, str, delay = 0):
        print(str)
        time.sleep(delay)

    def die(self):
        time.sleep(2)
        self.reset_console
        game.fprint("You are dead.", 2)
        game.fprint(f"You survived for {game.day} days.", 2)
        time.sleep(3)
        self.reset_console()
        game.play_again()
    
    def play_again(self):
        self.fprint("Do you want to play again?", 1)
        print("(1) Yes (2) No")
        while True:
            a = input("\n> ")
            if a == "1":
                self.fprint("Taking you to the main menu...")
                time.sleep(2)
                self.reset_data()
                self.menu()
            elif a == "2":
                self.fprint("Okay then.")
                     
            else:
                self.fprint("Invalid command!")




## setting up dialogue box for all avb cmmnds
    def commands(self):
        print("""\n This is the list of commands you may input to move around and interact with the game world. \n
    'help'       ----    shows this page
    'quit'       ----    quits the game
    'n'          ----    moves the player north
    'e'          ----    moves the player east
    's'          ----    moves the player south
    'w'          ----    moves the player west
    'map'        ----    opens the player's map
    'location'   ----    shows the player's current map coordinates
    'crafting'   ----    opens the crafting menu
    'bandage'    ----    restores some of the player's health (requires bandage)
    'treat'      ----    restores a majority of the player's health (requires medkit)
    'sleep'      ----    allows the player to sleep, and restores the player's energy (requires 1 wood to make a fire)
    'eat'        ----    restores player's hunger (requires food)
    'drink'      ----    restores player's thirst (requires water)
    'day'        ----    shows the current day
    'health'     ----    shows the player's current stats
    'inventory'  ----    shows the player's current inventory
    'patchnotes' ----    shows the current patchnotes for your version of the game
    
    """)
## crafting menu

    def crafting(self):
        print("""This is a list of all craftable items in the game.
       
              
        SUPPORT
        Camp  (WIP)         ----    100 Wood + 5 Tarp                   ----    'set camp'
        Bandage             ----    1 Cloth                             ----    'craft bandage'
        2 Cloth             ----    1 Tarp                              ----    'craft cloth'
        
        
              
        TOOLS      
        Scrap Axe           ----    1 Roadsign + 1 Metal Pipe + 1 Rope  ----    'craft scrap axe'
        

        ARMOR
        Mkshft Armr (WIP)   ----    1 Ceramic + 1 Rope                  ----    'craft makeshift armor'
        
        
        
        
        """)

## main menu actions
    def menu(self):
            self.reset_console
            self.fprint("""     
            
                    Rebuilding Eden
        Alpha 0.5.5 Release - By Jackson Hermsmeyer
                     Type 'play'.
            
            
            
            
            
            
            """)

            while True:
                userAction = input("\n> ")
                if userAction == "play":
                    self.start_intro()
                elif userAction == "quit":
                    sys.exit
                elif userAction == "help":
                    self.commands()
                elif userAction == "info":
                    self.fprint("© Jackson Hermsmeyer 2022-23")
                else:
                    self.fprint("Invalid command! Enter 'play' to launch the game, 'quit' to quit, 'info' for info, or 'help' for help.")
            

 ## pre-intro
    def start_intro(self):
        self.reset_console()
        print("\n")
        self.slow_print("...loading...", 0.2)
        self.reset_console()
        self.fprint("Do you want to skip the intro?")
        self.fprint("(1) Yes (2) No")

##skip intro
        while True:
            a = input("\n> ")
            if a == "1":
                self.reset_console()
                self.fprint("After reminiscing about old times, you get up, and decide to trek onward.")
                self.main()
               
            elif a == "2":
                self.intro()
            else:
                self.fprint("That is an invalid command. Please input a valid command.")

###################################### intro sequence
    def intro(self):
        self.reset_console()
        print("\n")
        self.slow_print(
        " Your sleep takes you to a not-so-distant memory.  "
     )
        self.slow_print(
        " \n A news anchor. A record-breaking solar flare. A collision course."

    )
        time.sleep(2)
        self.slow_print(
        " \n It was surreal. It was 12:08. Your wife was at work. Kids at school. "
    )
        self.slow_print(
        " \n You were in your cellar. The first thing you heard was the screams - unhuman."
    )
        self.slow_print(
        " \n The radiation changed them. Morphed them. Turned them. "
    )
        time.sleep(3)
        self.slow_print(
        " \n Almost no one survived."
    )
        self.slow_print(
        " \n In a stroke of merciful fate, you got out. Somehow. With the bare minimum on your back, you started out further into the Oregonian countryside, riding out the apocalypse. ")

        time.sleep(5)
        self.reset_console()

    
        self.slow_print(
        " \n \n \n You are alone. "
    )
        time.sleep(5)
        self.reset_console()
        time.sleep(1)
        self.fprint(" You are at your hastily-thrown together camp.")
        self.main()
       
#######################################
####################################### PATCH NOTES


    def patchnotes(self):
        print("""
        Rebuilding Eden Alpha 1.1 Patch Notes Dec.29 2022 
        NEW:
        - Added a new intro
        - Added different flavor text after skipping the intro
        - Crafting Menu - accessible via "crafting"
            - Added the ability to craft bandages
        - Combat Encounters
            - Added (3) Zombie encounters
        
        BUG FIXES:
       - Fixed a bug where the command "set camp" returned a null value, and crashed the program
       - Fixed a bug where the command "set camp" would print the source code of the program (after fixing the above bug)
       - Fixed a bug where health would reduce to -50 upon going west
       - Fixed a bug where drinking would deal 100 damage to the player
       - Fixed a bug where eating would deal 100 damage to the player
       - Fixed a bug where crafting 1 bandage would give you an infinite amount of bandages
       - Fixed a bug that allowed health over 100
       - Fixed a bug that killed the player after using a bandage
       - Fixed a bug that would crash the game after the intro text "You are alone" was shown
        
        
        
        
        
        ------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        
        
        Rebuilding Eden Alpha 1.2 Patch Notes Jan.1 2023
        NEW:
        - Added multiple new resources
            - Metal Wire
            - Leather strips
            - Tarp
            - Rope
        - Added a new in-text map!
            - Major locations are indicated with a letter
            - Map key indicates what that location is based upon letter
            - To see where you are, simply type in 'location', and pair it up with the map coordinates!
            - DISCLAIMER: As of right now, the map does not correspond to any in-game events; Alpha 1.3 will introduce static events based upon coordinate location on the map
        - Added new flavor text for some attacks
        - Added new flavor text for deaths
        
        
        CHANGES:
        - Reduced zombie damage from 25-50 to 10-25
        - Reduced starting load times
        - Reformatted title screen
        
        BUG FIXES:
        - Fixed multiple issues with Zombie encounters
        
        
        
        
        ------------------------------------------------------------------------------------------------------------------------------------------------
        Rebuilding Eden Alpha 1.3 Patch Notes Jan.2 2023
        
        NEW: Coordinate-Influenced Event System!
            - Added 2 new location events in the top left of the map (more to come!)
            - Added new flavor text for knife attacks
            - Added dialogue between certain characters
            - New GitHub depository!
                - DISCLAIMER: RE1.3 is NOT in its finished state! This version is as-of-yet not debugged, and much has still not been playtested.
        
        CHANGES:
            - Scavenging chance increased from 30% -> 50%
                - You can only scavenge in a location once / move
                - i.e. you move to (0,1), scavenge, move to (0,2), scavenge, and then move back to (0,1) and you may scavenge again. (THIS WILL BE REMOVED SOON, AS IN THE FUTURE SCAVENGING WILL BE DONE AUTOMATICALLY)
            - Fixed spelling error in opening intro

        BUG FIXES:
            - Fixed a bug that would allow you to enter a house by going West ???
            - Fixed self.die() function that wouldn't allow you to die
            - Fixed enemies from becoming fucking immortal and having negative health
            - Fixed a bug that printed the map infinitely (loop error)
            - Fixed not being able to quit the game
            - Fixed a bug that restarts your computer after going to the coordinate (1000,1000) ( I set up macro to see the limits of the coord system. I found it.)




        ------------------------------------------------------------------------------------------------------------------------------------------------
        Rebuilding Eden Alpha 1.4 Patch Notes Feb. 21
        
        NEWS: I've started working on the game again!

        NEW:
            - None
        BUG FIXES:
            - Fixed multiple sytnax bugs
            - Fixed locational bugs
            - Fixed inventory bugs
            - Fixed a bug that prevented you from crafting a bandage




        ------------------------------------------------------------------------------------------------------------------------------------------------
        Rebuilding Eden Alpha 1.5 Patch Notes Mar. 6
        NEW: 
            - Created outer boundaries
            - New mountain flavor text
            - Created save game framework (should be put in by 1.6 or 1.7)
        BUG FIXES:
            - Fixed a bug that did not allow you to choose not to enter buildings
            - Sytnax errors
            - Spelling / Grammar errors


        -------------------------------------------------------------------------------------------------------------------------------------------------
        
        Rebuilding Eden Alpha 1.5.3 Patch Notes


        NEW: 
            - You may now actually restart the game!
            - Dynamic Map System
                - Able to see current location directly on the map
                - Updated grid lines to make the map smoother
            - Added 1 new location in the north west corner (Up to 3 now!)
            - Added debug biome descriptions for grasslands + river
            - Added some debug commands
            - Items in inventory now stack 
                - ex: Cloth x2
            - New Biome marker system
                - Will be used in the future to generate random events.
            
        BUG FIXES:
            - Fixed a few function call errors
        
        CHANGES:
            - A few spelling mistakes


        -------------------------------------------------------------------------------------------------------------------------------------------------

        Rebuilding Eden Alpha 0.5.4 Patch Notes Dec. 8, '23
        
        NEWS: Production of RE has begun again! I can't wait to restart again.
        
        NEW:
              - Changed version number to represent alpha status
              - Finished level design on two-story white house
              - Biome Marker system fully released for the following biomes:
                    1) Forest
                    2) Roads (80%)
        BUG FIXES:
              - None
        
        CHANGES:
              - A few spelling mistakes

        -------------------------------------------------------------------------------------------------------------------------------------------------
              
        Rebuilding Eden Alpha 0.5.5 Patch Notes Dec. 9, '23
        NEW:
              - Added Axe
              - Added Scrap Axe
              - Added Makeshift Body Armor (WIP)
              - Added Body Armor (WIP)
              - Added Civilian Gas Mask (WIP)
              - Added Road Flare (WIP)
              - Added 2 Quest Items (Quest system still in progress)
              - Added 4 additional road events
              - Added Shotgun
              - Added additional flavor text for pistol combat 
       
        BUG FIXES:
              - Fixed the 'drink' command
              
        CHANGES:
              - Reduced Road Event Spawn Rate
              - Adjusted debug commands 
              - Adjusted Crafting Menu to reflect new craftable items
              - Spelling mistakes
              - Grammar mistakes

              

         
        
        
        
        
        
        
        
        """)
     
    
    
    
    def reset_data(self):
        global game, player
        game = Game(1)
        player = Player(0, 0, 100, 100, 100, 100, 0, 500, 20, 0, 0, "Null")
        player.items = []
        player.items.append("Knife")
        player.items.append("Pistol")
        self.start_intro
        


## prints out inventory
    def print_inventory(self):
        player.update_ammo
        self.fprint("Inside your pack:")
        print("Gold: ", player.gold)
        print("Pistol Ammo: ", player.pistol_ammo)
        print("Shotgun Ammo: ", player.shotgun_ammo)
        print("Rifle Ammo: ", player.rifle_ammo)
        item_count = {}
        for item in player.items:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

    # Print items with their count
        for item, count in item_count.items():
            print(f"{item} x{count}")
       
       

### shows current location
    def print_location(self):
        print(f"\nLocation: {player.x}, {player.y}")

# shows current day
    def print_day(self):
        print("\nDay:", game.day)
   
    def print_health(self):
        print("\nHealth: ", player.health)
        print("Hunger: ", player.hunger)
        print("Energy: ", player.energy)
        print("Thirst: ", player.thirst)

## updates player's temp stats
    def update_state(self):
        player.lose_energy()
        player.lose_hunger()
        player.lose_thirst()
        if (player.x == -9 and player.y == 9) or (player.x == -9 and player.y == 5) or (player.x == -4 and player.y == 5) or (player.x == -8 and player.y == 0) or (player.x == -8 and player.y == -3) or (player.x == -4 and player.y == 1) or (player.x == -4 and player.y == -5) or (player.x == 5 and player.y == -2) or (player.x == 7 and player.y == -9) or (player.x == 9 and player.y == -4) or (player.x == -9 and player.y == 4) or (player.x == -8 and player.y == 4) or (player.x == -7 and player.y == 4) or (player.x == -6 and player.y == 4) or (player.x == -4 and player.y == 5) or (player.x == -5 and player.y == 4) or (player.x == -4 and player.y == 4):
            player.biome = "Grassland"
        elif (player.x == -9 and player.y == -3) or (player.x == -9 and player.y == -4) or (player.x == -8 and player.y == -4) or (player.x == -8 and player.y == -5) or (player.x == -8 and player.y == -6) or (player.x == -7 and player.y == -6) or (player.x == -7 and player.y == -8) or (player.x == -6 and player.y == -8) or (player.x == -5 and player.y == -8) or (player.x == -4 and player.y == -8) or (player.x == -4 and player.y == -9) or (player.x == -3 and player.y == -9) or (player.x == -2 and player.y == -9):
            player.biome = "River"
        elif ( -8 <= player.x <=7 and player.y == 8) or (player.x == 4 and -2 <= player.y <= 7) or ( -2 <= player.x <= 3 and player.y == -6) or (-8 <= player.x <= -2 and player.y == -7) or (player.x == 7 and 5 <= player.y <= 8) or (player.x ==8 and player.y == 5) or (player.x == 3 and player.y == -5) or (player.x == 3 and player.y == -4) or (player.x ==3  and player.y == -3) or (player.x ==3 and player.y == -2):
            player.biome = "Road" 
        elif (player.x == 9 and player.y == 5) or (player.x == -9 and player.y == -7):
            player.biome = "Tunnel"
        elif (-8 <= player.x <= -5 and player.y == 9) or (player.x == -10 and 8 <= player.y <= 6) or (-8 <= player.x <= -5 and player.y == 5) or (player.x == -5 and player.y == -2) or (player.x == 6 and player.y == -2) or (player.x == 7 and player.y == -2) or (player.x == 6 and player.y == -4) or (player.x == 5 and player.y == -9):
            player.biome = "House"
        elif (-10 <= player.x <= 10 and player.y == -10) or (player.x == 10 and -10 <= player.y <= 10) or (player.x == -10 and -10 <= player.y <= 10) or (-10 <= player.x <= 10 and player.y == 10):
            player.biome = "Mountain"
        else:
            player.biome = "Forest"



    

## input + outputs for player commands
    def player_command(self, a):
        if a == "eat":
            player.eat()
        elif a == "drink":
            player.drink()
        elif a == "sleep":
            player.sleep()
        #tool usage
        elif a == "use axe":
            player.axeTool()


       #crafting commands
        elif a == "craft bandage":
            player.craft_bandage()
        elif a == "craft cloth":
            player.craft_cloth()
        elif a == "craft scrap axe":
            player.craft_scrap_axe()
        elif a == "craft rope":
            player.craft_rope()
       
       
       
       
       # misc
        elif a == "day":
            self.print_day()
        elif a == "health":
            self.print_health()
        elif a == "inventory":
            self.print_inventory()
        elif a == "bandage":
            player.bandage()
        elif a == "treat":
            player.treat()
        elif a == "location":
            self.print_location()
        elif a == "help":
            self.commands()
        elif a == "quit":
            sys.exit()
        elif a == "crafting":
            self.crafting()
        elif a == "patchnotes":
            self.patchnotes()
        elif a == "map":
            self.print_map()
        elif a == "read map":
            self.read_map()
        
        #debugging commands
        
        elif a == "biome":
            print(player.biome)
        elif a == "items":
            player.items.append("Cloth")
            player.items.append("Cloth")
            player.items.append("Cloth")
            player.items.append("Cloth")
            player.items.append("Cloth")
            player.items.append("Cloth")
            player.items.append("Food")
            player.items.append("Bandage")
            player.items.append("Road Sign")
            player.items.append("Rope")
            player.items.append("Rope")
            player.items.append("Ceramic")

        
        else:
            return False
        return True
    

    def print_map(self):
        world_map =  [['10 ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 9 ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 8 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 7 ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTMAGENTA_EX}S{Style.RESET_ALL} ', f' {Fore.LIGHTMAGENTA_EX}S{Style.RESET_ALL} ', f' {Fore.LIGHTMAGENTA_EX}S{Style.RESET_ALL} ', f' {Fore.LIGHTMAGENTA_EX}S{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 6 ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 5 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}T{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 4 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 3 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 2 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 1 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      [' 0 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-1 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-2 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-3 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-4 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-5 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-6 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-7 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}T{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-8 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-9 ',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.CYAN}R{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.YELLOW}H{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTGREEN_EX}G{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.GREEN}F{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['-10',f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ', f' {Fore.LIGHTBLACK_EX}X{Style.RESET_ALL} ',],
                      ['   ', '-10','-9 ','-8 ','-7 ','-6 ','-5 ','-4 ','-3 ','-2 ','-1 ',' 0 ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10'] ] 
        
    # Convert coordinates to indices for the map array
        map_size =22
        row = map_size - 1 - (player.y + map_size // 2)
        col = player.x + map_size // 2
    

        world_map[row][col] = f'{Fore.RED} U {Style.RESET_ALL}'

        
        
        map_size =22

    # Print the top border
        print("┌" + "───" * (map_size) + ("──" * 10) + "─" + "┐")

    # Print the map content
        for i, row in enumerate(world_map):
            row_str = "│"
            for cell in row:
                row_str += "" + cell + "│"
            print(row_str)

        # Print horizontal lines between rows, except for the last row
            if i < map_size - 1:
                print("├" + "───┼" * (map_size - 1) + "───┤")

    # Print the bottom border
        print("└" + "───" * map_size + ("──" * 10) + "─" + "┘")
        
        print("""  
                    MAP KEY
       
        U           ------          Player Location
        F           ------          Forest
        G           ------          Prarie
        H           ------          House
        S           ------          Store
        X           ------          Mountains
        T           ------          Highway Tunnel
        Grey R      ------          Road
        Blue R      ------          River
                                                        """)   

        
  






    def indoorZombie(self):
        while True:
            randomItem = random.randint(1, 5)
            if randomItem == 1:
                randomItem = "Cloth"
            elif randomItem == 2:
                randomItem = "Rope"
            elif randomItem == 3:
                randomItem = "Metal Wire"
            elif randomItem == 4:
                randomItem = "Tarp"
            elif randomItem == 5:
                randomItem = "Leather strip"
            player.fight("zombie", 100, random.randint(1, 25), randomItem, True, "It")
            break

## ZOMBIE ENCOUNTER
    def zombie(self):
        zombie_encounter = random.randint(1,3)
        if zombie_encounter == 1:
            self.fprint("As you walk along, you hear the distinct sound of fast shuffling behind you. Whirling around, you're met face to face with a mutant zombie! \nWill you fight(f) or run away(r) ?")
        elif zombie_encounter == 2:
            self.fprint("You walk past a clump of decaying corpses, paying no heed to them. But suddenlly, one of the bodies move! A zombie leaps at you, barely missing. \nWill you fight(f) or run away(r) ?")
        elif zombie_encounter == 3:
            self.fprint("A zombie emerges from the shadows, intent on your demise. Its head is oozing blood, which trickles down like some unholy waterfall. \nWill you fight(f), or run away(r)? ")
        while True:
            a = input ("\n> ")
            randomItem = random.randint(1, 5)
            if randomItem == 1:
                randomItem = "Cloth"
            elif randomItem == 2:
                randomItem = "Rope"
            elif randomItem == 3:
                randomItem = "Metal Wire"
            elif randomItem == 4:
                randomItem = "Tarp"
            elif randomItem == 5:
                randomItem = "Leather strip"
            if a == "r":
                escape = random.choice([True, False])
                if escape == True:
                    time.sleep(2)
                    self.fprint("You managed to escape, adrenaline pumping through your veins.")
                    break
                elif escape == False:
                    time.sleep(2)
                    self.fprint("You attempt to run, but trip and fall! As you struggle to get up, the zombie quickly closes the distance, leaving you with no choice but to fight!")
                    player.fight("zombie", 100, random.randint(1, 25), randomItem, True, "It")
            elif a =="f":
                player.fight("zombie", 100, random.randint(1,25), randomItem, True, "It")
            else: 
                self.fprint("That is an invalid command!")
                break
    def roadZombie(self):
        while True:
            randomItem = random.randint(1, 5)
            if randomItem == 1:
                randomItem = "Cloth"
            elif randomItem == 2:
                randomItem = "Rope"
            elif randomItem == 3:
                randomItem = "Metal Wire"
            elif randomItem == 4:
                randomItem = "Tarp"
            elif randomItem == 5:
                randomItem = "Leather strip"
            player.fight("zombie",100,random.randint(1,25), randomItem, True, "It")    
            break            
            
   
   
   
   
    
   
    def main(self):
        self.commands()
        while True:
            a = input("\n")
            if a == "n":
                self.reset_console()

                player.y += 1
                self.update_state()
            
                self.print_map()
                self.fprint("You went north.")
                self.check_event()
               
                
                
            
            elif a == "s":
                self.reset_console()
                
                player.y -= 1
                self.update_state()
                
                self.print_map()
                self.fprint("You went south.")
                self.check_event()
                
                
                
            elif a == "w":
                
                
                self.reset_console()
                player.x -= 1
                self.update_state()
                
                self.print_map()
                self.fprint("You went west.")
                self.check_event()
                
                
            elif a == "e":
                self.reset_console()

                player.x += 1
                self.update_state()
                
                self.print_map()
                self.fprint("You went east.")
                self.check_event()

                
                
                
                
            elif self.player_command(a):
                pass
            else:
                self.fprint("That is an invalid command. Please type in a valid command. Type in 'help' if you need help.")
    



    def check_event(self):

        

        tarp_used_blue_house = False


        if player.x == -8 and player.y == 9 and "House(-8,9)" in self.Locations:
            #LOCATION ID: House(-8,9)
            time.sleep(3)
            ## rando variables needed

            self.fprint("""
            
            
You stand on the grass in front of a brightly colored, white, one story house. 
The green grass has flourished with the lack of human intervention, and has overgrown the picket fence that encloses the yard.
To the north and west rise the great mountains, with one house to your south and another to your east. 
There are two boarded up windows to the left and right of the main door, with old, dried blood caking parts of the walls besides the door. You see no motion inside from out here, but you have low visibility.
Type 'enter' to enter, or continue on through the town. """)
            while True:
                a = input("\n>")
                if a == "enter":
                    time.sleep(2)
                    self.fprint("""
You carefully open the front door to the house, and step inside. As you step into the house, you realize that it's completely wide open - all the walls that would've sectioned off rooms have been deconstructed.
There is no furniture, only scrap wood and metal is scattered across the floor.""")
                    house_random_event = random.randint(1,3)
                    time.sleep(2)
                    if house_random_event == 1:
                        self.fprint("Suddenly, a zombie crawls out from under a large piece of plywood, intent on your demise! You are cornered and in a building, making escape an impossibility. \nYou ready yourself for a gruesome fight!")
                        time.sleep(5)
                        self.indoorZombie()
                    elif house_random_event ==2:
                        sack_location = random.randint(1,5)
                        if sack_location == 1:
                            sack_location = "a random barrel"
                        if sack_location ==2:
                            sack_location = "a broken table"
                        if sack_location == 3:
                            sack_location = "a shattered mirror"
                        if sack_location == 4: 
                            sack_location = "a dirty mattress"
                        if sack_location == 5:

                            sack_location = "a half-eaten corpse"
                        self.fprint(f"It seems like a scavenger has been through here, and left some supplies in a sack on {sack_location}.")
                        time.sleep(2)
                        self.fprint("You found Cloth, Food, and Water!")
                        player.items.append("Cloth")
                        player.items.append("Food")
                        player.items.append("Water")
                    elif house_random_event == 3:
                        self.fprint("As you walk through the house, a zombie falls out of the ceiling, nearly falling onto you! You trip backwards, struggling to get back up. You are cornered and in a building, making escape an impossibility.  \nYou ready yourself for a hard fight!")
                        time.sleep(5)
                        self.indoorZombie()
                        self.Locations.remove("House(-8,9)")
                self.fprint("You step away from the house.")
                break      
        elif player.x == -8 and player.y == 9 and "House(-8,9)" not in self.Locations:
            self.fprint("This is the same one-story house with boarded up windows. The dried blood seems to be older still. \nType enter to enter, or continue on through the town.")
            while True:
                a = input("\n>")
                if a == "enter":
                    time.sleep(2)
                    self.fprint("""
Carefully going back into the white building, everything seems to be the same. It's obvious someone has been here though, and you may find more resources (or dangers) within..""")
                    house_random_event = random.randint(1,3)
                    if house_random_event == 1:
                        self.fprint("Suddenly, a zombie crawls out from under a large piece of plywood, intent on your demise! You are cornered and in a building, making escape an impossibility. \nYou ready yourself for a gruesome fight!")
                        time.sleep(5)
                        self.indoorZombie()
                    elif house_random_event ==2:
                        sack_location = random.randint(1,3)
                        if sack_location == 1:
                            sack_location = "a random barrel."
                        if sack_location ==2:
                            sack_location = "a broken table."
                        if sack_location == 3:
                            sack_location = "a shattered mirror"
                        self.fprint(f"It seems like a scavenger has been through here, and left some supplies in a sack on {sack_location}.")
                        time.sleep(2)
                        self.fprint("You found Cloth, Food, and Water!")
                        time.sleep(2)
                        player.items.append("Cloth")
                        player.items.append("Food")
                        player.items.append("Water")
                    elif house_random_event == 3:
                        self.fprint("As you walk through the house, a zombie falls out of the ceiling, nearly falling onto you! You trip backwards, struggling to get back up. You are cornered and in a building, making escape an impossibility.  \nYou ready yourself for a hard fight!")
                        time.sleep(5)
                        self.indoorZombie()
                self.fprint("You step away from the house, and onto the sidewalk.")
                break
        
        elif player.x == -7 and player.y == 9 and "House(-7,9)" in self.Locations:
            ## LOCATION ID: HOUSE(-7,9)
            time.sleep(3)
            
            
            self.fprint("You stand on the grass in front of a blue, one story house.")
            time.sleep(3)
            self.fprint("To your north lie the great mountains. To the west is a white townhouse, and to the east a teal townhouse. To your south lies the 2 lane country road.")
            time.sleep(5)
            self.fprint(" The blue house is...off...somehow. Its foundations on the east side seem to be sinking a bit, and the one large window on the right side of the front of the house has been completely shattered.")
            time.sleep(5)
            self.fprint("The door on the left has been completely barricaded, and upon inspection, you are unable to open it. The only way inside would be through the window.")
            time.sleep(5)
            self.fprint(" Upon inspection of the window frame, it is at head height, requiring you to lift yourself within, posing a severe danger to yourself as the jagged and sharp edges of the glass would surely cut your hands and legs.")
            time.sleep(5)
            self.fprint("A tarp thick enough would protect you from the glass, at least for a second.")
            time.sleep(4)

            self.fprint("""
Type 'enter' to enter without any protection from the window.
Type 'enter with tarp' to enter the window with protection from the glass. (Requires a Tarp.)
Or, continue to explore the town.
            """)        
            while True:
                a = input("\n>")
                if a == "enter":
                    self.fprint("You mutter to yourself 'Fuck it' and jump inside. You misplace your hands so badly jumping up that both your palms become penetrated by thick shards of glass, staining your hands with blood almost immediately.")
                    time.sleep(5)
                    player.lose_health()
                elif a == "enter with tarp":
                    if "Tarp" in player.items:
                        player.items.remove("Tarp")
                        self.fprint("You throw the thick tarp over the window, allowing you to crawl inside without harming yourself. Pulling it off would end up tearing it beyond usability, so you keep it on the window frame for now.")
                        time.sleep(5)
                        tarp_used_blue_house = True
                    elif "Tarp" not in player.items:
                        self.fprint("You check your bag and realize you have no tarp to use. \nYou mutter to yourself 'Fuck it' and jump inside. \nYou misplace your hands so badly jumping up that both your palms become penetrated by thick shards of glass, staining your hands with blood almost immediately. ")
                        time.sleep(5)
                    else:
                        self.fprint("That is an invalid command! Type 'help' to get a list of commands.")
                else:
                    self.fprint("You step away from the house.")
                    break               
                self.fprint("Standing in the foyer of the house, the house doesn't look that bad considering the apocalypse. The carpet looks shaggy under your feet, but much of the furniture is unbroken and clean. \n")
                time.sleep(8)
                self.fprint("Wait. It's clean.")
                time.sleep(4)
                self.fprint("You begin to notice other things - an opened can of beans on a side table, a water spill on the carpet right next to the couch. Someone has been here.")
                time.sleep(8)
                self.fprint("You hear the sound of a door creaking open, down the hallway to your left. You quietly slip next to the wall right next to the hallway, hiding yourself. ")
                time.sleep(8)
                self.fprint("You can hear the slow walking of someone with heavy boots, carefully surveying the hallway, and making their way ever so close to you.")
                time.sleep(6)
                self.fprint("You hear a voice.")
                self.slow_print(f"\n{Fore.RED}Unknown Voice:{Style.RESET_ALL} Who's there?")
                time.sleep(3)
                self.fprint("""
Select a response. (1-3)
1) You don't say anything.
2) A friend!
3) Someone you don't want to mess with, so back up!
""")
                a = input("\n")
                if a == "1":
                    self.fprint("You don't say anything. As you listen, you can hear the sound of the boots getting closer and closer. \nWhat do you do?")
                    time.sleep(3)
                    self.fprint("\n1) Stay hidden, and hope for the best.\n2) Jump out from the wall and start shooting!")
                    a = input ("\n>")
                    if a == "1":                ## for sit 1
                        self.fprint("Decided to remain stealthy, you wait for the mysterious stranger to make their move first. \nAs the person slowly comes out of the hallway, he turns directly into you, and his face of momentary confusion turns to rage. \nThe man charges at you, and hits you on the head with his pistol, causing you to stagger away, losing health. ")
                        player.lose_health
                        time.sleep(5)
                        self.fprint("Now a few feet from eachother, he yells at you in apparent blind rage and begins raising his pistol to fire.")
                        randomItem = random.randint(1,3)
                        if randomItem == 1:
                            randomItem = "Cloth"
                        if randomItem == 2:
                            randomItem = "Rope"
                        if randomItem == 3:
                            randomItem = "Axe"
                        player.fight("Unknown Man", 100, random.randint(15,25), randomItem, True, "He")
                        time.sleep(4)
                        self.fprint("After a bloody battle, you managed to kill the man. After inspecting his body, you go to his room and find dozens of bullets - enough to last you a while. There's also some food and water in a cupboard.")
                        time.sleep(4)
                        player.items.append("Food")
                        player.items.append("Water")
                        player.pistol_ammo += 24
                    elif a == "2":              ## for sit 1
                        self.fprint("Taking no chances, you take a wide step into the hallway entrance and point your weapon at a man, clad it black clothing, with a pistol also trained directly at your chest!")
                        randomItem = random.randint(1,3)
                        if randomItem == 1:
                            randomItem = "Cloth"
                        elif randomItem == 2:
                            randomItem = "Rope"
                        elif randomItem == 3:
                            randomItem = "Axe"
                        player.fight("Unknown Man", 100, random.randint(15,25), randomItem, True, "He")
                        self.fprint("After your suprise attack, and with some wounds, you check the rest of the house. In the room he came from, you find a couple dozen bullets and some food and water.")
                        player.items.append("Food")
                        player.items.append("Water")
                        player.pistol_ammo += 24
                    else:
                        self.fprint("That is an invalid command! Type 'help' to see a list of commands.")
                
                
                
                
                elif a == "2":
                        self.slow_print(f"{Fore.GREEN}You:{Style.RESET_ALL} A friend! \n")
                        self.slow_print(f"{Fore.RED}Unknown Voice:{Style.RESET_ALL} What the fuck are you doing in my house?\n")
                        self.slow_print(f"{Fore.GREEN}You:{Style.RESET_ALL} Do you think we could work something out? You've come this far, it would be unfortunate to stop now.\n")
                        self.slow_print(f"{Fore.RED}Unknown Voice:{Style.RESET_ALL} Better men have tried and failed to kill me. Stop hiding and face me!\n")
                        self.slow_print(f"{Fore.GREEN}You:{Style.RESET_ALL} All right! Hard way then.\n")
                        self.fprint("You take out your trusty firearm and step into the open hallway, and train your weapon upon a man, clad in black clothing, holding a pistol in your direction.\n")
                        randomItem = random.randint(1,3)
                        if randomItem == 1:
                                randomItem = "Cloth"
                        elif randomItem == 2:
                                randomItem = "Rope"
                        elif randomItem == 3:
                                randomItem = "Axe"
                        player.fight("Unknown Man", 100, random.randint(15,25), randomItem, True, "He")
                        self.fprint("After a bloody battle, you managed to kill the man. After inspecting his body, you go to his room and find dozens of bullets - enough to last you a while. There's also some food and water in a cupboard.")
                        player.items.append("Food")
                        player.items.append("Water")
                        player.pistol_ammo += 24
                elif a == "3": 
                        self.slow_print(f"{Fore.GREEN}You:{Style.RESET_ALL} Someone you don't want to mess with, so back up!\n")
                        self.slow_print(f"{Fore.RED}Unknown Voice:{Style.RESET_ALL} No, you back up you motherfucker! Get out of my goddamn house!\n")
                        self.slow_print(f"{Fore.GREEN}You:{Style.RESET_ALL} I'm just tryna live, same as you man!\n")
                        self.slow_print(f"{Fore.RED}Unknown Voice:{Style.RESET_ALL} Fuck you!\n")
                        self.slow_print(f"{Fore.GREEN}You:{Style.RESET_ALL} You've made your choice!\n")
                        self.fprint("You take out your weapon and take a deep breath. Without another thought, you take a step out into the hallway to see a man, clad in black clothing, who is holding a pistol in your direction.")
                        randomItem = random.randint(1,3)
                        if randomItem == 1:
                            randomItem = "Cloth"
                        elif randomItem == 2:
                            randomItem = "Rope"
                        elif randomItem == 3:
                            randomItem = "Axe"
                        player.fight("Unknown Man", 100, random.randint(15,25), randomItem, True, "He")
                        self.fprint("After your suprise attack, and with some wounds, you check the rest of the house. In the room he came from, you find a couple dozen bullets and some food and water.\n")
                        player.items.append("Food")
                        player.items.append("Water")
                        player.pistol_ammo += 24
                        self.fprint("After one last examination of the house, you find nothing else of value in the house, and carefully hop out of the window, avoiding any glass.")
                game.Locations.remove("House(-7,9)")
                self.fprint("You step onto the sidewalk outside the house.")
                break
        elif player.x == -7 and player.y == 9 and "House(-7,9)" not in self.Locations:
            self.fprint("This is the same blue house from a while ago. Nothing about it seems to have changed.\n To your north lie the great mountains. To the west is a white townhouse, and to the east a teal townhouse. To your south lies the 2 lane town road.")
            time.sleep(8)
            if tarp_used_blue_house == True:
                self.fprint("The same tarp you used a while ago is still there, and would grant safe passage through the window again.")
                time.sleep(5)
            else:
                self.fprint("The window still has jagged, sharp edges around it, proving to be dangerous if you wanted to go inside again.")
                time.sleep(5)
            self.fprint("""
Type 'enter' to enter without any protection from the window.
Type 'enter with tarp' to enter the window with protection from the glass. (Requires a Tarp.)
Or, continue to explore the town.
            """)
            time.sleep(2)        
            while True:
                a = input("\n>")
                if a == "enter":
                    self.fprint("'There may still be stuff in there' you think to yourself. \nYou sigh, and carefully make your way into the tall window. You cut your hands and arms in the process, but you got in without killing yourself.")
                    player.lose_health()
                    time.sleep(2)
                elif a == "enter with tarp":
                    if "Tarp" in player.items:
                        player.items.remove("Tarp")
                        self.fprint("You throw the thick tarp over the window, allowing you to crawl inside without harming yourself. Pulling it off would end up tearing it beyond usability, so you keep it on the window frame for now.")
                        tarp_used_blue_house = True
                    elif "Tarp" not in player.items:       
                        self.fprint("Realizing you once again don't have a tarp, you mutter to yourself, 'Fuck me' and jump inside. \n You manage to get in without piercing your hands this time, but you still have cuts and scatches all over your arms and hands.")
                else: ("That is an invalid command!")
                self.fprint("The house itself has not changed at all. The man's dead body still lies in the hallway, rotting away. \nThe only noticable change in the enviroment is the excessive amount of flies. \nExamination of the rooms you've already been in prove you correct: you already got everything. This wasn't worth the hassle.")
                time.sleep(8)
                self.fprint("There's nothing else here for you. You carefully hop out of the window, avoiding any glass.")
                break
        
        elif player.x == -6 and player.y == 9 and "House(-6,9)" in self.Locations:
            visited_rooms = []

            def room_choices():
                while True:
                    self.fprint("Where do you go?")

                    if '1' not in visited_rooms:
                        self.fprint("Type '1' to enter the first opening.")
                    if '2' not in visited_rooms:
                        self.fprint("Type '2' to enter the second opening.")
                    if '3' not in visited_rooms:
                        self.fprint("Type '3' to enter the third opening.")
                    if ('1' and '2' and '3') in visited_rooms:
                        self.fprint("You have already visited all the rooms.")
                    break

                b = input("\n>")
                if b == '1' and '1' not in visited_rooms:
                    visited_rooms.append('1')
                    room1()
                elif b == '2' and '2' not in visited_rooms:
                    visited_rooms.append('2')
                    room2()
                elif b == '3' and '3' not in visited_rooms:
                    visited_rooms.append('3')
                    room3()
                else:
                    self.fprint("Invalid choice, please try again.")




            def room1():
                self.fprint("As you slowly walk into the room, you notice furniture strewn about.")                            
                time.sleep(3)
                self.fprint("There is a large kitchen table in the center, with broken chairs on the floor. In the center is a an extravagant platter of rotten food, flies buzzing.")
                time.sleep(4)
                self.fprint("There is seemingly nothing of value in this room, aside from a few strips of cloth you manage to pull up from a chair.")
                player.items.append("Cloth")
                player.items.append("Cloth")
                time.sleep(3)
                self.fprint("You walk back into the hallway.")
                room_choices()
            def room2():
                self.fprint("You take a few careful steps over to the second opening, and hear a noticable crunching noise. As you being to peer inside the room, there is a omnipresent black residue caking the ceiling and walls.")
                time.sleep(4)
                self.fprint("As you take a step inside the room, the residue seems to almost react to your presence, and the crunching stops. An uneasy, eerie silence falls over the room.")
                time.sleep(4)
                self.fprint("Now in the middle of the dark room, you turn on your flashlight to get your bearings. ")
                time.sleep(3)
                self.fprint("As you survey the room, your light seems to reflect back in one corner as you quickly sweep it across the room. You slowly turn over to the reflection, resting your flashlight on it once again.")
                time.sleep(5)
                self.fprint("The reflection looks back.")
                time.sleep(3)
                self.fprint("A pair of white, irridescent eyes is the only evidence of a being in that dark corner. As it stands up, it seems to continually get bigger and bigger, rising to a stature of at least 8 feet.")
                time.sleep(5)
                self.fprint("As it does so, it unfurls its fingers from its hands - dripping with a black tar, long, and utterly terrifying.")
                time.sleep(4)
                self.fprint("You begin backing up into a corner in the room, as your heart begins to beat within your chest. You feel only fear.")
                time.sleep(4)
                self.fprint("The black creature seems to study you for a moment, before taking a strong but slow step forward.")
                time.sleep(4)
                self.fprint("And then another.")
                time.sleep(4)
                self.fprint("Step.")
                time.sleep(.3)
                self.fprint("Step.")
                time.sleep(.3)
                self.fprint("Step.")
                time.sleep(.3)
                self.fprint("Step.")
                time.sleep(.3)
                self.fprint("Step.")
                time.sleep(.3)
                self.fprint("The creature closes the distance between the both of you in a split second, and reaches back to lash at you with its arm!")
                randomItem = random.randint(1,3)
                if randomItem == 1:
                    randomItem = "Black Ooze"
                elif randomItem == 2:
                    randomItem = "Irridescent Eye"
                elif randomItem == 3:
                    randomItem = "Blackened Tooth"
                player.fight("Black Creature", 150, random.randint(15,25), randomItem, True, "It")
                time.sleep(2)
                self.fprint("The already decaying body of the black creature seems to sink into floorboards.")
                time.sleep(2)
                self.fprint("Catching your breath, you grab the " + randomItem + " from your pack. It seems to hold a strange and unnatural power. You quickly put it away again just in case.")
                time.sleep(4)
                self.fprint("You take a few steps out of the room, and back into the hallway.")
                room_choices()
            def room3():
                self.fprint("You walk up the stairs.")
                time.sleep(1)
                self.fprint("As you ascend the stairs, your eyes are met with another disturbing sight - the same black ooze you saw before now completely covers the floor and ceiling of this second floor. \n")
                time.sleep(4)
                self.fprint("Though there was once most likely some distinct rooms up here, all the walls seemingly have disappeared, replaced by black mass.  ")
                time.sleep(3)
                self.fprint("Creeping into the main area, you find a storage box amidst the rubble and ooze. Inside, you find some supplies.")
                time.sleep(2)
                self.fprint("You found 6 cloth!")
                player.items.append("Cloth")
                player.items.append("Cloth")
                player.items.append("Cloth")
                player.items.append("Cloth")
                player.items.append("Cloth")
                player.items.append("Cloth")
                time.sleep(.5)
                self.fprint("You found 5 shotgun shells!")
                player.shotgun_ammo+= 5
                time.sleep(.5)
                self.fprint("You found an old map!")
                player.items.append("Old Map")
                time.sleep(.5)
                self.fprint("Tip: enter 'read old map' to examine the contents of the map. ")
                time.sleep(1)
                self.fprint("Not wanting to disturb whatever could be living here, you cautiously step down the stairs, and leave the building.")
                game.Locations.remove("House(-6,9)")
                return
    
            
            
            
            
            
            def cellar_opening():
                time.sleep(2)
                self.fprint("As you descend, the damp floorboards beneath your feet squeak and shake under your presence.")
                time.sleep(2)
                self.fprint("The air down in the cellar is heavy, and every move you make further into it drains you. After only a few steps, you have to catch yourself on the wall to stop from falling.")
                time.sleep(4)
                self.fprint("Do you continue? (Yes or No?)")
                a = input(">")
                if a == "Yes" or "yes":
                    self.fprint("You decide to continue into the darkness. Each step and each breath becomes more laborious, until you collapse on the floor.")
                    time.sleep(2)
                    self.fprint("In your last few moments of consciousness, you feel a slimy tendril grab you by your arm, and it pulls you into the dark depths...")
                    game.die()
                elif a == "No" or "no":
                    self.fprint("Thinking better of it, you manage to stumble out of the cellar and into the backyard of the house.")
                    return
                else:
                    self.fprint("That is an invalid command!")



            
            
            self.fprint("You stand in front of a white townhouse, its two stories a prominent and unique characteristic among the other houses in this town. There seems to be a potent stench coming from within, immediately taking over your senses. \nIt is in rough condition, but still stands, with a sturdy grey door blocking any line of sight into the building. \n")
            time.sleep(6)
            self.fprint("Closer inspection reveals that the door is unlocked.")
            time.sleep(2)
            self.fprint("""
Type 'enter' to enter through the grey door.
Type 'investigate' to go around the backside of the house.
Or, continue to explore the town. """)
            time.sleep(2)
            
            while True:
                

                a = input("\n> ")
                if a == "enter":
                    self.fprint("You walk up to the landing, and slowly open the door. \n")
                    time.sleep(1)
                    self.fprint("Your eyes are met by a long hallway, strewn with trash and assorted debris.")
                    time.sleep(2)
                    self.fprint("The stench you could smell from outside has become even more powerful - and the ceiling tiles above you have been darkened and soaked with a black substance, which slowly drips down in front of you.")     
                    time.sleep(3)
                    self.fprint("The hallway has 3 openings: one to your direct left, which leads into an adjacent room. \nThe second is in the middle of the hallway on your right, which would seemingly enter into another room. \nThe third is on the complete other end of the hallway, which seems to be the stairs to go up to the second story.")
                    time.sleep(5)
                    room_choices()
                elif a == "investigate":
                    self.fprint("You walk around the back of the building, and notice a cellar door in the ground. It seems to be unlocked")
                    time.sleep(2)
                    self.fprint("You take a deep breath, and delve inside.")
                    cellar_opening()
                else: 
                    self.fprint("You step away from the house.")
                    return
        elif player.x == -6 and player.y == 9 and "House(-6,9)" not in self.Locations:
            self.fprint("Since you've last visited this house, you've noticed that the distinct smell permeating from the house itself has lessened, and further investigation inside shows that not much else has changed.")
            self.fprint("The cellar could still be investigated, though.")
            self.frpint("Type 'enter cellar' to explore the cellar, or continue to explore the town.")
            a = input("\n> ")
            if a == "enter cellar" or "Enter cellar" or "Enter Cellar" or "enter Cellar":
                time.sleep(2)
                self.fprint("As you descend, the damp floorboards beneath your feet squeak and shake under your presence.")
                time.sleep(2)
                self.fprint("The air down in the cellar is heavy, and every move you make further into it drains you. After only a few steps, you have to catch yourself on the wall to stop from falling.")
                time.sleep(4)
                self.fprint("Do you continue? (Yes or No?)")
                a = input(">")
                if a == "Yes" or "yes":
                    self.fprint("You decide to continue into the darkness. Each step and each breath becomes more laborious, until you collapse on the floor.")
                    time.sleep(2)
                    self.fprint("In your last few moments of consciousness, you feel a slimy tendril grab you by your arm, and it pulls you into the dark depths...")
                    game.die()
                elif a == "No" or "no":
                    self.fprint("Thinking better of it, you manage to stumble out of the cellar and into the backyard of the house.")
                    return
                else:
                    self.fprint("That is an invalid command!")
            else:
                self.fprint("You step away from the house.")
                return



            
        ## death barriers
        #############################################
        elif -10 <= player.x <= 10 and player.y == -10:
            self.fprint("You stand before the mighty southern mountians, looming in front of you. Its high peaks would prove a treacherous climb, and any attempts to do so would surely end in your death. Going further south would be a death sentence.")
        elif -10 <= player.x <= 10 and player.y == -11:
            self.fprint("You decide to continue up the mountain, desiring an escape from this dangerous valley. As you head up the mountains, the cold air whips at your skin, lapping at the last of your heat. \nAs you crest over the first range, you see nothing but endless wilderness for miles. Your eyes get heavy, and the cold darkness takes you.")
            game.die()
        elif player.x == 10 and -10 <= player.y <= 10:
            self.fprint("You stand before the mighty eastern mountains, looming in front of you. Its high peaks would prove a treacherous climb, and any attempts to do so would surely end in your death. Going further east would be a death sentence.")
        elif player.x == 11 and -10 <= player.y <= 10:
            self.fprint("You decide to continue up the mountain, desiring an escape from this dangerous valley. As you head up the mountains, the cold air whips at your skin, lapping at the last of your heat. \nAs you crest over the first range, you see nothing but endless wilderness for miles. Your eyes get heavy, and the cold darkness takes you.")
            game.die()
        elif player.x == -10 and -10 <= player.y <= 10:
            self.fprint("You stand before the mighty western mountains, looming in front of you. Its high peaks would prove a treacherous climb, and any attempts to do so would surely end in your death. Going further west would be a death sentence.")
        elif player.x == -11 and -10 <= player.y <= 10:
            self.fprint("You decide to continue up the mountain, desiring an escape from this dangerous valley. As you head up the mountains, the cold air whips at your skin, lapping at the last of your heat. \nAs you crest over the first range, you see nothing but endless wilderness for miles. Your eyes get heavy, and the cold darkness takes you.")
            game.die()
        elif -10 <= player.x <= 10 and player.y == 10:
            self.fprint("You stand before the mighty northern mountians, looming in front of you. Its high peaks would prove a treacherous climb, and any attempts to do so would surely end in your death. Going further south would be a death sentence.")
        elif -10 <= player.x <= 10 and player.y == 11:
            self.fprint("You decide to continue up the mountain, desiring an escape from this dangerous valley. As you head up the mountains, the cold air whips at your skin, lapping at the last of your heat. \nAs you crest over the first range, you see nothing but endless wilderness for miles. Your eyes get heavy, and the cold darkness takes you.")
            game.die()

        ###############################################
        
        ### Biome Designated Rando Events
        elif player.biome == ("Road"):
            self.fprint("You're on an old, asphalt road, littered with abandoned cars.")

            ### ADD DESIGNATED ROADBLOCK AREA 
            ## notes:
            ## high traffic, warned off it 1 unit away.
            ## much more dangerous, higher tier loot.
            chance_road_event = random.randint(1,2)
            if chance_road_event == 1:
            

                road_event = random.randint(1,20)

                if road_event == 7:
                    self.fprint("As you walk through the maze of cars and trucks, a ganarly hand reaches out from under a sedan, grabbing your ankle!")
                    time.sleep(4)
                    self.fprint("After a brief struggle, you trip and fall on your back, trying to get away. A zombie rises from under the sedan, lashing out!")
                    time.sleep(4)
                    self.roadZombie()
                    pass
                if road_event == 2:
                    descriptor_word = " a "
                    randomRoadItem = random.randint(1,5)
                    if randomRoadItem == 1:
                        randomRoadItem ="Metal Spring"
                    if randomRoadItem == 2:
                        randomRoadItem = "Cloth"
                        descriptor_word = " a piece of "
                    if randomRoadItem == 3:
                        randomRoadItem = "Metal Pipe"
                    if randomRoadItem == 4:
                        randomRoadItem = "Ceramic"
                        descriptor_word = " a piece of "
                    if randomRoadItem == 5:
                        randomRoadItem = "Medkit"

                    self.fprint("A large van stands in the middle of the road, its trunk slightly popped open.")
                    time.sleep(2)
                    self.fprint("You slowly and cautiously open the trunk, and find" + descriptor_word + randomRoadItem + "!")
                    player.items.append(randomRoadItem)
                    time.sleep(2)
                    pass

                ########################################################## ROAD EVENT WIP
                if road_event == 3:
                    self.fprint("You spot an old stop sign on the side of the road with a sharp edge, and pick it up for safe keeping. ")
                    player.items.append("Road Sign")
                    time.sleep(1.9)
                    self.fprint("You found a Road Sign!")
                
                if road_event == 4:
                    police_car_descriptor_word = " a "
                    police_car_loot = random.randint(1,5)
                    if police_car_loot == 1:
                        police_car_loot = "Shotgun"
                        police_car_descriptor_word = " a "
                    if police_car_loot == 2:
                        police_car_loot = "Body Armor (WIP)"
                        police_car_descriptor_word = " "
                    if police_car_loot == 3:
                        police_car_loot = "Road Flare"
                        police_car_descriptor_word = " a "
                    if police_car_loot == 4:
                        police_car_loot = "Civilian Gas Mask"
                        police_car_descriptor_word = " a "
                    if police_car_loot == 5:
                        police_car_loot = "Medkit"
                        police_car_descriptor_word = " a "
                
                    self.fprint("As you walk down the road, you come upon an old police squad car. Inside, you grab" + police_car_descriptor_word + police_car_loot + "!")
                    player.items.append(police_car_loot)
                    time.sleep(3)
                    self.fprint("You found" + police_car_descriptor_word + police_car_loot + "!")
                
                if road_event == 5:
                    dead_body_descriptor = random.randint(1,2)
                    dead_pronoun = random.randint(1,2)

                    if dead_body_descriptor == 1:
                        dead_body_descriptor = "raider."
                    elif dead_body_descriptor == 2:
                        dead_body_descriptor = "scavenger."
                    
                    if dead_pronoun == 1:
                        dead_pronoun = "her"
                    if dead_pronoun == 2:
                        dead_pronoun = "his"
                    self.fprint("You come upon the long-dead body of a " + dead_body_descriptor + "Upon opening " + dead_pronoun + " pack, you find some food and water.")
                    player.items.append("Water")
                    player.items.append("Food")
                    time.sleep(2)
                    self.fprint("You found Water!")
                    time.sleep(.4)
                    self.fprint("You found Food!")
                
                if road_event == 6:
                    self.fprint("The gravel of the old paved road crunches under your feet as you pass by multiple wrecked cars.")
                    time.sleep(2)
                    self.fprint("You manage to grab a few pieces of scrap metal before leaving.")
                    time.sleep(1.2)
                    player.items.append("Scrap Metal")
                    player.items.append("Scrap Metal")
                    self.fprint("You found 2 Scrap Metal!")
            
        
        elif player.biome == ("Forest"):
            jacob_letter_found = False
            self.fprint("You're in a forest. Trees stretch around and above you on all sides.")
            chance_forest_event = random.randint(1,10)
            if chance_forest_event == (1):
                if jacob_letter_found == True:
                    forest_event = random.randint (1,4)
                else:
                    forest_event = random.randint(1,5)
                
                if forest_event == 1:
                    self.fprint("As you walk through the forest, you hear the brisk shuffing of feet behind you. As you turn around, you are suddenly faced with a zombie!")
                    time.sleep(2)
                    self.zombie()
                    return
                if forest_event == 2:
                    self.fprint("You stumble upon an apple tree, ripe for the picking. You take as many as you can carry, and then move on.")
                    time.sleep(2) 
                    self.fprint("You found 3 food!")
                    player.items.append("Food")
                    player.items.append("Food")
                    player.items.append("Food")
                if forest_event == 3:
                    self.fprint("As you walk amongst the trees, you feel like someone is watching you.")
                    time.sleep(2)
                    self.zombie()
                    time.sleep(2)
                    return
                if forest_event == 4:
                    self.fprint("The trees give way to a small clearing, and in the center lies a hastily torn down camp - with some resources strewn about. ")
                    time.sleep(4)
                    camp_items = random.randint(1,3)
                    if camp_items == 1:
                        player.items.append("Wire")
                        player.items.append("Circuit Board")
                        time.sleep(2)
                        self.fprint("A busted up speaker yields some wire, and a circuit board.")
                        time.sleep(2)
                    if camp_items == 2:
                        player.items.append("Cloth")
                        player.items.append("Medkit")
                        player.items.append("Tarp")
                        time.sleep(2)
                        self.fprint("You find some cloth, a tarp, and a medkit.")
                        time.sleep(3)
                    if camp_items == 3:
                        player.items.append("Cloth")
                        player.items.append("Cloth")
                        player.pistol_ammo += 12
                        time.sleep(2)
                        self.fprint("You find some cloth, and 12 rounds for your pistol strewn about.")
                        time.sleep(3)
                if forest_event == 5:
                    self.fprint("As you walk through the forest, the distinct smell of death hits you. A few feet away, a man wearing street clothes is slumped against a tree, with a knife stuck in his chest.")
                    time.sleep(3) 
                    self.fprint("\nAn investigation of his body reveals a distinct bite on his neck.")
                    time.sleep(3)
                    self.fprint("\nYou notice a crunched up piece of paper in his left. \nThe letter, scrawled in pencil, with a few blood droplets on it, reads:")
                    time.sleep(3)
                    self.fprint("""

                    
Connor,


I'm so sorry. You probably won't ever get this. I don't even know why I'm writing it.
I'm not letting it take me. Tell all the guys at Eden I love 'em. Tell Mom I love her.

I can feel it coming on again. 
Goodbye.

Jacob.
                    
                    
                    
                                
                    
                    """)
                    time.sleep(5)
                    
                    player.items.append("Jacob's letter")
                    jacob_letter_found = True
                    self.fprint("You stuff the letter in your pocket, pay your respects, and continue on.")
                    time.sleep(3)
                

                else: pass
                        
        
        
        
        
        
        else: pass


                        
                        
                        
                                 
                        
                        
                        


class Player:
    def __init__(self, x, y, health, hunger, energy, thirst, attack, gold, pistol_ammo, shotgun_ammo,
    rifle_ammo, biome):
        self.items = []
        self.x = x
        self.y = y
        self.health = health
        self.hunger = hunger
        self.energy = energy
        self.thirst = thirst
        self.attack = attack
        self.gold = gold
        self.pistol_ammo = pistol_ammo
        self.shotgun_ammo = shotgun_ammo
        self.rifle_ammo = rifle_ammo
        self.biome = biome
   ## bandages
    def bandage(self):
        if "Bandage" in self.items and self.health < 100:
            self.health += 15
            game.fprint("You bandaged your wound, providing a small health boost.")
            self.items.remove("Bandage")
            if self.health > 100:
                self. health = 100
        elif "Bandage" not in self.items:
            game.fprint("You don't have any bandages.")
        else:
            game.fprint("Your health is already full.")
    ## medkits
    def treat(self):
        if "Medkit" in self.items and self.health < 100:
            self.health += 50
            game.fprint("You have effectively treated yourself of your wounds, providing a great health boost.")
            self.items.remove("Bandage")
            if self.health > 100:
                self.health = 100
        elif "Medkit" not in self.items:
            game.fprint("You do not have any Medkits.")
        else:
            game.fprint("Your health is already full.")
            

    def read_map(self):
        if "Old Map" in self.items:
            game.fprint("You take the old map out of your pack, and open it up.")
            time.sleep(1)
            game.fprint("The map itself is caked with blood on the right corner, and depicts a small area in the south-east of the valley. ")
            time.sleep(3)
            game.fprint("A large 'X' has been drawn over a grid on the small map, which, after coordinating it with your other map, seems to be nearby the cell (-7, 9)")
            time.sleep(3)
        else:
            game.fprint("You have no other map to read!")




  ## function for setting camp
    def sleep(self):
        if "Wood" in self.items:
            self.items.remove("Wood")
            self.lose_hunger()
            self.lose_thirst()
            player.energy = 100
            game.day +=1
            game.fprint("You light a small fire, and sleep by its heat in the crisp Oregonian weather.")
        else:
            game.fprint("You don't have any wood to make a camp fire. Without its warmth, you dare not sleep under these stars.")
   ## function for eating
    def eat(self):
        if "Food" in self.items and self.hunger <100:
            self.items.remove("Food")
            self.hunger = 100
            self.health += random.randint(5,10)
            if self.health > 100:
                self.health = 100
            game.fprint("You sit down and have a quick bite to eat. Your hunger has been satiated, for now.")
        elif "Food" not in self.items:
            game.fprint("You don't have any food to eat.")
        else:
            game.fprint("You aren't hungry.")
    def axeTool(self):
        if "Axe" or "Scrap Axe" in self.items and self.biome == "Forest":
            self.fprint("Lifting your axe out of your pack, you appreach the nearest tree and begin to hack it down.")
            time.sleep(2)
            self.fprint("After some time, you fell the tree, cutting it up into usable pieces.")
            self.fprint("You found 8 wood!")
            self.lose_energy()
            self.lose_energy()
            self.items.append("Wood")
            self.items.append("Wood")
            self.items.append("Wood")
            self.items.append("Wood")
            self.items.append("Wood")
            self.items.append("Wood")
            self.items.append("Wood")
            self.items.append("Wood")
        elif "Axe" or "Scrap Axe" in self.items and self.biome != "Forest":
            self.fprint("You need to be in a forest in order to chop down trees.")
        else: 
            self.fprint("You need an axe to chop down trees.")
            





## CRAFTING CRAFTING CRAFTING CRAFTING CRAFTING CRAFTING CRAFTING CRAFTING
    def craft_bandage(self):
        bandageFailChance = random.randint(1,10)
        if "Cloth" in self.items:
            if bandageFailChance == (1):
                self.items.remove("Cloth")
                game.fprint("As you begin rolling the cloth together, its feeble fibers break and fracture, rendering the cloth useless.")
            else:
                self.items.remove("Cloth")
                self.items.append("Bandage")
                game.fprint("Using some straps of cloth, you sucessfully made a bandage.")
        else:
             game.fprint("You do not have the neecessary item to craft a Bandage.")
    
    def craft_cloth(self):
        if "Tarp" in self.items:
            self.items.remove("Tarp")
            self.items.append("Bandage")
            self.items.append("Bandage")
            game.fprint("Using your knife, you cut the tarp into usable cloth pieces.")
        else:
            game.fprint("You do not have the necessary item to craft Cloth.")

    
    def craft_scrap_axe(self):
        if "Roadsign" and "Metal Pipe" and "Rope" in self.items:
            self.items.remove("Roadsign")
            self.items.remove("Metal Pipe")
            self.items.remove("Rope")
            self.items.append("Scrap Axe")
            game.fprint("Using a piece of rope and a little bit of luck, you manage to create a handle and blade out of metal scrap to use as an axe.")
        else:
            game.fprint("You do not have all the necessary items to craft the Scrap Axe.")
    
    def craft_rope(self):
        if "Cloth" in self.items:
            self.items.remove("Cloth")
            self.items.append("Rope")
            game.fprint("Winding a long piece of rope together around itself, you create a piece of rope.")
        else:
            game.fprint("You do not have the necessary item to craft Rope")

    def craft_makeshift_armor(self):
        if "Ceramic" and "Rope" in self.items:
            self.items.remove("Ceramic")
            self.items.remove("Rope")
            game.fprint("Using a flat piece of ceramic, you attach it to your body via rope, providing a level of regional protection. NOTE- THIS IS WIP. NOT WORKING.")
            self.items.append("Makeshift Armor")
        else:
            game.fprint("You do not have the necessary items to craft Makeshift Body Armor.")







  ## function for drinking
    def drink(self):
        if "Water" in self.items and self.thirst < 100:
            self.items.remove("Water")
            self.thirst = 100
            self.health += random.randint(5,10)
            if self.health > 100:
                self.health = 100
            game.fprint("You drink some warm water, quenching your thirst.")
        elif "Water" not in self.items and self.thirst < 100:
            game.fprint("You do not have any water to drink.")
        elif self.thirst == 100:
            game.fprint("You aren't thirsty.")
        else: game.fprint("Game Error: drink(self) function Error. Reboot.")

   ## 0 health death
    def lose_health(self):
        self.health -= random.randint(1,10)
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            game.die()
    ##0 energy to health loss
    def lose_energy(self):
        self.energy -= random.randint(1,6)
        if self.energy < 0:
            self.energy = 0
        if self.energy == 0:
            self.lose_health
   ## hunger to health loss
    def lose_hunger(self):
        self.hunger -= random.randint(1,6)
        if self.hunger <0:
            self.hunger = 0
        if self.hunger == 0:
            self.lose_health
   ## thirst to health loss
    def lose_thirst(self):
        self.thirst -= random.randint(1,6)
        if self.thirst < 0:
            self.thirst = 0
        if self.thirst == 0:
            self.lose_health()
    ## make a bandage function
    def makeBandage(self):
        if "Cloth" in self.items:
            self.items.remove("Cloth")
            self.items.append("Bandage")
            game.fprint("Using some straps of cloth, you sucessfully made a bandage.")
        else:
            game.fprint("You do not have any cloth to make a bandage.")
   ## scavenge function
    def hello(self):
        print("This is a test.")

    def bag_salvage(self):
        self.items.append("Cloth")
        self.items.append("Food")
        self.items.append("Water")

    def scavenge(self):
        find = random.randint(1,10)
        item_found = random.choice(["Wood", "Water", "Food", "Cloth"])
        if find <= 5:
            game.fprint(f"You found {item_found}!")
            self.items.append(item_found)
        else:
            game.fprint("You couldn't find anything")
    def update_ammo(self):
        total_pistol_ammo = self.items.count("Pistol Bullet")
        total_shotgun_ammo = self.items.count("Shotgun Shell")
        total_rifle_ammo = self.items.count("Rifle Bullet")
        self.pistol_ammo += total_pistol_ammo
        self.shotgun_ammo += total_shotgun_ammo
        self.rifle_ammo += total_rifle_ammo
        while "Pistol Bullet" in self.items:
            self.items.remove("Pistol Bullet")
        while "Shotgun Shell" in self.items:
            self.items.remove("Shotgun Shell")
        while "Rifle Bullet" in self.items:
            self.items.remove("Rifle Bullet")
    def fight(self, enemy, enemy_health, enemy_attack, item_drop, unit, pronoun):
        self.update_ammo()
        time.sleep(2)
        while True:
            if "Rifle" in self.items and self.rifle_ammo > 0:
                rifle_flavor_text = random.randint(1,3)
                if rifle_flavor_text == 1:
                    rifle_flavor_text = "You aim down the sights of your rifle, and let off a shot!"
                elif rifle_flavor_text == 2:
                    rifle_flavor_text = "Your instincts take over, and you let off a powerful shot with your rifle!"
                elif rifle_flavor_text == 3:
                    rifle_flavor_text = "The muzzle of your rifle bursts into a fiery explosion of light, sending a bullet straight towards your enemy!"
                self.attackattack = random.randint(40, 60)
                self.rifle_ammo -=1
                game.fprint(rifle_flavor_text)
            elif "Shotgun" in self.items and self.shotgun_ammo > 0:
                shotgun_flavor_text  = random.randint(1,3)
                if shotgun_flavor_text == 1:
                    shotgun_flavor_text = "As you unload a sheet of buckshot at your enemy, you feel the stock of your shotgun dig into your shoulder."
                elif shotgun_flavor_text == 2:
                    shotgun_flavor_text = "You steadily hold your shotgun, and fire off a shot!"
                elif shotgun_flavor_text == 3:
                    shotgun_flavor_text = "As you fire, the deafening boom from your shotguns makes your ears ring."
                self.attack = random.randint(40, 50)
                self.shotgun_ammo -= 1
                game.fprint(shotgun_flavor_text)
            elif "Pistol" in self.items and self.pistol_ammo > 0:
                pistol_flavor_text = random.randint(1,7)
                if pistol_flavor_text == 1:
                        pistol_flavor_text = "You clench your pistol's grip tightly, and let off a shot!"
                elif pistol_flavor_text == 2:
                    pistol_flavor_text = "You carefully aim down your ironsights, and pull the trigger on your pistol!"
                elif pistol_flavor_text == 3:
                    pistol_flavor_text = "The adrenaline in your body and focused mind give you a clear sight on your target - and you shoot!"
                elif pistol_flavor_text == 4:
                    pistol_flavor_text = "A shot rings out from your pistol!"
                elif pistol_flavor_text == 5:
                    pistol_flavor_text = "A flash escapes from your barrel, sending a bullet towards your enemy!"
                elif pistol_flavor_text == 6:
                    pistol_flavor_text = "You line up the sight picture on your enemy, and let loose a shot!"
                elif pistol_flavor_text == 7:
                    pistol_flavor_text = "Your handgun, heavy in your hand, lets off a deafening shot!"
                self.attack=random.randint(20,40)
                self.pistol_ammo -=1
                game.fprint(pistol_flavor_text)
            elif "Knife" in self.items:
                knife_flavor_text = random.randint(1,3)
                if knife_flavor_text == 1:
                    knife_flavor_text = "Your 6 inches of steel swing through the air!"
                elif knife_flavor_text == 2:
                    knife_flavor_text = "You swing your knife!"
                elif knife_flavor_text == 3:
                    knife_flavor_text = "You catch the glint of your blade as it cuts through the air, right towards its target!"

                self.attack = random.randint(8, 25)

                game.fprint(knife_flavor_text)
            else:
                game.fprint("Realizing you have nothing but your hands to defend yourself with, you hurl a punch!")
                self.attack = random.randint(1,10)
            time.sleep(2)
            enemy_health -= self.attack
            if enemy_health > 0:
                if unit == True:
                    game.fprint(
                        f"You hit the {enemy}! {pronoun} has {enemy_health} health left.", 3
                    )
                else:
                    game.fprint(
                    f"You hit {enemy}! {pronoun} has {enemy_health} health left.", 3)
            if enemy_health <= 0:
                if unit == True:
                    game.fprint(f"You killed the {enemy}", 2)
                else:
                    game.fprint(f"You killed {enemy}", 2)
                find_chance = random.randint(1,10)
                if find_chance <= 3:
                    amount = random.randint(1,100)
                    self.gold += amount
                    game.fprint(f"You found {amount} gold!", 2)
                self.items.append(item_drop)
                game.fprint(f"You found a {item_drop}.", 2)
                return True
            self.health -= enemy_attack
            if self.health <= 0:
                if unit == True:
                    game.fprint(f"The {enemy} kills you...", 3)
                    game.die()                
                else:
                    game.fprint(f"{enemy} kills you...", 3)
                    game.die()
                pass
                    
            if enemy_attack > 0:
                    if unit == True:
                        game.fprint(
                            f"The {enemy} strikes you! You have {self.health} health left.", 3
                        )
                    else: 
                        game.fprint(
                            f"{enemy} strikes you! You have {self.health} left.", 3

                        )





game = Game(1)
player = Player(0, 0, 100, 100, 100, 100, 0, 500, 20, 0, 0, "Null")
##player.items.remove all
player.items.append("Knife")
player.items.append("Pistol")
game.menu()
