known_users = ["Musa", "Amrah", "Sadiq","Yusuf", "Paul", "Andrew", "Salamatu", "Peter"]
while True:
    print("Hello, Welcome to the Travis Security System")
    name = input("What is your name: ").strip().capitalize()
    if name in known_users:
        print(f"Hello {name}, You are recognized, Welcome back!")
        index = input("Do you want to be removed? (y/n)? ").strip().lower
        if index == "y" or "Y":
            known_users.remove(name)
        elif index == "n" or "N":
            print("That's fine, I didn't want you to go anyway")
    else:
        print(f"Hey! {name} You are not recognized by the system")
        add_me = input("Would you like to be added to the database (y/n)? ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No problem, I'll see you arround")
        else:
            print("Invalid Input Try again")