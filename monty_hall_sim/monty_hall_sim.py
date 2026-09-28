import random

# Return Door Number with the FATEST BUNNY ON EARTH (Angela's Bunny)
def randomlyPlaceFatBunny(nDoors):
    return random.randint(0, nDoors)

# Return Array With FAT BUNNY or just nothing
def fillDoors(nDoors):
    doors = []
    fatBunnyDoor = randomlyPlaceFatBunny(nDoors - 1)
    for i in range(0, nDoors):
        if i == fatBunnyDoor:
            doors.append("FAT BUNNY")
        else:
            doors.append("Nothing")
    
    return doors

# Ask the user number of doors
def chooseNumberDoors():
    while(True):
        nDoorsText = input("\nHow many doors would you like? (Choose at least 3): ")
        nDoors = int(nDoorsText)
        if nDoors < 3:
            print("Please chose at least 3 doors.")
        else:
            return nDoors

# Ask the user number of iterations
def chooseIterations():
    while True:
        iterationsText = input("\nHow many iterations would you like? (100-1.000.000): ")
        iterations = int(iterationsText)
        if iterations < 100:
            print("Please chose at least 100 iterations.")
        elif iterations > 1000000:
            print("Please chose less than 1.000.000 iterations (For your own good)")
        else:
            return iterations

# Return Other Door with Bunny
def revealDoors(doors, doorSelected, isSim):
    if doors[doorSelected] == "FAT BUNNY":
        switchDoor = random.choice(
            [door for door in range(len(doors)) if door != doorSelected])
    else: 
        switchDoor = doors.index("FAT BUNNY")

    if not isSim:
        for i in range (0, len(doors)):
            if i != switchDoor and i != doorSelected:
                print(f"Door number {i+1} has nothing")

    return switchDoor

# Game of Monty Hall
def montyHallGame():
    print("\nWelcome to the Monty Hall Game!!!")
    print("Choose a door. One door hide the prize.... A FAT BUNNY \nThe others are empty")

    nDoors = chooseNumberDoors()
    
    doors = fillDoors(nDoors)
    doorSelectedText = input(f"\nChoose a door (1-{nDoors}): ")
    doorSelected = int(doorSelectedText) - 1

    print(f"You chose door {doorSelectedText}")
    print("\nMonty opens the other empty doors, leaving one closed door.")
    switchDoor = revealDoors(doors, doorSelected, False)
    selection = input(f"\nWould you like to switch to door {switchDoor+1}? (yes/no): ")

    while (True):
        if selection == "yes" or selection == "y":
            doorSelected = switchDoor
            break
        elif selection == "no" or selection == "n":
            break 
        else:
            print("Please answer yes or no")
        
        
    if doors[doorSelected] == "FAT BUNNY":
        print("\nYou found the FAT BUNNY! You win!")
    else:
        print("\nNo prize this time, no FAT so SAD, You Lose")

# Simulation of Monty Hall
def montyHallSimulation():
    print("\nWelcome to the Monty Hall Simulation")
    print("\nIn this simulation we will prove the probability of the Monty Hall Problem. \
          \nThis simulation will let the users to test with x number of doors and x number \
          \nof iterations.")

    nDoors = chooseNumberDoors()
    nIterations = chooseIterations()

    nWins = 0

    print("\nIterations:")
    for iter in range(0, nIterations):
        doors = fillDoors(nDoors)
        doorSelected = random.randint(0, nDoors-1)
        doorSwitched = revealDoors(doors, doorSelected, True)
        doorPicked = doorSwitched

        if doorPicked == doors.index("FAT BUNNY"):
            nWins+=1
            print(f"Iteration {iter+1}: Switch Won - Switch%: {(nWins/(iter+1))*100}% - Stay%: {((iter+1-nWins)/(iter+1))*100}%")
        else:
            print(f"Iteration {iter+1}: Stay Won - Switch%: {(nWins/(iter+1))*100}% - Stay%: {((iter+1-nWins)/(iter+1))*100}%")

    print("\nFinal Results:")
    print(f"\nExpected Results: Switch%: {((nDoors-1)/nDoors)*100} - Stay%: {(1/nDoors)*100}")
    print(f"Simulation Results: Switch%: {(nWins/nIterations)*100} - Stay%: {((nIterations-nWins)/nIterations)*100}")

        
    

def main():
    print("\nWelcome to the Monty Hall Simulation.")
    print("Choose a simulation mode:")
    print("1. Play the game")
    print("2. Run simulations")
    print("3. Exit")

    simulationMode = 0

    while simulationMode != 3:
        simulationModeText = input("\nEnter 1, 2, or 3: ")
        simulationMode = int(simulationModeText)

        if simulationMode == 1:
            print("\nStarting the game...")
            montyHallGame()

        elif simulationMode == 2:
            print("\nRunning simulations...")
            montyHallSimulation()

        elif simulationMode == 3:
            print("\nExiting the program. Goodbye!")
            exit()

        else:
            print("\nInvalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()