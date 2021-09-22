import csv
from csv import writer
import os.path
from csv import writer
from student import Student

studentList = []  # student list used to add student object attributes and insert into file
file_exists = os.path.exists('student_data.csv')
if not file_exists:
    file = open('student_data.csv', 'w')
file = open("student_data.csv")
reader = csv.reader(file)
lines = len(list(reader))

#test git
print("Hello")
print("Haha")
#hello

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
        register()
    elif decision == "2":
        login()
    else:
        print("Invalid option, please try again")
        decision = input("1. Create an account\n2. Login\nYour selection: ")
        welcome(decision)


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


def findUsername(username):
    # searches file for username for login
    csv_file = csv.reader(open("student_data.csv", "r"), delimiter=",")
    # loop through the csv list
    for line in csv_file:
        if username in line:
            return True
    return False


def findPassword(password):
    # searches file for password for login
    csv_file = csv.reader(open("student_data.csv", "r"), delimiter=",")
    # loop through the csv list
    for line in csv_file:
        if password in line:
            return True
    return False


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    flag = findUsername(username)
    flag2 = findPassword(password)
    # both username and password have to exist in file to reach successful login
    while not flag and not flag2:
        print("Invalid username/password. Please try again")
        username = input("Enter username: ")
        password = input("Enter password: ")
        flag = findUsername(username)
        flag2 = findPassword(password)
    print("You have successfully logged in")
    menu()


def menu():
    print("")
    print("1. Search for job/internship")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. Log out")
    print("5. Exit program")
    choice = input("Your selection: ")

    if (choice == "1"):
        print("Under construction for now"
              " returning to menu")
        menu()
    elif(choice == "2"):
        print("Under construction for now"
              " returning to menu")
        menu()
    elif(choice == "3"):
        menu_learnskill()
    elif(choice == "4"):
        main()
    elif(choice == "5"):
        exit()


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
        menu()


def register():

    # Checks if the max accounts have been reached
    maxAccountFlag = max_accts()
    if maxAccountFlag:
        quit()

    # take input
    username = input("Enter username: ")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    password = input("Enter your password: ")

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


def main():  # controller of program
    print("Welcome to InCollege! An application designed for college students hoping to connect with other college students in effort to land a job!")
    print("")
    print("Are you a new user? Or do you already have an account? Select an option below")
    decision = input("1. Create an account\n2. Login\nYour selection: ")
    welcome(decision)

if __name__ == "__main__":
    # execute only if run as a script
    main()
