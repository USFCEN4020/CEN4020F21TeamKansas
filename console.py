import time
import manage as m
import utility

# The screen is at the begin of the program, or after its options finish (log-in, sign up)
def Welcome_Page():
    print("\nWelcome to InCollege! An application designed for college students hoping to connect with other college students in effort to land a job!")
    print("")
    print("Are you a new user? Or do you already have an account? Select an option below")
    print("1. Create an account")  # log-in
    print("2. Login to an existing account")  # sign up
    print("3. Connect with someone you know")
    print("4. Play the video")
    print("5. Exit inCollege")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-5
    decision = utility.checkUserInput(decision, 1, 5)

    if (decision == "1"):
        Register_Page()
    elif (decision == "2"):
        manage = m.Manage()  # create a new object Manage
        name = manage.login()  # get user's name after logging in successful
        Login_Page(name)
    elif (decision == "3"):
        ConnectWithPeople_Page()
    elif (decision == "4"):
        print("\nVideo is now playing in 3 seconds!")
        time.sleep(3)
        Welcome_Page()
    elif (decision == "5"):
        return


def Login_Page(name):
    print()
    print("\nSelect one of the below options:")
    print("1. Search for job/internship")
    print("2. Post a Job")
    print("3. Learn a New Skill")
    print("4. Log Out")
    print("5. Exit Program")
    decision = input("\nYour selection: ")

    # Used for input validation. User should only choose a value 1-5
    decision = utility.checkUserInput(decision, 1, 5)

    if (decision == "1"):
        print("\nUnder construction for now")
        Login_Page(name)
    elif (decision == "2"):
        manage = m.Manage()
        manage.new_job(name)
        Login_Page(name)
    elif (decision == "3"):
        LearnSkill_Page(name)
    elif (decision == "4"):
        Welcome_Page()
    elif (decision == "5"):
        return


# Displays 5 skills that the user can learn (all of which return "under construction"). The user is also allowed to not choose a skill, which will bring the user back to the welcome screen by calling welcomeScreen.
def LearnSkill_Page(name):
    print()
    print("\nSelect one of the below options:")
    print("1. Learn C")
    print("2. Learn Java")
    print("3. Learn Python")
    print("4. Learn SQL")
    print("5. Learn C++")
    print("6. Return to Menu")
    decision = input("\nYour selection: ")

    # Used for input validation. User should only choose a value 1-6
    decision = utility.checkUserInput(decision, 1, 6)

    if (decision == "1"):
        print("\nUnder construction for now")
        LearnSkill_Page(name)
    elif (decision == "2"):
        print("\nUnder construction for now")
        LearnSkill_Page(name)
    elif (decision == "3"):
        print("\nUnder construction for now")
        LearnSkill_Page(name)
    elif (decision == "4"):
        print("\nUnder construction for now")
        LearnSkill_Page(name)
    elif (decision == "5"):
        print("\nUnder construction for now")
        LearnSkill_Page(name)
    elif (decision == "6"):
        Login_Page(name)


def Register_Page():
    manage = m.Manage()
    name = manage.register()
    if name != None:  # sign up successfully
        Login_Page(name)
    else:
        print()
        print("Select one of the below options:")
        print("1. Create a New Account. ")
        print("2. Go Back to Home Screen.")
        decision = input("\nYour selection: ")

        # Used for input validation. User should only choose a value 1-2
        choice = utility.checkUserInput(decision, 1, 2)
        if (decision == "1"):
            Register_Page()
        elif (decision == "2"):
            Welcome_Page()


def ConnectWithPeople_Page():
    manage = m.Manage()
    firstname = input("Enter friend's first name: ")
    lastname = input("Enter friend's last name: ")
    manage.find_people(firstname, lastname)
    print("\nSelect one of the below options:")
    print("1. Login")
    print("2. Create a New Account.")
    print("3. Go Back to Home Screen.")
    decision = input("\nYour selection: ")

    # Used for input validation. User should only choose a value 1-3
    decision = utility.checkUserInput(decision, 1, 3)

    if (decision == "1"):
        manage = m.Manage()
        name = manage.login()

        if name == None:
            Welcome_Page()
        else:  # log in successfully
            Login_Page(name)

    elif (decision == "2"):
        Register_Page()
    elif (decision == "3"):
        Welcome_Page()
