<<<<<<< HEAD
import time
import csv
from csv import writer
import os.path
from student import Student
from job import Job
import manage as m
import main

studentList = []  # student list used to add student object attributes and insert into file
file_exists = os.path.exists('student_data.csv')
if not file_exists:
    file = open('student_data.csv', 'w')
file = open("student_data.csv")
reader = csv.reader(file)
lines = len(list(reader))

def max_accts():
    # this makes sure we only support five accounts for first epic
    csv_file = csv.reader(open("student_data.csv", "r"), delimiter=",")
    if lines >= 5:
        # if called, means no more accounts can be created1
        print("All permitted accounts have been created, please come back later")
        return True


def append_list_as_row(file_name, list_of_elem):
    # function that adds to file
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

print()

def welcome():

    print("Welcome to InCollege! An application designed for college students hoping to connect with other college students in effort to land a job!")
    print("")
    print("Are you a new user? Or do you already have an account? Select an option below")
    decision = input("1. Create an account\n"
    "2. Login\n"
    "3. Find someone you know \n"
    "4. Play the video \n"
    "0. Exit\nYour selection: ")

    if decision == "1":
        register() #takes you to register screen
    elif decision == "2":
        #call the login method in Manage class
        manage = m.Manage()
        username_key = manage.login() #takes you to login screen
        #if username is empty try again
        if username_key == None:
            welcome(decision)
        else:
            job_menu(username_key)

    #find someone
    elif decision == "3":
        find_someone() #find someone function

    #watch video
    elif decision == "4":
        print("\nVideo is now playing in 3 seconds!")
        time.sleep(3)

        main.main()
    
    #exit
    elif decision == "0":
        print("\nBye!!!")
        exit()

    else:
        print("Invalid option, please try again")
        decision = input("1. Create an account\n2. Login\n3. Find someone you know \n4. Play the video \nYour selection: ")
        welcome(decision)

#menu_job
def job_menu(username_key):
    print("1. Search for job/internship")
    print("2. Post a job")
    print("3. Learn a new skill")
    print("4. Log out")
    print("5. Exit program")
    choice = input("Your selection: ")

    if (choice == "1"):
        print("Under construction for now"
              " returning to menu")

        job_menu(username_key)
    elif (choice == "2"):       
        job_manage = m.Manage()
        job_manage.post_new_job(username_key)

        job_menu(username_key)
    elif(choice == "3"):
        menu_learnskill()
    elif(choice == "4"):
        main()
    elif(choice == "5"):
        exit()


# this is after find_someone runs and is able to find somone 
#prompts the user to register/login since their friend has an account
def join_Incollege():
    print("Select one of the options below: ")
    print("1. Log in")
    print("2. Sign up")
    print("3. Return to homescreen")
    decision = input("Your selection: ")
    
    if(decision == "1"):
        manage = m.Manage()
        #takes you to login screen
        username_key = manage.login()
        #if username is empty try again
        if username_key == None:
            welcome(decision)
        else:
            job_menu(username_key)

    elif(decision == "2"):
        register()
    elif(decision == "3"):
        main.main()


def checkPass(password):
    # minimum 8 character
    if len(password) < 8:
        return False

    # max 12 characters
    if len(password) > 12:
        return False

    # Has an uppercase
    if not any(character.isupper() for character in password):
        return False

    # at least one digit
    if not any(character.isdigit() for character in password):
        return False

    # at least one non_alpha
    if password.isalnum():
        return False

    return True


def checkUsername(username):
    # ensures unique username when creating account
    csv_file = csv.reader(open("student_data.csv", "r"), delimiter=",")
    # loop through the csv list
    for line in csv_file:
        if username in line:
            return False
    return True

