'''
Manage Input Output file
Manage login
'''
from typing import Any
import job
import csv
import os.path
import console
import student
import utility as u

job_file_name = "job_data.csv"
student_file_name = "student_data.csv"

class Manage:
    def __init__(self):
        #list of job
        self.job_list = []
        self.student_list = []
        
        #title for job data
        if not os.path.isfile(job_file_name):
            with open(job_file_name, "w") as job_file:
                write_csv = csv.writer(job_file)                
        
        #add data from the file to job list
        with open(job_file_name, "r") as job_file:
            read_csv = csv.reader(job_file)
            for row in read_csv:
                if row != []:
                    self.job_list.append(job.Job(row[0], row[1], row[2], row[3], row[4], row[5]))
        
        #student_data.csv
        if not os.path.isfile(student_file_name):
            with open(student_file_name, "w") as student_file:
                write_csv = csv.writer(student_file)

        #add data from the file to student.py        
        with open(student_file_name, "r") as student_file:
            read_csv = csv.reader(student_file)
            for row in read_csv:
                if row != []:
                    self.student_list.append(student.Student(row[0], row[1], row[2], row[3]))
                    
                       

    #get student list and get length of student list
    def get_student_list(self):
        return self.student_list

    def get_length(self):
        return len(self.student_list)

    def login(self):
        #create a new object
        m = Manage()

        #when do not have any account in the system
        if(len(m.get_student_list())) <= 0:
            print("You have to sign up an account!\n")
            return
        
        username = input("Enter username: ")
        password = input("Enter password: ")
        flag = u.findUsername(username)
        flag2 = u.findPassword(password)

        print(flag)
        print(flag2)
    # both username and password have to exist in file to reach successful login
        while flag == False or flag2 == False:
            print("Invalid username/password. Please try again")
            username = input("Enter username: ")
            password = input("Enter password: ")
            flag = u.findUsername(username)
            flag2 = u.findPassword(password)
        print("You have successfully logged in\n")    
        return username   

        
    def add_job(self, job, post_name):
        #number_of_job = 1
        for element in self.job_list:
            if element.get_title() == job.get_title():
                print("Job already exists!")
        
        #if number of job less than 6
        if len(self.job_list) < 5:
            self.job_list.append(job)            
            #write to the file
            with open(job_file_name, 'a') as job_file:
                write_csv = csv.writer(job_file)
                write_csv.writerow((job.get_title(),job.get_description(),job.get_employer(),job.get_location(),job.get_salary(),job.get_post_name()))
                print("\nPosted the Job Sucessfully!\n")
        else: #number of job > 5
            print("\nReach the limit of job (5)!\n")
            return

    
    def post_new_job(self, post_name):
        job_title = input("Enter Job Title: ")
        job_description = input("Enter Job Description: ")
        job_employer = input("Enter The Employer: ")
        job_location = input("Enter Job Location: ")
        job_salary = input("Enter Job Salary: ")
        #need to check valid input
        #check salary input
        
        new_job = job.Job(job_title, job_description, job_employer, job_location, job_salary, post_name)
        # return user's name who posted a job
        
        return self.add_job(new_job, post_name)


    
            

