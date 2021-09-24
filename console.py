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


def welcome(decision):
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
        decision = input("Press 1 to go back to the menu")
        back_to_menu(decision)
    print("They are a part of the InCollege system")
    print("Join them!")
    print()
    join_Incollege()


def back_to_menu(decision): #gives user a chance to go back to menu at any point
    if decision == '1':
        job_menu()
    while decision != '1':
        decision = input("Invalid input, please press 1 to go back to menu: ")
    job_menu()
        

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
