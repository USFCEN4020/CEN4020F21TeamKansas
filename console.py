import time
import manage as m
import utility
import csv

FILENAME_STUDENT = "student_data.csv"
FILENAME_SETTINGS = "settings.csv"
FILENAME_PROFILE = "profiles.csv"
FILENAME_FRIEND = "friends.csv"
FILENAME_FRIEND = "requests.csv"
blank_string = " "

# The screen is at the begin of the program, or after its options finish (log-in, sign up)
def Welcome_Page():
    print("\nWelcome to InCollege! An application designed for college students hoping to connect with other college students in effort to land a job!")
    print("")
    print("Are you a new user? Or do you already have an account? Select an option below")
    print("1. Create an account")
    print("2. Login to an existing account")
    print("3. Connect with someone you know")
    print("4. Play the video")
    print("5. Useful Links")
    print("6. InCollege Important Links")
    print("7. Exit inCollege")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-7
    decision = utility.checkUserInput(decision, 1, 7)

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
        UsefulLinks_Page(0, blank_string)
    elif (decision == "6"):
        ImportantLinks_Page(0, blank_string)
    elif (decision == "7"):
        return


def Login_Page(name):
    print()
    print("\nSelect one of the below options:")
    print("1. Create Profile")
    print("2. View Profile")
    print("3. Search for job/internship")
    print("4. Post a Job")
    print("5. Learn a New Skill")
    print("6. Useful Links")
    print("7. inCollege Important Links")
    print("8. Log Out")
    decision = input("\nYour selection: ")

    # Used for input validation. User should only choose a value 1-8
    decision = utility.checkUserInput(decision, 1, 8)

    if (decision == "1"):
        manage = m.Manage()
        manage.create_profile(name)
        decision = input("\n1. Return to previous screen. ")
        decision = utility.checkUserInput(decision, 1, 1)
        Login_Page(name)
    elif (decision == "2"):
        manage = m.Manage()
        manage.view_profile(name)
        decision = input("\n1. Return to previous screen. ")
        decision = utility.checkUserInput(decision, 1, 1)
        Login_Page(name)
    elif (decision == "3"):
        print("\nUnder construction for now")
        Login_Page(name)
    elif (decision == "4"):
        manage = m.Manage()
        manage.new_job(name)
        Login_Page(name)
    elif (decision == "5"):
        LearnSkill_Page(name)
    elif (decision == "6"):
        UsefulLinks_Page(1, name)
    elif (decision == "7"):
        ImportantLinks_Page(1, name)
    elif (decision == "8"):
        Welcome_Page()


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

def ImportantLinks_Page(value, name):
    print("\nInCollege Important Links. Select one of the below options:")
    print("1. A Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Go Back to Previous Screen")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-9
    decision = utility.checkUserInput(decision, 1, 9)

    if (decision == "1"):
        print("\nA Copyright Notice: Copyright © 2021 by Team Kansas. All rights reserved.")
        ImportantLinks_Page(value, name)
    elif (decision == "2"):
        print("\nAbout inCollege: inCollege is the best application designed for college students hoping to connect with other college students in effort to land a job!")
        ImportantLinks_Page(value, name)
    elif (decision == "3"):
        print("\nAccessibility: We are committed to making accessibility a core consideration from the every stage and update of inCollege.")
        ImportantLinks_Page(value, name)
    elif (decision == "4"):
        print("\nUser Agreement: With agreement to registerign an account and signing in, the user complies with terms and conditions for inCollege.")
        ImportantLinks_Page(value, name)
    elif (decision == "5"):
        print("\nOur privacy policy explains how we treat your personal data and protect your privacy when you use our Services. By using our Services, you agree that inCollege can use such data in accordance with our privacy policy.")
        PrivacyPolicy_Page(value, name)
    elif (decision == "6"):
        print("\nCookie Policy: Chocolate Chip Cookies or Rainbow Sprinkle Cookies?")
        ImportantLinks_Page(value, name)
    elif (decision == "7"):
        print("\nCopyright Policy: We own all things inCollege.")
        ImportantLinks_Page(value, name)
    elif (decision == "8"):
        print("\nBrand Policy: This policy governs the use of all inCollege trademarks (see definition) for any purpose. Consistency in the use of inCollege trademarks strengthens their value and our ability to protect them from unauthorized use. The inCollege should be consulted whenever it is not clear whether a proposed use is permissible.")
        ImportantLinks_Page(value, name)
    elif (decision == "9"):
        if value == 0:
            Welcome_Page()
        elif value == 1:
            Login_Page(name)


def PrivacyPolicy_Page(value, name):

    if value == 0:
        print("\nSign in for Guest Controls and Language Features")
        print("1. Go back to InCollege Important links")
        decision = input("Your selection: ")

        # check the right value of input from user
        decision = utility.checkUserInput(decision, 1, 1)

        if (decision  == "1"):
            ImportantLinks_Page(value, name)

    # A Signed in user will get the option to access guest controls and Language
    elif value == 1:
        print()
        print("\nPrivacy Policy - Select one of the below options:")
        print("1. Guest Controls")
        print("2. Language")
        print("3. Go back to InCollege Important Links")
        decision = input("Your selection: ")

        # Used for input validation. User should only choose a value 1-3
        decision = utility.checkUserInput(decision, 1, 3)

        if (decision  == "1"):
            GuestControls_Page(value, name)
        elif (decision  == "2"):
            Language_Page(value, name)
        elif (decision  == "3"):
            ImportantLinks_Page(value, name)

