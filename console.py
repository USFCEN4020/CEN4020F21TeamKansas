import time
import manage as m
import utility
import csv
import friend
import os.path
import student as s
import job as j
from datetime import datetime
from datetime import timedelta

FILENAME_MES = "pending_messages.csv" #FromThisUsername, ToThisUsername, the Message
FILE_SAVE_MES = "messages.csv"
FILENAME_STUDENT = "student_data.csv"
FILENAME_APP = "applications.csv"
FILENAME_SETTINGS = "settings.csv"
FILENAME_PROFILE = "profiles.csv"
FILENAME_JOB = "job_data.csv"
FILENAME_FRIEND = "friends.csv"
FILENAME_REQUEST = "requests.csv"
FILENAME_POL = "policy.csv"
FILENAME_NEW_USER = "new_user.csv"
FILENAME_NEW_JOB = "new_jobs_notif.csv"
FILENAME_DEL_JOB = "del_jobs_notif.csv"
FILENAME_COURSES = "courses.csv"
blank_string = " "


# The screen is at the begin of the program, or after its options finish (log-in, sign up)
def Welcome_Page():
    if (not os.path.exists(FILENAME_COURSES)):
        open(FILENAME_COURSES, 'w').close()
    if (not os.path.exists("save_job.csv")):
        open("save_job.csv", 'w').close()
    if (not os.path.exists("courses.csv")):
        open("courses.csv", 'w').close()
    if (not os.path.exists(FILENAME_APP)):
        open(FILENAME_APP, 'w').close()
    if (not os.path.exists("MyCollege_appliedJobs.txt")):
        open("MyCollege_appliedJobs.txt", 'w').close()
    if (not os.path.exists("MyCollege_jobs.txt")):
        open("MyCollege_jobs.txt", 'w').close()
    if (not os.path.exists("MyCollege_profiles.txt")):
        open("MyCollege_profiles.txt", 'w').close()
    if (not os.path.exists("MyCollege_savedJobs.txt")):
        open("MyCollege_savedJobs.txt", 'w').close()
    if (not os.path.exists("MyCollege_users.txt")):
        open("MyCollege_users.txt", 'w').close()
    if (not os.path.exists("newJobs.txt")):
        open("newJobs.txt", 'w').close()
    if (not os.path.exists("studentAccounts.txt")):
        open("studentAccounts.txt", 'w').close()
    if (not os.path.exists("newtraining.txt")):
        open("newtraining.txt", 'w').close()

    print("\nWelcome to InCollege! An application designed for college students hoping to connect with other college students in effort to land a job!")
    print("")

    print("The following additions (or refusals) are from the API:")
    read_newJobs()
    read_studentAccounts()
    read_savedJobs()
    read_appliedJobs()

    print("Are you a new user? Or do you already have an account? Select an option below")
    print("1. Create an account")
    print("2. Login to an existing account")
    print("3. Connect with someone you know")
    print("4. Play the video")
    print("5. Training")
    print("6. Useful Links")
    print("7. InCollege Important Links")
    print("8. Exit inCollege")
    decision = input("Your selection: ")

    # Used for input validation. User should only choose a value 1-8
    decision = utility.checkUserInput(decision, 1, 8)

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
        Training_Page()
    elif (decision == "6"):
        UsefulLinks_Page(0, blank_string)
    elif (decision == "7"):
        ImportantLinks_Page(0, blank_string)
    elif (decision == "8"):
        exit()


