films = {
    "Tarzan": {"Age": 14, "Seats": 1},
    "Finding Lucy": {"Age": 10, "Seats": 2},
    "Wandering Samurai": {"Age": 10, "Seats": 2},
}

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        #Check User Age
        age = int(input("How old are you?: ").strip())
        # Check for available seats
        if age >= films[choice]["Age"]:
            num_seats = films[choice]["Seats"]
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice]["Seats"] += -1
            else:
                print("Sorry we're sold out")
        else:
            print("Sorry you're not old enough...")
    else:
        print("Sorry, we dont have that film...")