def GuestControls_Page(value, name):

    toggle = [" ", " ", " ", " ", " "]
    lines = list()
    empty = []
    count = 0

    # Reads current language setting and then populates empty list called lines with info
    with open(FILENAME_SETTINGS, 'r') as readFile:
        reader = csv.reader(readFile)
        for item in reader:
            # used to fix spacing
            if item != empty:
                lines.append(item)
                count = count + 1
            for space in item:
                if (space == name):
                    toggle = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                    lines.pop()
                    count = count - 1

    print("\nEmail Feature is currently", toggle[1])
    print("SMS Feature is currently", toggle[2])
    print("Targeted Advertising Feature is currently", toggle[3])

    print("\nSelect one of the below options:")
    print("1. Toggle ON/OFF Email Feature")
    print("2. Toggle ON/OFF SMS Feature")
    print("3. Toggle ON/OFF Targeted Advertising Feature")
    print("4. Go back to Privacy Policy")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-4
    decision = utility.checkUserInput(decision, 1, 4)

    if (decision == "1"):
        if (toggle[1] == "ON"):
            toggle[1] = "OFF"
        else:
            toggle[1] = "ON"
        lines.append(toggle)

        # overwrite
        with open(FILENAME_SETTINGS, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        GuestControls_Page(value, name)

    elif (decision == "2"):
        if (toggle[2] == "ON"):
            toggle[2] = "OFF"
        else:
            toggle[2] = "ON"
        lines.append(toggle)
        #overwrite
        with open(FILENAME_SETTINGS, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        GuestControls_Page(value, name)
    elif (decision == "3"):
        if (toggle[3] == "ON"):
            toggle[3] = "OFF"
        else:
            toggle[3] = "ON"
        lines.append(toggle)

        # overwrite
        with open(FILENAME_SETTINGS, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        GuestControls_Page(value, name)
    elif (decision == "4"):
        PrivacyPolicy_Page(value, name)


# Name is username of the user so each user has their own settings
def Language_Page(value, name):

    #helper variables
    lines = list()
    toggle = [" ", " ", " ", " ", " "]
    blank = []
    count = 0

    #read current language setting and fill 'lines' with info
    with open(FILENAME_SETTINGS, 'r') as readFile:
        reader = csv.reader(readFile)
        for item in reader:
            if item != blank: # or else there will be stupid amount of white space
                lines.append(item)
                count = count + 1
            for field in item:
                if (field == name):
                    toggle = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                    lines.pop()
                    count = count - 1

    print()
    print("Your Language is currently set to", toggle[4])
    print("Select one of the below options:")
    print("1. Set to your language to English")
    print("2. Set to your language to Spanish")
    print("3. Go back to Privacy Policy")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-4
    decision = utility.checkUserInput(decision, 1, 3)

    if (decision == "1"):
        toggle[4] = "English"
        lines.append(toggle)

        #overwrite
        with open(FILENAME_SETTINGS, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        Language_Page(value, name)

    elif (decision == "2"):
        toggle [4] = "Spanish"
        lines.append(toggle)
        #overwrite
        with open(FILENAME_SETTINGS, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        Language_Page(value, name)

    elif (decision == "3"):
        lines.append(toggle)

        # Adds toggle to list
        # overwrite
        with open(FILENAME_SETTINGS, 'w') as writeFile:
            writer = csv.writer(writeFile)
            for row in lines:
                writer.writerow(row)
        PrivacyPolicy_Page(value, name)


def UsefulLinks_Page(value, name):
    print("\nSelect one of the below options:")
    print("(1) General")
    print("(2) Browse InCollege")
    print("(3) Business solutions")
    print("(4) Directories")
    print("(5) Go back to previous screen")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-4
    decision = utility.checkUserInput(decision, 1, 5)

    if (decision == "1"):
        GeneralLinks_Page(value,name)
    elif (decision == "2"):
        print("\nUnder construction")
        UsefulLinks_Page(value, name)
    elif (decision == "3"):
        print("\nUnder construction")
        UsefulLinks_Page(value, name)
    elif (decision == "4"):
        print("\nUnder construction")
        UsefulLinks_Page(value,name)
    elif (decision == "5"):
        if value == 0:
            Welcome_Page()
        elif value == 1:
            Login_Page(name)


def GeneralLinks_Page(value, name):
    print()
    print("Select one of the below options:")
    print("1. Sign up")
    print("2. Help Center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("8. Back to Useful Links")

    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-4
    decision = utility.checkUserInput(decision, 1, 8)

    if (decision == "1"):
        Register_Page()
    elif (decision == "2"):
        print("\nWe're here to help!")
        GeneralLinks_Page(value, name)
    elif (decision == "3"):
        print("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide.")
        GeneralLinks_Page(value, name)
    elif (decision == "4"):
        print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports." )
        GeneralLinks_Page(value, name)
    elif (decision == "5"):
        print("\nUnder construction")
        GeneralLinks_Page(value, name)
    elif (decision == "6"):
        print("\nUnder construction")
        GeneralLinks_Page(value, name)
    elif (decision == "7"):
        print("\nUnder construction")
        GeneralLinks_Page(value, name)
    elif (decision == "8"):
        UsefulLinks_Page(value, name)


def search_friend(name):
    manage = m.Manage()
    sent = 0
    choice = 0

    while sent == 0:
        results = list()
        entry = [" ", " ", " ", " ", " "]
        print("Select one of the options to search for friend")
        print("1. Search by last name")
        print("2. Search by University")
        print("3. Search by Major")
        print("4. Return to previous page")
        choice = input("Your selection: ")

        # check user input
        choice = utility.checkUserInput(choice, 1, 7)

        if choice == "1":
            last = input("Enter last name: ")
            name = list()
            name = manage.return_name_last(last)