def Login_Page(name):
    #friend.check_requests(name)
    #maybe add check_application(name) here?
    #check_messages(name)

    print("Enter 1 to check any notifications. Enter 0 to continue")
    pick = input("Your selection: ")
    pick = utility.checkUserInput(pick, 0, 1)
    if pick == "1":
        friend.check_requests(name)
        check_application(name)
        check_application(name)
        check_messages(name)
        check_profile_creation(name)
        check_new_user(name)
        check_applied_in_seven_days(name)
        check_new_job(name)
        check_del_job(name)

    print()
    print("\nSelect one of the below options:")
    print("1. Create Profile")#
    print("2. View Profile")#
    print("3. Search a job")#
    print("4. Post a Job") #
    print("5. Delete a Job") #
    print("6. Learn a New Skill")#
    print("7. Useful Links")#
    print("8. inCollege Important Links")#
    print("9. Connect with Friends") #
    print("10. My Connections")#
    print("11. Send a Message")
    print("12. InCollege Learning")
    print("13. Log Out")
    decision = input("\nYour selection: ")

    # Used for input validation. User should only choose a value 1-12
    decision = utility.checkUserInput(decision, 1, 13)

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
        LearnSkill_Page(name)
    elif decision == "7":
        UsefulLinks_Page(1, name)
    elif decision == "8":
        ImportantLinks_Page(1, name)
    elif decision == "9":
        friend.search_friend(name)
    elif decision == "10":
        friend.show_connection(name)
    elif decision == "11":
        send_message(name)
    elif decision == "12":
        InCollege_Learning_Screen(name)
    elif decision == "13":
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
    lines = list()
    if name != None:  # sign up successfully
        lines.append(name)
        with open(FILENAME_STUDENT, "r") as file1:
            reader_csv1 = csv.reader(file1)
            for row1 in reader_csv1:
                if row1 != []:
                    lines.append(row1[0])

        with open(FILENAME_NEW_USER, "a") as file:
            writer_csv = csv.writer(file)
            writer_csv.writerow(lines)
        Login_Page(name)
    #add name to new_user file
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
        check_num_jobs_appliedto(name)
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
                            manage.save_date_LastJobAppliedTo(name)
                    elif (thirdDecision == "2"):  # Save
                        manage.add_save_job(name, j[int(secDecision) - 1][0])

            read_savedJobs()
            read_appliedJobs()

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
            read_savedJobs()

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


############################ EPIC 7 MESSAGING ##############################################

