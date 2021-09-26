import csv
import os.path
import pytest
import utility as u
import console as c
import job as j
import manage as ma
from csv import writer
import main
import student as s

# To test password verfication. In Terminal run: pytest test_main.py


class TestClass:
    '''----------------------------------EPIC #1 TESTS-----------------------------------------------------'''
    # Tests if requirements for a valid password are satisfied within main.checkPass()

    # Validates if Less than 8 characters
    def test_checkPass_lessthan8(self):
        assert u.AccountPasswordClass.check_min_characters("1$A") == False  # 3 chars
        assert u.AccountPasswordClass.check_min_characters("1$Abcde") == False  # 7 char
        assert u.AccountPasswordClass.check_min_characters("1$Abcdef") == True  # 8 char

    # Validates if More than 12 characters
    def test_checkPass_morethan12(self):
        assert u.AccountPasswordClass.check_max_characters("1$Abcdefghijk") == False  # 13 characters
        assert u.AccountPasswordClass.check_max_characters("1$Abcdefghij") == True  # 12 characters
        assert u.AccountPasswordClass.check_max_characters("1$Abcdefghi") == True  # 11 characters

    # Validates if it includes an Uppercase letter
    def test_checkPass_noUpper(self):
        assert u.AccountPasswordClass.check_Uppercase_letter("1$abcdefg") == False  # Does not include an Uppercase letter
        assert u.AccountPasswordClass.check_Uppercase_letter("1$Abcdefg") == True  # Does include an Uppercase letter

    # Validates if it includes a digit char
    def test_checkPass_Digit(self):
        assert u.AccountPasswordClass.check_digit("$Abcdefgh") == False  # Does not include a digit char
        assert u.AccountPasswordClass.check_digit("$Abcd5efgh") == True  # Does include a digit char

    # Validates if it includes a non-alphabetic char
    def test_checkPass_nonAlpha(selfs):
        assert u.AccountPasswordClass.check_non_alpha("1Abcdefgh") == False  # Does not include a non-alphabetic char
        assert u.AccountPasswordClass.check_non_alpha("1Abc$defgh") == True  # Does include a non-alphabetic char

    '''----------------------------------EPIC #2 TESTS-----------------------------------------------------'''

    def test_maximimAccounts(self):
        filename = "student_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()

        teststud1 = s.Student("dericwright", "Password123!", "Deric", "Wright")
        assert manage.add_student(teststud1) == teststud1.get_user_name()

        teststud2 = s.Student("matteovescera", "Password123!", "Matteo", "Vescera")
        assert manage.add_student(teststud2) == teststud2.get_user_name()

        teststud3 = s.Student("stefanovisentin", "Password123!", "Stefano", "Visentin")
        assert manage.add_student(teststud3) == teststud3.get_user_name()

        teststud4 = s.Student("darshavala", "Password123!", "Darshan", "Vala")
        assert manage.add_student(teststud4) == teststud4.get_user_name()

        teststud5 = s.Student("panatdawiangngoen", "Password123!", "Panatda", "Wiangngoen")
        assert manage.add_student(teststud5) == teststud5.get_user_name()


    # Tests if adding jobs works
    def test_Jobs(self):
        filename = "job_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()

        testjob1 = j.Job("Developer", "Devs some stuff", "USF", "Tampa", "100000", "Deric")
        assert manage.add_job(testjob1, "Deric") == testjob1.get_poster_name()

        testjob2 = j.Job("Developer2", "Devs some stuff", "USF", "Tampa", "200000", "Nghia")
        assert manage.add_job(testjob2, "Nghia") == testjob2.get_poster_name()

        testjob3 = j.Job("Chef", "cooks stuff", "Hell's Kitchen", "Tampa", "20000", "Matteo")
        assert manage.add_job(testjob3 , "DP") == testjob3 .get_poster_name()

        testjob4 = j.Job("Gamer", "Rules the World", "FaZe Clan", "Tampa", "2000", "Darshan")
        assert manage.add_job(testjob4, "KP") == testjob4.get_poster_name()

        testjob5 = j.Job("Pilot", "Flys stuff", "Southwest", "Tampa", "3000", "Stefano")
        assert manage.add_job(testjob5, "YQ") == testjob5.get_poster_name()

    # Test success story
    def testmain_OpenF(self):
        file = open("success_story.txt", 'r')
        expected = "This is the story of Guy Fieri from Flavor Town\nGuy had to move out of Flavor Town, losing all respect in the culinary world and everything he owned,\nhis only choice was to go back to college!\nHe majored in Computer Science and was looking for oppurtunities in the field but he had no experience.\nHe was not able to successfully learn the necessary skills to pass coding exams and recruitment questions :(\nHowever, his good friend Bobby Flay introduced him to InCollege! This helped Guy learn essential skills and connect with people\neven though he did not have enough experience. This led to Guy finding a job posting \nthat Bobby's company posted and he applied, getting the job and earning Bobby a refferal bonus.\nThe job was located in Flavor Town and Guy was ecstatic to move back.\n\nFor a video on why you would want to join InCollege, select option 4! "
        assert expected == file.read()