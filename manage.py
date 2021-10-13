import student as s
import csv
import os.path
import utility
import job as j
import settings as set
import profiles as p
from datetime import datetime

FILENAME_STUDENT = "student_data.csv"
FILENAME_JOB = "job_data.csv"
FILENAME_SETTINGS = "settings.csv"
FILENAME_PROFILE = "profiles.csv"
FILENAME_FRIEND = "friends.csv"
FILENAME_REQUEST = "requests.csv"

class Manage:
    def __init__(self):
        self.student_list = []
        self.job_list = []
        self.settings_list = []
        self.profiles_list = []

        # student_data.csv
        if not os.path.isfile(FILENAME_STUDENT):
            with open(FILENAME_STUDENT,'a') as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("User_Name", "Password", "First_Name", "Last_Name"))

        # Add data from student_data.csv to student_list
        with open(FILENAME_STUDENT,'r') as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != []:
                    self.student_list.append(s.Student(item[0], item[1], item[2], item[3]))


        # Add a Title to the job_data.csv
        if not os.path.isfile(FILENAME_JOB):
            with open(FILENAME_JOB,'a') as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("Title", "Description", "Employer", "Location", "Salary", "Poster_Name"))

        # Add data from job_data to job_list
        with open(FILENAME_JOB,'r') as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != []:
                    self.job_list.append(j.Job(item[0], item[1], item[2], item[3], item[4], item[5]))

        # Adds titles for the settings.csv
        if not os.path.isfile(FILENAME_SETTINGS):
            with open(FILENAME_SETTINGS, "w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("user", "email_notifications", "sms_notifications", "targeted_ads", "language_set"))

        # Adds data from settings.csv to settings_list
        with open(FILENAME_SETTINGS, "r") as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != []:
                    self.settings_list.append(set.Settings(item[0],item[1], item[2], item[3], item[4]))

        # Adds titles for the profiles.csv
        if not os.path.isfile(FILENAME_PROFILE):
            with open(FILENAME_PROFILE, "w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("user", "title", "major", "university", "biography", "experience", "education"))

        # Adds data from profiles.csv to profiles_list
        with open(FILENAME_PROFILE, "r") as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != []:
                    self.profiles_list.append(p.Profiles(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))


    def get_list(self):
        return self.student_list


    def get_length(self):
        return len(self.student_list)


    def login(self):
        # creates a new Manage object
        manage = Manage()

        if len(manage.get_list()) == 1:
            print("\nThere aren't any accounts.")
            print("Create a New account to proceed.\n")
            return None

        # create an object of class AccountExistClass
        account = utility.AccountExistClass()

        user_name = input("Enter username: ")

        # Checks if the username exists in student_data.csv file
        while not account.check_name(user_name):
            user_name = input("Enter user name again: ")

        # Currently assume that the user exists
        password = input("Enter a password: ")
        while not account.check_password(user_name, password):
            password = input("Incorrect password. Please try again: ")

        print("\nYou have successfully logged in.")
        return user_name

    def register(self):
        manage = Manage()
        # User input to create a new account
        username = input("Enter username: ")
        password = input ("Enter a password: ")
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")

        # Creates a new object of class AccountPasswordClass
        account = utility.AccountPasswordClass()

        # Checks password validation requirements
        while not(account.check_min_characters(password)) or not(account.check_max_characters(password)) or not(account.check_Uppercase_letter(password)) or not(account.check_non_alpha(password)) or not(account.check_digit(password)):
            password = input("Enter a password again: ")

        # Create a new student object and add it to the student_data.csv file
        student = s.Student(username, password, firstname, lastname)
        return manage.add_student(student)


    def find_people(self, first, last):
        manage = Manage()
        name = first + " " + last
        # Checks if a friend is in InCollege
        for item in manage.student_list:
            if item.get_name() == name:
                print("\nThey are a part of the InCollege system.")
                return item.get_user_name()

        print("\nThey are not yet a part of the InCollege system yet.")
        return None

    def add_job(self, job, n):
        if len(self.job_list) >= 5:
            print("\nYou cannot post anymore jobs. Limited to 5.")
            return None

        else:
            self.job_list.append(job)
            print("\nJob has been posted.")
            with open(FILENAME_JOB,"a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow((job.get_title(), job.get_description(), job.get_employer(), job.get_location(), job.get_salary(), job.get_poster_name()))

            return(job.get_poster_name())


    def new_job(self, poster_name):
        manage = Manage()

        title = input("Enter Job Title: ")
        description = input("Enter Job Description: ")
        employer = input("Enter The Employer: ")
        location = input("Enter Job Location: ")
        salary = input("Enter Job Salary: ")

        account = utility.InputValueClass()
        # Check if the salary is correct
        while not account.check_isNumber(salary):
            print("Please input a valid salary.")
            salary = input("Salary: ")

        job = j.Job(title, description, employer, location, salary, poster_name)
        return manage.add_job(job,poster_name)

    # Adds a new object student with first name, last name and password to student_data.csv file
    def add_student(self, student):
        for item in self.student_list:
            if item.get_user_name() == student.get_user_name():
                print("\nThere is an account with the same username")
                print("Try again!")
                return None

        if len(self.student_list) < 5:
            self.student_list.append(student)
            user_name = student.get_user_name()
            print("Account successfully created.")

            with open(FILENAME_STUDENT, "a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow((student.get_user_name(), student.get_password(), student.get_first(), student.get_last()))

            # Sets the default settings for the user.
            with open(FILENAME_SETTINGS, "a") as file_stg:
                writer_csv = csv.writer(file_stg)
                writer_csv.writerow((user_name, "ON", "ON", "ON", "English"))

            return user_name

        else:
            print("\nAll accounts have been created. Can't add anymore.")
            return None

    def manage_settings(self, username, field, state):
        manage = Manage()
        # find the settings object associated with that user
        for toggleitem in manage.settings_list:
            if toggleitem.get_user() == username:
                if field == "email_notifications":
                    return toggleitem.get_email_notifications()
                elif field == "sms_notifications":
                    return toggleitem.get_sms_notifications()
                elif field == "targeted_ads":
                    return toggleitem.get_targeted_ads()
                elif field == "language_set":
                    return toggleitem.get_language()
                else:
                    print("This field in the Guest Controls/Settings do not exist")
                    return "NONE"

        # Settings are only made when a user is created. Check if it returns the user's username
        print("The user Does Not Exist.")
        return toggleitem.get_user()

    # Create profile function
    def create_profile(self, name):
        title = input("Enter a Title: ")
        major = input("Enter a Major: ")
        major = major.title()
        university = input("Enter University: ")
        university = university.title()
        biography = input("About Yourself: ")

        check_experience = input("Do you have any experience you would like to add? (Yes/No)  ")
        experience = ""

        while check_experience.upper() != "YES" and check_experience.upper() != "NO":
            check_experience = input("Invalid Input. Please Try Again. Do you have any experience you would like to add? (Yes/No) ")

        if check_experience.upper() == "YES":
            for value in range(3):
                experience_title = input("Job Title: ")
                experience_employer = input("Employer: ")
                experience_date_started = input("Date Started MM/DD/YYYY: ")
                while (check_date(experience_date_started) == False):
                    experience_date_started = input("Date not valid. Please Try Again: ")
                experience_date_ended = input("Date Ended MM/DD/YYYY: ")
                while (check_date(experience_date_ended) == False or compare_dates(experience_date_started, experience_date_ended) == False):
                    if (check_date(experience_date_ended) == False):
                        experience_date_ended = input("Date not valid. Please Try Again: ")
                    elif (compare_dates(experience_date_started, experience_date_ended) == False):
                        experience_date_ended = input("End date is before start date. Please Try Again: ")

                experience_location = input("Job Location: ")
                experience_description = input("Job Description: ")
                experience = experience + "(" + experience_title + "," + experience_employer + "," + experience_date_started + "," + experience_date_ended + "," + experience_location  + "," + experience_description + ")"
                # Allows up to 3 experiences to be added
                if (value < 2):
                    new_experience = input("Do you have more experience to add? Enter YES/NO  ")
                    while new_experience.upper() != "YES" and new_experience.upper() != "NO":
                        new_experience = input("Invalid Input. Try Again: ")
                if new_experience.upper() == "NO":
                    break

        school = input("\nEducation Information:\nEnter School Name: ")
        degree = input("Enter Degree: ")
        years = input("Enter the Years Attended: ")
        education = "[" + school + "," + degree + "," + years + "]"

        print("\nYour profile has been made.")
        with open(FILENAME_PROFILE, "a") as file:
            writer_csv = csv.writer(file)
            writer_csv.writerow((name, title, major, university, biography, experience, education))

    def view_profile(self, name):
        with open(FILENAME_PROFILE, "r") as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != [] and item[0] == name:
                    print()
                    for row in self.student_list:
                        if row.get_user_name() == name:
                            print(row.get_name())
                    print("Title: " + item[1])
                    print("Major: " + item[2])
                    print("University Name: " + item[3])
                    print("About me: " + item[4])
                    experience = item[5]
                    experience_list = experience.split(")")
                    print(experience_list)
                    experience_list.pop()

                    print()
                    for element in experience_list:
                        sub_element = element[1:]
                        list_sub_experience = sub_element.split(",")
                        print("Title: " + list_sub_experience[0])
                        print("Job Description: " + list_sub_experience[5])
                        print("Work: " + list_sub_experience[4])
                        print("Start date: " + list_sub_experience[2])
                        print("End date: " + list_sub_experience[3])
                        print("Employer: " + list_sub_experience[1])

                    print("\nMy Education Information:")
                    education = item[6]
                    len_education = len(education) - 1
                    sub_education = education[1:len_education]

                    list_sub_education = sub_education.split(",")
                    print("University: " + list_sub_education[0])
                    print("Major: " + list_sub_education[1])
                    print("Years attended: " + list_sub_education[2])
                    return name

        print("\nProfile not created.")
        return name

    def add_friend(self, s1, s2):
        with open(FILENAME_FRIEND, "a") as file:
            writer_csv = csv.writer(file)
            writer_csv.writerow((s1, s2))
            writer_csv.writerow((s2, s1))

    def return_students(self, name):
        blank = []
        count = 0
        lines = list()
        results = list()

        # read current students and fill lines with relavent student
        with open(FILENAME_STUDENT, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count += 1

                    if lines[count - 1][3] == name:
                        results.append(row)

            return results

    def return_names(self, last):
        blank = []
        count = 0
        lines = list()
        names = list()
        # read current students and fill lines with relavent student
        with open(FILENAME_STUDENT, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count += 1

                    if lines[count - 1][3] == last:
                        names.append(row)

            return names

    def return_names_uni(self, uni):
        blank = []
        count = 0
        lines = list()
        names = list()
        # read current students and fill lines with relavent student
        with open(FILENAME_PROFILE, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count += 1

                    if lines[count - 1][3] == uni:
                        names.append(row)

            return names

    def return_names_major(self, major):
        blank = []
        count = 0
        lines = list()
        names = list()
        # read current students and fill lines with relavent student
        with open(FILENAME_PROFILE, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count += 1

                    if lines[count - 1][3] == major:
                        names.append(row)

            return names

    def send_requests(self, sname, unames):
        blank = []
        try:
            unames.remove(sname)
        except ValueError:
            gar = 0
        if len(unames) == 0:
            print("No students found")
            print()
        else:
            dup = 0
            print("Request to connect?")
            print("0. No.")
            print("1. Yes")
            for uname in unames:
                choice = input(uname + "?: ")
                choice = utility.checkUserInput(choice, 0, 1)
                if choice == "1":
                    with open(FILENAME_REQUEST, 'r') as readFile:
                        reader = csv.reader(readFile)
                        for row in reader:
                            if row != blank:
                                if row[0] == sname and row[1] == uname:
                                    dup = dup + 1

                    with open(FILENAME_FRIEND, 'r') as readFile2:
                        reader2 = csv.reader(readFile2)
                        for row in reader2:
                            if row != blank:
                                if row[0] == sname and row[1] == uname:
                                    dup = dup + 1

                    if dup == 0:
                        with open(FILENAME_REQUEST, "a") as file:
                            writer_csv = csv.writer(file)
                            writer_csv.writerow((sname, uname))
                        print("Connection Request Sent")
                    else:
                        print("Friend request was sent or accepted")


# Functions to check dates
def check_date(date_text):
    try:
        datetime.strptime(date_text, '%m/%d/%Y')
        return True
    except ValueError:
        return False


def compare_dates(date1, date2):
    date1 = datetime.strptime(date1, '%m/%d/%Y')
    date2 = datetime.strptime(date2, '%m/%d/%Y')
    return date1<date2