def get_friends(name):
    fri_list = [] #grabbing usernames
    with open (FILENAME_FRIEND, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and row [0] == name and (row[1] not in fri_list):
                fri_list.append(row[1])
            elif row != [] and row [1] == name and (row [0] not in fri_list):
                fri_list.append(row[0])

    return fri_list


#PRINTS ALL THE PROFILES IN student.csv
def all_profiles(name):
    names_list = list()
    username_list = list()
    empty = []
    valid_users = get_friends(name)

    with open(FILENAME_STUDENT, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if (row != empty) and (row[0] != name) and (row[0] != "User_Name"): #for empty space, which we dont want
                username_list.append(row[0])
                names_list.append(row[2]+" "+row[3]) #first and last name

    i = 0
    print("InCollege Users: ")
    while i < len(names_list):
        if(username_list[i] in valid_users):
            print(str(i+1)+". " + username_list[i]+": "+names_list[i] + " - FRIEND")
        else:
            print(str(i+1)+". " + username_list[i]+": "+names_list[i])
        i += 1
    return username_list


#SENDS MESSAGE TO A FRIEND (OR ANYONE IF PLUS MEMBER)
def send_message(name):
    with open(FILENAME_STUDENT, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row != [] and (row[0] == name):
                tier = row[4] #find what tier the person is

    #Display all people in student.csv
    all_users = all_profiles(name)
    valid_users = get_friends(name)

    #Choose a user to send a message via numbered list
    choice = input("Enter the corresponding number for which user to message: ")
    choice = utility.checkUserInput(choice,1,len(all_users)) # fixed its in utility
    sendMessageTo = all_users[int(choice)-1] 
    allowToSend = False

    if tier == "standard":
        for x in valid_users:
            if x == sendMessageTo:
                allowToSend = True
    elif tier == "plus": 
        allowToSend = True

    #See if we send the message or not (depending on tier level)
    if allowToSend == True:
        manage = m.Manage()
        message = input("Type the message you want to send to "+sendMessageTo+":\n")
        manage.add_pending_message(name, sendMessageTo, message)
        print("Message sent!")
    else: 
        print("Sorry, you must be friends with that person to send messages")

    #Menu
    print("Select one of the below options:")
    print("(1) Send another message")
    print("(2) Return to Log In Screen")
    choice = input("Your selection: ")
    choice = utility.checkUserInput(choice,1,2)

    if (choice == "1"):
        send_message(name)
    else:
        Login_Page(name)

def check_profile_creation(name):
    #Read profile name and if none match then send message
    send_message = 1
    with open(FILENAME_PROFILE, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and row[0] == name:
                #if name found then don't send message.
                send_message = 0
    print_profile_notification(send_message)
    return send_message

def print_profile_notification(send_message):
    if send_message == 1:
        print("You have not created a profile yet! Please make a profile")

def check_new_user(name):
    overwrite = list()
    check = 0
    with open(FILENAME_NEW_USER, "r") as file:
        reader = csv.reader(file)
        user = list(reader) 
        for row in user:
            if(row == []):
                continue
            new_row = list()
            if(row[0] == name):
                for entry in row:
                    new_row.append(entry)
            else:
                for entry in row:
                    if entry == name:
                        check = 1
                        newName = row[0]
                        with open(FILENAME_STUDENT, "r") as file1:
                             reader_csv1 = csv.reader(file1)
                             for row1 in reader_csv1:
                                if row1 != [] and row1[0] == newName:
                                    first_name = row1[2]
                                    last_name = row1[3]
                                    print(first_name +" " +last_name + " has joined in college")
                    else:
                        new_row.append(entry)
            overwrite.append(new_row)

    with open(FILENAME_NEW_USER, "w") as file:
        writer = csv.writer(file)
        writer.writerows(overwrite) 

    return check


#NOTIFIES USER THAT THEY HAVE RECEIVED A MESSAGE AND ALLOWS THEM THE OPTION TO CHECK
#IF THEY DO NOT WANT TO CHECK, NEXT TIME THEY LOGIN IT WILL PROMPT AGAIN
def check_messages(name):
    message_list = [] #(from, message) in this format
    with open (FILENAME_MES, "r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and row [1] == name:
                message_list.append((row[0],row[1], row[2]))

    if len(message_list) > 0:
        print ("You have recieved messages from some people!")
        for info in message_list:   
            From, To, Message = info
            print()
            print ("Do you want to see the message from: " + "\"" + From + "\"")
            print("Select one of the below options:")
            print("(1) Yes")
            print("(2) No")
            choice = input("Your selection: ")
            choice = utility.checkUserInput(choice,1,2)

            if choice == "1":
                print()
                print(Message)
                print ("Do you want to save the message from: " + "\"" + From + "\"")
                print("Select one of the below options:")
                print("(1) Yes")
                print("(2) No")
                choice = input("Your selection: ")
                choice = utility.checkUserInput(choice,1,2)

                
                if (choice == "1"):
                    add_message(From,To,Message) 
                    delete_pending_message(From, To, Message) 
                elif(choice == "2"):
                    delete_pending_message(From, To, Message)
    
                print("Do you want to respond the message from " + "\"" + From + "\"")
                print("Select one of the below options:")
                print("(1) Yes")
                print("(2) No")
                choice = input("Your selection: ")
                choice = utility.checkUserInput(choice,1,2)

                if choice == "1":
                    text = input ("Please type a message: ")
                    with open(FILENAME_MES,"a") as file:
                        writer = csv.writer(file)
                        writer.writerow((To, From, text))
                    print("The message was sent to " + "\"" + From + "\"")
                elif choice == "2":
                    pass


#NEW MESSAGE FOR message.csv
def add_message(From, To, Message):
    with open(FILE_SAVE_MES, "a") as file:
        writer = csv.writer(file)
        writer.writerow((From, To, Message))


#DELETE ROW FROM pending_message.csv
def delete_pending_message (From, To, Message):
    delete_list = []
    with open(FILENAME_MES,"r") as file:
        reader_csv = csv.reader(file)
        for row in reader_csv:
            if row != [] and (row[0] != From or row[1] != To or row[2] != Message):
                delete_list.append(tuple(row))

    with open(FILENAME_MES,"w") as file:
        writer_csv = csv.writer(file)
        for info in delete_list:
            writer_csv.writerow(info)

######################## JOB STUFF ###############################

def check_applied_in_seven_days(name):
    #checks if its been seven days since applying to a job
    with open(FILENAME_STUDENT, "r") as file:
        reader = csv.reader(file)
        lines = list(reader)
        for row in lines:
            if (row != []) and (row[0] == name):
                lastApplied = row[5]
                _today =  datetime.today().strftime('%Y %m %d')
                today = datetime.strptime(_today, '%Y %m %d')
                sevenMinusToday = today+timedelta(days=-7)
                if(row[5] != "0"):
                    lastTime = datetime.strptime(lastApplied, '%Y-%m-%d %H:%M:%S')
                    if(lastTime <= sevenMinusToday):
                        #send job notification
                        print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")

def check_num_jobs_appliedto(name):
    with open(FILENAME_APP,"r") as file:
                reader_csv = csv.reader(file)
                i = 0
                for row in reader_csv:
                    if row != [] and row[0] == name:
                        i += 1
    print("\nYou have currently applied for "+str(i)+" job(s).")

def check_new_job(name):
    overwrite = list()

    with open(FILENAME_NEW_JOB, "r") as file:
        reader = csv.reader(file)
        job = list(reader) 
        for row in job: #each row is a 'job title', 'list of users who have not seen'
            if(row == []):
                continue
            new_row = list()
            if(row != []) and (row[0] != "jobTitle"):
                for entry in row:
                    if entry == name:
                        print("A new job "+row[0]+" has been posted")
                    else:
                        new_row.append(entry)
            overwrite.append(new_row)

    with open(FILENAME_NEW_JOB, "w") as file:
        writer = csv.writer(file)
        writer.writerows(overwrite) 

def check_del_job(name):
    new_notif = list()

    with open(FILENAME_DEL_JOB, "r") as file:
        reader = csv.reader(file)
        notif = list(reader) 
        for row in notif:
            if (row != []) and (row[0] == name):
                print("The job \'"+row[1]+"\' you applied for has been deleted.")
            elif (row != []):
                new_notif.append(row)

    with open(FILENAME_DEL_JOB, "w") as file:
        writer = csv.writer(file)
        writer.writerows(new_notif)


#####################   Epic 9 Training   ########################

def Training_Page():
    TrainingList = read_Training()
    print()
    print("Select one of the below options:")
    print("1. Training and Education")
    print("2. IT Help Desk")
    print("3. Business Analysis and Strategy")
    print("4. Security")
    i = 4

    if TrainingList != 0:
        for c in TrainingList:
            i = i + 1
            print("(" + str(i) + ") " + c, end='\n')
    i = i + 1
    print("(" + str(i) + ") Return to Main Menu")
    choice = input("Your selection: ")
    print()

    if (choice == "1"):
        Training_Education_Page()
    elif (choice == "2"):
        print("Coming soon!")
        Training_Page()
    elif (choice == "3"):
        BusinessAnalysis_Screen()
    elif (choice == "4"):
        print("coming soon!")
        Training_Page()
    elif (choice == str(i)):
        Welcome_Page()
    else:
        print("coming soon!")
        Welcome_Page()


def Training_Education_Page():
    print()
    print("Select one of the below options:")
    print("1. Inverview training")
    print("2. programming training ")
    print("3. Buisness training")
    print("4. Medical training")
    print("5. Go back to training screen")
    choice = input("Your selection: ")
    print()

    if (choice == "1"):
        print("Under Construction")
        Training_Education_Page()
    elif (choice == "2"):
        print("Under Construction")
        Training_Education_Page()
    elif (choice == "3"):
        print("Under Construction")
        Training_Education_Page()
    elif (choice == "4"):
        print("Under Construction")
        Training_Education_Page()
    elif (choice == "5"):
        Training_Page()


def BusinessAnalysis_Screen():
    print()
    print("Trending Courses:")
    print("1. How to use InCollege Learning")
    print("2. Train the Trainer")
    print("3. Gamification of Learning")
    print("4. Not seeing what you’re looking for? Sign in to see all 7,609 results.")
    print("5. Return to Main Menu")
    choice = input("Your selection: ")
    print()

    if (choice == "1"):
        sign_in()
    elif (choice == "2"):
        sign_in()
    elif (choice == "3"):
        sign_in()
    elif (choice == "4"):
        sign_in()
    elif (choice == "5"):
        Welcome_Page()


def InCollege_Learning_Screen(name):
    TrainingList = read_Training()
    print()
    check_Training(name)
    choice = input("Your selection: ")
    print()

    if (choice == "1"):
        completeTraining(name, "How to use InCollege Learning")
    elif (choice == "2"):
        completeTraining(name, "Train the Trainer")
    elif (choice == "3"):
        completeTraining(name, "Gamification of Learning")
    elif (choice == "4"):
        completeTraining(name, "Understanding the Architectural Design Process")
    elif (choice == "5"):
        completeTraining(name, "Project Management Simplified")
    else:
        i = 5
        for c in TrainingList:
            i = i + 1
            if choice == str(i):
                completeTraining(name, c)
        i = i + 1
        if (choice == str(i)):
            Login_Page(name)


def completeTraining(name, course):
    with open(FILENAME_COURSES, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    for c in data:
        if not c:
            continue
        else:
            if (c[0] == name and c[1] == course):
                choice = " "
                while (choice.lower() != "yes" or choice.lower() != "No"):
                    choice = input("You have already taken this course, do you want to take it again? (Yes/No)")
                    if choice.lower() == "yes":
                        print("You have now completed this training")
                        InCollege_Learning_Screen(name)
                    elif choice.lower() == "no":
                        print("Course Cancelled")
                        InCollege_Learning_Screen(name)
    add_Course(name, course)
    write_Training()
    print("You have now completed this training")
    InCollege_Learning_Screen(name)


def check_Training(name):
    TrainingList = read_Training()
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    with open(FILENAME_COURSES, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for c in data:
        if not c:
            continue
        else:
            if (c[0] == name):
                if c[1] == "How to use InCollege Learning":
                    one = " [Taken]"
                elif c[1] == "Train the Trainer":
                    two = " [Taken]"
                elif c[1] == "Gamification of Learning":
                    three = " [Taken]"
                elif c[1] == "Understanding the Architectural Design Process":
                    four = " [Taken]"
                elif c[1] == "Project Management Simplified":
                    five = " [Taken]"

    print("Courses you can take:")
    print("1. How to use InCollege Learning" + one)
    print("2. Train the Trainer" + two)
    print("3. Gamification of Learning" + three)
    print("4. Understanding the Architectural Design Process" + four)
    print("5. Project Management Simplified" + five)
    i = 5
    for d in TrainingList:
        i = i + 1
        taken = ""
        for f in data:
            if not f:
                continue
            if f[0] == name and f[1] == d:
                taken = " [Taken]"
        print("(" + str(i) + ") " + d + taken)

    i = i + 1
    print("(" + str(i) + ") Return to Main Menu")


def add_Course(name, course):
    with open(FILENAME_COURSES, "a") as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow((name, course))


def sign_in():
    print("Sign into your INCollege Account")
    name = None
    while name == None:  # if the user fails when logging in the account
        manage = m.Manage()  # create a new object Manage
        name = manage.login()  # get user's name after logging in successful
    Login_Page(name)


############# Epic 10 #####################

def read_newJobs():
    if os.path.exists("newJobs.txt"):
        manage = m.Manage()
        lines = list()
        jobs = list()
        f = open("newJobs.txt", "r")
        lines = f.readlines()
        f.close()
        i = 0
        title = ""
        description = ""
        employer = ""
        location = ""
        salary = 0
        poster = ""
        while (i < len(lines)):
            title = lines[i]
            i = i + 1
            description = ""
            while (lines[i] != "&&&\n"):
                description += (lines[i].rstrip('\n') + ' ')
                i = i + 1
            i = i + 1
            employer = lines[i]
            i = i + 1
            location = lines[i]
            i = i + 1
            salary = int(lines[i])
            i = i + 1
            poster = lines[i]
            i = i + 1
            i = i + 1
            newJ = j.Job(title.rstrip('\n'), description.rstrip('\n'), employer.rstrip('\n'), location.rstrip('\n'),
                         salary, poster.rstrip('\n'))
            manage.add_job(newJ, "API_Input")
            jobs.append(newJ)
        return jobs


def read_studentAccounts():
    if os.path.exists("studentAccounts.txt"):
        manage = m.Manage()
        lines = list()
        students = list()
        f = open("studentAccounts.txt", "r")
        lines = f.readlines()
        f.close()
        i = 0
        username = ""
        password = ""
        fname = ""
        lname = ""
        while (i < len(lines)):
            username = lines[i]
            i = i + 1
            password = lines[i]
            i = i + 1
            fname = lines[i]
            i = i + 1
            lname = lines[i]
            i = i + 1
            i = i + 1
            newS = s.Student(username.rstrip('\n'), password.rstrip('\n'), fname.rstrip('\n'), lname.rstrip('\n'))
            manage.add_student(newS)
            students.append(newS)
        return students


############ Reads and adds courses from newtraining.txt ############
def read_Training():
    if os.path.exists("newtraining.txt"):
        lines = list()
        newlist = list()
        f = open("newtraining.txt", "r")
        lines = f.read().split('\n')
        f.close()
        for d in lines:
            if d == '':
                continue
            else:
                newlist.append(d)
        return newlist


############ Writes Completed Courses for each user into MyCollege_training.txt ############
def write_Training():
    p = open("MyCollege_training.txt", "w")
    with open("courses.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data.sort()
    name = ""
    for c in data:
        if not c:
            continue
        if name == "":
            name = c[0]
            p.write(c[0] + "\n" + c[1] + "\n")
        elif c[0] == name:
            p.write(c[1] + "\n")
        elif c[0] != name:
            p.write("=====\n")
            name = c[0]
            p.write(c[0] + "\n" + c[1] + "\n")


############ Saved Jobs API ############
def read_savedJobs():
    p = open("MyCollege_savedJobs.txt", "w+")
    with open("save_job.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data.sort()
    name = ""
    for c in data:
        if not c:
            continue
        if name == "":
            name = c[0]
            p.write(c[0] + "\n" + c[1] + "\n")
        elif c[0] == name:
            p.write(c[1] + "\n")
        elif c[0] != name:
            p.write("=====\n")
            name = c[0]
            p.write(c[0] + "\n" + c[1] + "\n")


############ Applied Jobs API ############
def read_appliedJobs():
    p = open("MyCollege_appliedJobs.txt", "w+")
    with open("applications.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    while ([] in data):
        data.remove([])
    data.sort(key=lambda x: x[1])
    title = ""
    for c in data:
        if title == "":
            title = c[1]
            p.write(c[1] + "\n" + c[0] + "\n\"" + c[5] + "\"\n")
        elif c[1] == title:
            p.write(c[0] + "\n\"" + c[5] + "\"\n")
        elif c[1] != title:
            p.write("=====\n")
            title = c[1]
            p.write(c[1] + "\n" + c[0] + "\n\"" + c[5] + "\"\n")