def menu_learnskill(): #we can change the skills, these are just what came to mind
    print("")
    print("1. Learn C")
    print("2. Learn Java")
    print("3. Learn Python")
    print("4. Learn SQL")
    print("5. Learn C++")
    print("6. Return to menu")
    choice = input("Your selection: ")

    if (choice == "1"):
        print()
        print("Under construction for now"
              " returning to menu")
        menu_learnskill() # this will change
    elif(choice == "2"):
        print()
        print("Under construction for now"
              " returning to menu")
        menu_learnskill() # this will change
    elif(choice == "3"):
        print()
        print("Under construction for now"
              " returning to menu")
        menu_learnskill() # this will change
    elif(choice == "4"):
        print()
        print("Under construction for now"
              " returning to menu")
        menu_learnskill() # this will change
    elif(choice == "5"):
        print()
        print("Under construction for now"
              " returning to menu")
        menu_learnskill() # this will change
    elif(choice == "6"):
        job_menu()


def register():

    # Checks if the max accounts have been reached
    maxAccountFlag = max_accts()
    if maxAccountFlag:
        quit()

    # take input
    username = input("Enter username: ")
    password = input("Enter your password: ")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")

    # this is capitalizing the first letter of first and last name
    a_string = firstname 
    firstname = a_string.title()
    a_string = lastname
    lastname = a_string.title()

    # This block checks password
    flag = checkPass(password)
    while not flag:
        print("Invalid password. Password must be between 8-12 characters"
              " and contain one uppercase letter, one digit, and one non-alpha character")
        password = input("Enter your password: ")
        flag = checkPass(password)

    # This block checks for unique username
    flag = checkUsername(username)
    while not flag:
        print("Username already exists. Please try again")
        username = input("Enter username: ")
        flag = checkUsername(username)

    # If they make it here, everything is good so we can create student object and add them to list and insert into file
    student = Student(username, password, firstname, lastname)
    studentList.extend([student.user_name, student.password, student.first, student.last])
    append_list_as_row('student_data.csv', studentList)
    print("Account successfully created, come back next time and login!")


def find_someone():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    #capitalizing first letter of first and last name
    #this is needed because if they write the persons name in lowercase
    #it will say the name is not there
    a_string = firstname
    firstname = a_string.title()
    a_string = lastname
    lastname = a_string.title()

    flag = findFirstName(firstname)
    flag2 = findLastName(lastname)
    # both username and password have to exist in file to reach successful login
    if not flag and not flag2:
        print("They are not yet a part of the InCollege system yet")
        decision = input("Press 1 to go back to the menu: ")
        back_to_menu(decision)
    print("They are a part of the InCollege system")
    print("Join them!")
    print()
    join_Incollege()


def back_to_menu(decision): #gives user a chance to go back to menu at any point
    if decision == '1':
        welcome()
    while decision != '1':
        decision = input("Invalid input, please press 1 to go back to menu: ")
    welcome()
        

def findFirstName(firstname):
    # searches file for username for login
    csv_file = csv.reader(open("student_data.csv", "r"), delimiter=",")
    # loop through the csv list
    for line in csv_file:
        if firstname in line:
            return True
    return False


def findLastName(lastname):
    #fdsfsdfsdf
    # searches file for username for login
    csv_file = csv.reader(open("student_data.csv", "r"), delimiter=",")
    # loop through the csv list
    for line in csv_file:
        if lastname in line:
            return True
    return False
=======
import time
import manage as m
import utility
import csv
import friend

FILENAME_STUDENT = "student_data.csv"
FILENAME_APP = "applications.csv"
FILENAME_SETTINGS = "settings.csv"
FILENAME_PROFILE = "profiles.csv"
FILENAME_JOB = "job_data.csv"
FILENAME_FRIEND = "friends.csv"
FILENAME_REQUEST = "requests.csv"
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
        exit()


