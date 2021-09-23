'''
Manage Input Output file
'''
import job
import csv
import os.path

job_file_name = "job_data.csv"

class Manage:
    def __init__(self):
        #list of job
        self.job_list = []

        #title for job data
        if not os.path.isfile(job_file_name):
            with open(job_file_name, "w") as job_file:
                write_csv = csv.writer(job_file)
                write_csv.writerow(("Title","Description","Employer","Location","Salary","Post_Name"))
        
        #add data from the file to job list
        with open(job_file_name, "r") as job_file:
            read_csv = csv.reader(job_file)
            for row in read_csv:
                if row != []:
                    self.job_list.append(job.Job(row[0], row[1], row[2], row[3], row[4], row[5]))
        
    def add_job(self, job, post_name):
        #number_of_job = 1
        for element in self.job_list:
            if element.get_title() == job.get_title():
                print("Job already exists!")
        
        if len(self.job_list) < 6:
            self.job_list.append(job)
            print("Posted the Job Sucessfully!")
            #write to the file
            with open(job_file_name, "a") as job_file:
                write_csv = csv.writer(job_file)
                write_csv.writerow(job.get_title(),job.get_description(),job.get_employer(),job.get_location(),job.get_salary(),job.get_post_name())
        else: #number of job > 5
            print("Reach the limit of job (5)!")
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
        m = Manage()
        # return user's name who posted a job
        return m.add_job(new_job, post_name)


    
            

