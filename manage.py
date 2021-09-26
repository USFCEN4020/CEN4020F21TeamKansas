import student as s
import csv
import os.path
import utility
import job as j

FILENAME_STUDENT = "student_data.csv"
FILENAME_JOB = "job_data.csv"

class Manage:
    def __init__(self):
        self.student_list = []
        self.job_list = []

        # student_data.csv
        if not os.path.isfile(FILENAME_STUDENT):
            with open(FILENAME_STUDENT,"a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("User_Name", "Password", "First_Name", "Last_Name"))

        # Add data from student_data.csv to student_list
        with open(FILENAME_STUDENT,"r") as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != []:
                    self.student_list.append(s.Student(item[0], item[1], item[2], item[3]))


        # Add a Title to the job_data.csv
        if not os.path.isfile(FILENAME_JOB):
            with open(FILENAME_JOB,"a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("Title", "Description", "Employer", "Location", "Salary", "Post_Name"))

        # Add data from job_data to job_list
        with open(FILENAME_JOB,"r") as file:
            reader_csv = csv.reader(file)
            for item in reader_csv:
                if item != []:
                    self.job_list.append(j.Job(item[0], item[1], item[2], item[3], item[4], item[5]))

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
            return user_name

        else:
            print("\nAll accounts have been created. Can't add anymore.")
            return None
