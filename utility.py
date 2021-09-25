'''
Helpful function
'''
import csv

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