def Login_Page(name):
    friend.check_requests(name)
    print()
    print("\nSelect one of the below options:")
    print("1. Create Profile")
    print("2. View Profile")
    print("3. Search for job/internship")
    print("4. Post a Job")
    print("5. Delete a Job")
    print("6. Search a Job")
    print("7. Learn a New Skill")
    print("8. Useful Links")
    print("9. inCollege Important Links")
    print("10. Connect with Friends")
    print("11. My Connections")
    print("12. Log Out")
    decision = input("\nYour selection: ")

    # Used for input validation. User should only choose a value 1-11
    decision = utility.checkUserInput(decision, 1, 11)

    if decision == "1":
        manage = m.Manage()
        manage.create_profile(name)
        decision = input("\n1. Return to previous screen. ")
        decision = utility.checkUserInput(decision, 1, 1)
        Login_Page(name)
    elif decision == "2":
        manage = m.Manage()
        manage.view_profile(name)
        decision = input("\n1. Return to previous screen. ")
        decision = utility.checkUserInput(decision, 1, 1)
        Login_Page(name)
    elif decision == "3":
        job_Screen(name)
    elif decision == "4":
        manage = m.Manage()
        manage.new_job(name)
        Login_Page(name)
    elif decision == "5":
        manage = m.Manage()
        JobTL = []  # keep the titles of jobs that the user posted
        for ele in manage.get_list_job():
            if ele.get_poster_name() == name:
                JobTL.append(ele.get_title())

        if len(JobTL) != 0:
            print("\nHere is all the Jobs that have been posted by you: ")
            count = 0
            for ele in JobTL:
                count += 1
                print(str(count) + ": " + ele)

            for ele in JobTL:
                print()
                print("Would you like to eliminate job with title: " + "\"" + ele + "\"")
                print("1. Yes, 2 No")
                secDecision = input("Input: ")
                # check the right value of input from user
                secDecision = utility.checkUserInput(secDecision, 1, 2)
                if secDecision == "1":
                    manage.delete_job(name, ele)
                    Login_Page(name)
                else:
                    pass
        else:
            print("\nYou have not posted any jobs so far")
            Login_Page(name)
    elif decision == "6":
        job_Screen(name)
    elif decision == "7":
        LearnSkill_Page(name)
    elif decision == "8":
        UsefulLinks_Page(1, name)
    elif decision == "9":
        ImportantLinks_Page(1, name)
    elif decision == "10":
        friend.search_friend(name)
    elif decision == "11":
        friend.show_connection(name)
    elif decision == "12":
        Welcome_Page()


# Displays 5 skills that the user can learn
# (all of which return "under construction").
# The user is also allowed to not choose a skill,
# which will bring the user back to the welcome screen
# by calling welcomeScreen.
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
        decision = utility.checkUserInput(decision, 1, 2)
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

