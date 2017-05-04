# Import the time module
import time

# Game intro and instructions
print("  _______                                _       _     _ \n |__   __|                              | |     | |   (_)\n    | | __ _ _ __ ___   __ _  __ _  ___ | |_ ___| |__  _ \n    | |/ _` | '_ ` _ \ / _` |/ _` |/ _ \| __/ __| '_ \| |\n    | | (_| | | | | | | (_| | (_| | (_) | || (__| | | | |\n    |_|\__,_|_| |_| |_|\__,_|\__, |\___/ \__\___|_| |_|_|\n                              __/ |                      \n                             |___/                       ")
time.sleep(3)
print("Welcome to Tamagotchi simulator! The instructions below explain how the game works:\n")
time.sleep(2)
print("1. Your Tamagotchi has 100% health and 0% hunger to start with. Hunger level will go up by 10% each turn\n")
time.sleep(2)
print("2. When your Tamagotchi's hunger level reaches 80%, they will begin to lose 5% health per turn, until the hunger level drops below 80% again\n")
time.sleep(2)
print("3. Every turn, you can choose to feed your Tamagotchi, or to wait another turn. Feeding drops your Tamagotchi's hunger level by a certain amount, depending on what you fed them\n")
time.sleep(2)
print("4. You have a certain amount of stock in your inventory. Go to the shop to buy more!\n")
time.sleep(2)
print("5. As your Tamagotchi levels up, their maximum health will go up, as will their skill\n")
time.sleep(2)
print("6. If your Tamagotchi's health reaches 0%, it will die and it's game over!\n")
time.sleep(2)
print("7. Your Tamagotchi's health cannot go above 100%, nor can its hunger go below 0%\n")
time.sleep(2)
print("Enjoy the simulator! Press A to start!")
start = input().lower()

# Creature stats stored in a dictionary
creature = {
    "level": 1,
    "exp": 0,
    "health": 100,
    "hunger": 0,
    "sleep": 0,
    "skill": 0,
    "tired": False,
    "sick": False,
    "tricks": {
        "jump_hoop": ["jumped the hoop", 10],
        "roll_over": ["rolled over", 4],
        "high_five": ["gave you a high five", 12],
        "two_legged_walk": ["walked on two legs", 16],
        "front_flip": ["did a front flip", 23]
    }
}

# Food hunger restoration values stored in a dictionary
food = {
    "Chew Stix": 5,
    "Tem Flakes": 10,
    "Leftover Chicken": 12,
    "Swiss Cheese": 9,
    "Tama-Corp DLux Bytes": 22
}

# The items in the current inventory
inventory = {
    "Chew Stix": 5,
    "Tem Flakes": 5,
    "Leftover Chicken": 5,
    "Swiss Cheese": 5,
    "Tama-Corp DLux Bytes": 5,
    "money": 100
}

# The price of shop items
shop = {
    "Chew Stix": 5,
    "Tem Flakes": 10,
    "Leftover Chicken": 12,
    "Swiss Cheese": 9,
    "Tama-Corp DLux Bytes": 22
}

# Competing in a competition
def compete():
    print("You entered into a Tamagotchi competition!")
    time.sleep(2)
    print("Your Tamagotchi has " + str(len(creature["tricks"])) + " tricks:")
    for key in creature["tricks"]:
        print(key + ": worth %s points" % (creature["tricks"[key]]))
    time.sleep(2)
    print("Enter the name of the trick you'd like to do, as shown above:")
    trick = input()

# Do a trick in the competition
def pull_trick(_trick):
    print("Your Tamagotchi " + creature["tricks"[_trick[0]]] + "!")
    print("Your score went up by " + str(creature["tricks"[_trick[1]]]) + "!")


# Feed function
def feed():
    print("What would you like to feed your Tamagotchi?")
    time.sleep(1)
    # Print out the feeding options that the player has
    print("You have " + str(len(food)) + " options:")
    for key in food:
        print(key + ": restores %s hunger" % (food[key]))
    eat = input("(stix/flakes/chicken/cheese/bytes)")
    # Decrease the creature's hunger by a certain amount, depending on what food they chose
    if eat == "stix":
        print("You fed your Tamagotchi Chew Stix!")
        creature["hunger"] -= food["Chew Stix"]
    elif eat == "flakes":
        print("You fed your Tamagotchi Tem Flakes!")
        creature["hunger"] -= food["Tem Flakes"]
    elif eat == "chicken":
        print("You fed your Tamagotchi Leftover Chicken!")
        creature["hunger"] -= food["Leftover Chicken"]
    elif eat == "cheese":
        print("You fed your Tamagotchi Swiss Cheese!")
        creature["hunger"] -= food["Swiss Cheese"]
    elif eat == "bytes":
        print("You fed your Tamagotchi Tama-Corp DLux Bytes!")
        creature["hunger"] -= food["Tama-Corp DLux Bytes"]
    else:
        pass

    # The creature's hunger cannot drop below 0%, so if it is negative, reset it to 0
    if creature["hunger"] < 0:
        creature["hunger"] = 0
    else:
        pass
    time.sleep(3)
    # Tell the player the new hunger of their Tamagotchi
    print("Your Tamagotchi's hunger is now: " + str(creature["hunger"]))
    time.sleep(3)


def play():
    # Game over if your creature's health reaches zero
    while creature["health"] > 0:
        # Creature's hunger goes up by 10% each turn
        creature["hunger"] += 10
        # If your creature's hunger reaches 100%...
        if creature["hunger"] >= 100:
            # ...they lose 20% health each turn until their hunger level drops below 80% again
            creature["health"] -= 20
        # If they have 90% hunger...
        elif creature["hunger"] >= 90:
            # Deplete 15% health
            creature["health"] -= 15
        # If they have 80% hunger...
        elif creature["hunger"] >= 80:
            # Deplete 10% health
            creature["health"] -= 10
        else:
            # If the hunger level is 79% or below, nothing happens
            pass

        # Give the player a choice of what they want to do with their creature
        print("Do you want to feed your Tamagotchi or wait another turn? (feed/wait)")
        choice = input()
        if choice == "feed":
            # If they choose to feed, run the feed() function
            feed()
        elif choice == "wait":
            # Else, just do nothing
            pass
        else:
            # If the player enters and invalid choice, alert them and allow them to enter a new choice
            print("Invalid choice - choose to either 'feed' your Tamagotchi or 'wait' another turn...")

        # Print the creature's current health and hunger level to the console
        print("Your Tamagotchi's current health is: " + str(creature["health"]) + ", and their hunger level is: " + str(creature["hunger"]))
        time.sleep(3)

play()

# If the creature's health drops below 1%, they die and the game is over
print("Your creature's health ran out and they died!")
time.sleep(3)
print("\n")
print("Would you like to try again with a new egg? (y/n)")
replay = input()
# Start a new game if the player wants to
if replay == "y":
    play()
else:
    pass