def job_Screen(name):
    decision = 0
    while(decision != 5):
        print("Welcome to the Job Screen please enter your selection on the menu below")
        print("1. View all jobs")
        print("2. View jobs that you have applied to")
        print("3. View jobs that you have not applied to")
        print("4. View your saved jobs")
        print("5. Return to Log In Screen")
        decision = input("Input: ")
        if (decision == "1"):  # search all jobs
            manage = m.Manage()
            j = list()
            print("Here are the current jobs in the system:")
            with open(FILENAME_JOB, "r") as f:
                JobR = csv.reader(f)
                i = 0
                for row in JobR:
                    if row != [] and row != ["Title", "Description", "Employer", "Location", "Salary", "Post_Name"]:
                        i = i + 1
                        j.append(row)
                        JobA = 0
                        with open(FILENAME_APP, "r") as f2:
                            ApplicR = csv.reader(f2)
                            for entry in ApplicR:
                                if entry != []:
                                    if (entry[0] == name) and (entry[1] == row[0]) and (entry[2] == row[2]):
                                        JobA = JobA + 1
                        if JobA > 0:
                            print(str(i) + ": " + row[0] + " (Applied)")
                        else:
                            print(str(i) + ": " + row[0])
                JobN = len(j)
            secDecision = JobN + 1
            thirdDecision = 0
            while (secDecision != "0"):
                print("Enter the job number that you wish to view (and if you wish, save or apply to) or press 0 to return")
                secDecision = input("Input: ")
                # check that acceptable input was provided by the user
                secDecision = utility.checkUserInput(secDecision, 0, JobN)

                if (secDecision != "0"):
                    print(j[int(secDecision) - 1][0])
                    print("Employer: " + j[int(secDecision) - 1][2])
                    print("Location: " + j[int(secDecision) - 1][3])
                    print("Pay: " + j[int(secDecision) - 1][4])
                    print("About: " + j[int(secDecision) - 1][1])
                    print()
                    print("1. Apply, 2. Save 3. Return to menu")
                    thirdDecision = input("Input: ")
                    thirdDecision = utility.checkUserInput(thirdDecision, 1, 3)
                    if (thirdDecision == "1"):  # Application
                        JobA = 0
                        with open(FILENAME_APP, "r") as f:
                            ApplicR = csv.reader(f)
                            for entry in ApplicR:
                                if entry != []:
                                    if (entry[0] == name) and (entry[1] == j[int(secDecision) - 1][0]) and (
                                        entry[2] == j[int(secDecision) - 1][2]):
                                        JobA = JobA + 1
                        if JobA > 0:
                            print("You have already applications to that job")
                        else:
                            manage.add_application(name, j[int(secDecision) - 1][0], j[int(secDecision) - 1][2])
                    elif (thirdDecision == "2"):  # Save
                        manage.add_save_job(name, j[int(secDecision) - 1][0])

        # View jobs JobA to
        elif (decision == "2"):
            print("Here are the jobs you have applied to:")
            with open(FILENAME_APP, "r") as f:
                JobR = csv.reader(f)
                i = 0
                for row in JobR:
                    if row != [] and row[0] == name:
                        print(row[1] + " at " + row[2])


        elif (decision == "3"):
            ApplicL = []  # keep title of applications of the user
            with open(FILENAME_APP, "r") as f:
                JobR = csv.reader(f)
                for row in JobR:
                    if row != [] and row[0] == name:
                        ApplicL.append(row[1])

            JobL = []  # keep title of job in the system.
            with open(FILENAME_JOB, "r") as f2:
                JobR = csv.reader(f2)
                for row in JobR:
                    if row != [] and row != ["Title", "Description", "Employer", "Location", "Salary", "Post_Name"]:
                        JobL.append(row[0])

            count = 0
            for element in JobL:
                if element not in ApplicL:
                    count += 1
                    print(str(count) + ": " + element)

        # View saved jobs
        elif (decision == "4"):
            manage = m.Manage()
            JobSL = manage.list_save_job(name)
            if len(JobSL) != 0:
                count = 0
                for element in JobSL:
                    count += 1
                    print(str(count) + ": " + element)
            else:
                print("You have no saved jobs!")

            if len(JobSL) != 0:

                print("Would you like to unsave any jobs?")
                print("1. Unsave, 2.Keep")
                secDecision = input("Input: ")
                # check the right value of input from user
                secDecision = utility.checkUserInput(secDecision, 1, 2)

                if (secDecision == "1"):
                    for element in JobSL:
                        print()
                        print("Do you want to delete job: " + "\"" + element + "\"")
                        print("1. Yes 2. No")
                        secDecision = input("Input: ")
                        # check the right value of input from user
                        secDecision = utility.checkUserInput(secDecision, 1, 2)
                        if (secDecision == "1"):
                            manage.delete_save_job(name, element)
                        else:
                            pass

                elif (secDecision == "2"):
                    pass

        if(decision == "5"):
            Login_Page(name)

def check_application(name):
        ApplicL = []  # keep title of applications of the user
        with open(FILENAME_APP, "r") as f:
            ApplicR = csv.reader(f)
            for row in ApplicR:
                if row != [] and row[0] == name:
                    ApplicL.append(row[1])

        JobL = []  # keep title of job in the system.
        with open(FILENAME_JOB, "r") as f2:
            JobR = csv.reader(f2)
            for row in JobR:
                if row != [] and row != ["Title", "Description", "Employer", "Location", "Salary", "Post_Name"]:
                    JobL.append(row[0])

        for element in ApplicL:
            if element not in JobL:
                print()
                print("The job: " + "\"" + element + "\"" + " has been removed")
                delete_application(name, element)


# delede all applications for the job which is deleted
def delete_application(name, title):
    n = []
    with open(FILENAME_APP, "r") as f:
        ApplicR = csv.reader(f)
        for row in ApplicR:
            if row != [] and (row[0] != name or row[1] != title):
                n.append(tuple(row))

    with open(FILENAME_APP, "w") as f2:
        ApplicW = csv.writer(f2)
        for ele in n:
            ApplicW.writerow(ele)
>>>>>>> Epic6
