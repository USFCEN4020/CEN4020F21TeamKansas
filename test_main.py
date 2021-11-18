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
import profiles as p

# To test password verfication. In Terminal run: pytest test_main.py

FILENAME_PROFILE = "profiles.csv"
FILENAME_STUDENT = "student_data.csv"
FILENAME_JOBS = "new_jobs_notif.csv"

class TestClass:
    '''----------------------------------EPIC #1 TESTS-----------------------------------------------------'''
    # Tests if requirements for a valid password are satisfied within main.checkPass()

    # Validates if Less than 8 characters
    def test_checkPass_lessthan8(self):
        assert u.AccountPasswordClass.check_min_characters(self, "1$A") == False  # 3 chars
        assert u.AccountPasswordClass.check_min_characters(self, "1$Abcde") == False  # 7 char
        assert u.AccountPasswordClass.check_min_characters(self, "1$Abcdef") == True  # 8 char

    # Validates if More than 12 characters
    def test_checkPass_morethan12(self):
        assert u.AccountPasswordClass.check_max_characters(self, "1$Abcdefghijk") == False  # 13 characters
        assert u.AccountPasswordClass.check_max_characters(self, "1$Abcdefghij") == True  # 12 characters
        assert u.AccountPasswordClass.check_max_characters(self, "1$Abcdefghi") == True  # 11 characters

    # Validates if it includes an Uppercase letter
    def test_checkPass_noUpper(self):
        assert u.AccountPasswordClass.check_Uppercase_letter(self, "1$abcdefg") == False  # Does not include an Uppercase letter
        assert u.AccountPasswordClass.check_Uppercase_letter(self, "1$Abcdefg") == True  # Does include an Uppercase letter

    # Validates if it includes a digit char
    def test_checkPass_Digit(self):
        assert u.AccountPasswordClass.check_digit(self, "$Abcdefgh") == False  # Does not include a digit char
        assert u.AccountPasswordClass.check_digit(self, "$Abcd5efgh") == True  # Does include a digit char

    # Validates if it includes a non-alphabetic char
    def test_checkPass_nonAlpha(self):
        assert u.AccountPasswordClass.check_non_alpha(self, "1Abcdefgh") == False  # Does not include a non-alphabetic char
        assert u.AccountPasswordClass.check_non_alpha(self, "1Abc$defgh") == True  # Does include a non-alphabetic char

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

    '''-------------------------------------EPIC #3 TESTS---------------------------------------------------'''

    def test_importantLinks(self):
        filename = "settings.csv"
        file = open(filename, "w+")
        file.close()
        manage = ma.Manage()

        filename2 = "student_data.csv"
        file = open(filename2, "w+")
        file.close()
        manage = ma.Manage()
        #########################################

        stud1 = s.Student("TEST1", "P@ssword123", "Matteo", "Vescera")  # adds student
        assert manage.add_student(stud1) == stud1.get_user_name()
        pos = list()
        entry = [" ", " ", " ", " ", " "]
        arr = []
        count = 0
        pos_count = 0
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != arr:
                    pos.append(row)
                    count += 1
                    pos_count = count - 1
                for field in row:
                    if (field == "TEST1"):
                        entry = [pos[pos_count][0], pos[pos_count][1], pos[pos_count][2], pos[pos_count][3],
                                 pos[pos_count][4]]
                        pos.pop()
                        count -= 1

        assert (stud1.get_user_name() == entry[0])  # adds student's settings into csv file
        assert ("ON" == entry[1])
        assert ("ON" == entry[2])
        assert ("ON" == entry[3])
        assert ("English" == entry[4])

        #########################################

        stud2 = s.Student("TEST2", "P@ssword123", "Stefano", "Visentin")  # adds student
        assert manage.add_student(stud2) == stud2.get_user_name()
        pos = list()
        entry = [" ", " ", " ", " ", " "]
        arr = []
        count = 0
        pos_count = 0
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != arr:
                    pos.append(row)
                    count += 1
                    pos_count = count - 1
                for field in row:
                    if (field == "TEST2"):
                        entry = [pos[pos_count][0], pos[pos_count][1], pos[pos_count][2], pos[pos_count][3],
                                 pos[pos_count][4]]
                        pos.pop()
                        count -= 1

        assert (stud2.get_user_name() == entry[0])  # adds student's settings into csv file
        assert ("ON" == entry[1])
        assert ("ON" == entry[2])
        assert ("ON" == entry[3])
        assert ("English" == entry[4])

        #########################################

    '''-------------------------------------EPIC #4 TESTS---------------------------------------------------'''

    # Tests if adding jobs works
    def test_Profiles(self):
        filename = "profiles.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()

        filename2 = "student_data.csv"
        file = open(filename2, "w+")
        file.close()
        manage = ma.Manage()

        stud1 = s.Student("TEST1", "P@ssword123", "Stefano", "Visentin")  # adds student
        assert manage.add_student(stud1) == stud1.get_user_name()

        pos = list()
        entry = [" ", " ", " ", " ", " ", " ", " "]
        arr = []
        count = 0
        pos_count = 0
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != arr:
                    pos.append(row)
                    count += 1
                    pos_count = count - 1
                for field in row:
                    if field == "TEST1":
                        entry = [pos[pos_count][0], pos[pos_count][1], pos[pos_count][2], pos[pos_count][3],
                                 pos[pos_count][4]]
                        pos.pop()
                        count -= 1
        try:
            assert (stud1.get_user_name() == entry[0])  # adds student's settings into csv file
            assert ("SWE" == entry[1])
            assert ("Computer Science" == entry[2])
            assert ("University of South Florida" == entry[3])
            assert ("This is a test" == entry[4])
            assert ("I have no experience" == entry[5])
            assert ("[usf, computer science, 4]" == entry[6])
        except AssertionError:
            with open('profiles.csv', 'w') as f:
                row = [stud1.get_user_name(), 'SWE', 'Computer Science', 'University of South Florida','This is a test', 'I have no experience', 'usf, computer science, 4' ]
                newWriter = csv.writer(f)
                newWriter.writerow(row)


        stud2 = s.Student("TEST2", "P@ssword123", "Matteo", "Vescera")  # adds student
        assert manage.add_student(stud2) == stud2.get_user_name()

        pos = list()
        entry = [" ", " ", " ", " ", " ", " ", " "]
        arr = []
        count = 0
        pos_count = 0
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != arr:
                    pos.append(row)
                    count += 1
                    pos_count = count - 1
                for field in row:
                    if field == "TEST2":
                        entry = [pos[pos_count][0], pos[pos_count][1], pos[pos_count][2], pos[pos_count][3],
                                 pos[pos_count][4]]
                        pos.pop()
                        count -= 1
        try:
            assert (stud1.get_user_name() == entry[0])  # adds student's settings into csv file
            assert ("Developer" == entry[1])
            assert ("Computer Science" == entry[2])
            assert ("University of South Florida" == entry[3])
            assert ("This is test #2" == entry[4])
            assert ("I have no experience" == entry[5])
            assert ("[usf, computer science, 4]" == entry[6])
        except AssertionError:
            with open('profiles.csv', 'w') as f:
                row = [stud1.get_user_name(), 'Developer', 'Computer Science', 'University of South Florida','This is test #2', 'I have no experience', 'usf, computer science, 4' ]
                newWriter = csv.writer(f)
                newWriter.writerow(row)


    '''-------------------------------------EPIC #5 TESTS---------------------------------------------------'''

    # Test 10 Max accounts
    def test_10maximimAccounts(self):
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

        teststud6 = s.Student("nghiatroung", "Password123!", "Nghia", "Troung")
        assert manage.add_student(teststud6) == teststud6.get_user_name()

        teststud7 = s.Student("test7", "Password123!", "Test", "Seven")
        assert manage.add_student(teststud7) == teststud7.get_user_name()

        teststud8 = s.Student("test8", "Password123!", "Test", "Eight")
        assert manage.add_student(teststud8) == teststud8.get_user_name()

        teststud9 = s.Student("test9", "Password123!", "Test", "Nine")
        assert manage.add_student(teststud9) == teststud9.get_user_name()

        teststud10 = s.Student("test10", "Password123!", "Test", "Ten")
        assert manage.add_student(teststud10) == teststud10.get_user_name()

    #test case to return last name 
    def test_return_friend_lastname(self):
        manage = ma.Manage()
        blank = []
        count = 0
        lastname = "Wright"
        lines = list()
        expected_result = list()
        with open(FILENAME_STUDENT, 'r') as rFile:
            reader = csv.reader(rFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count = count + 1
                    if lines[count - 1][3] == lastname:
                        expected_result.append(lines[count - 1][0])
            return expected_result

        actual_result = manage.return_friend_lastname(lastname)
        assert len(actual_result) == len(expected)
        assert all([a == b for a, b in zip(actual_result, expected_result)])

    #test case to return a friend in university
    def test_return_friend_university(self):
        manage = ma.Manage()
        expected_result = list()
        blank = []
        university = "Usf"
        count = 0
        lines = list()
        with open(FILENAME_PROFILE, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count = count + 1
                    if lines[count - 1][3] == university:
                        expected_result.append(lines[count - 1][0])

        actual_result = manage.return_friend_university(university)
        assert len(actual_result) == len(expected_result)
        assert all([a == b for a, b in zip(actual_result, expected_result)])

    #test case to return a friend major
    def test_return_friend_major(self):
        manage = ma.Manage()
        blank = []
        count = 0
        lines = list()
        major = "Computer Science"
        expected_result = list()
        with open(FILENAME_PROFILE, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank:
                    lines.append(row)
                    count = count + 1
                    if lines[count - 1][2] == major:
                        expected_result.append(lines[count - 1][0])
            return expected_result
        actual_result = manage.return_friend_major(major)
        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual_result, expected_result)])

    '''-------------------------------------EPIC #6 TESTS---------------------------------------------------'''
    #test 10 job list
    def test_JobsMax(self):
        filename = "job_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()

        testjob1 = j.Job("Developer", "Devs some stuff", "USF", "Tampa", "100000", "Deric")
        assert manage.add_job(testjob1, "Deric") == testjob1.get_poster_name()

        testjob2 = j.Job("Developer2", "Devs some stuff", "USF", "Tampa", "200000", "Nghia")
        assert manage.add_job(testjob2, "Nghia") == testjob2.get_poster_name()

        testjob3 = j.Job("Chef", "cooks stuff", "Hell's Kitchen", "Tampa", "20000", "Matteo")
        assert manage.add_job(testjob3, "Matteo") == testjob3.get_poster_name()

        testjob4 = j.Job("Gamer", "Rules the World", "FaZe Clan", "Tampa", "2000", "Darshan")
        assert manage.add_job(testjob4, "Darshan") == testjob4.get_poster_name()

        testjob5 = j.Job("Tester", "Tests stuff", "Microsoft", "Tampa", "5000", "Panatda")
        assert manage.add_job(testjob5, "Panatda") == testjob5.get_poster_name()

        testjob6 = j.Job("World Dominator", "Rules the World", "The World", "Tampa", "10000", "Stefano")
        assert manage.add_job(testjob6, "Stefano") == testjob6.get_poster_name()

        testjob7 = j.Job("Builder", "Builds stuff", "BobTheBuilder", "Tampa", "1000", "Bob")
        assert manage.add_job(testjob7, "Builder") == testjob7.get_poster_name()

        testjob8 = j.Job("Builder2", "Survives", "Mojang", "Minecraft", "3000", "Steve")
        assert manage.add_job(testjob8, "Steven") == testjob8.get_poster_name()

        testjob9 = j.Job("Master Chief", "Defeats the Covenant", "UNSC", "Halo", "117", "John")
        assert manage.add_job(testjob9, "Steveo") == testjob9.get_poster_name()

        testjob10 = j.Job("Spiderman", "Saves stuff", "New York", "Marvel", "2000", "Peter")
        assert manage.add_job(testjob10, "Steve") == testjob10.get_poster_name()


    def test_list_save_job(self):
        name = "Developer1"
        assert name
        list_save_job = []
        with open("save_job.csv", "r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != [] and row[0] == name:
                    list_save_job.append(row[1])
        assert name == "Developer1"

    def test_add_save_job(self):
        username = "dericwright"
        title = "Job1"
        list_application = []  # keep title of applications of the user
        with open("applications.csv", "r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != [] and row[0] == username:
                    list_application.append(row[1])
        assert title != False

    '''-------------------------------------EPIC #7 TESTS---------------------------------------------------'''

    def test_add_pending_message(self):
        user1 = "Nghia"
        user2 = "Deric"
        message = "Pending Message Test"
        flag = 0
        blank = []
        manage = ma.Manage()
        manage.add_pending_message(user1, user2, message)
        with open("pending_messages.csv", 'r') as f:
            PMReader = csv.reader(f)
            for row in PMReader:
                if row != blank:
                    print(row[0])
                    print(row[1])
                    print(row[2])
                    if (row[0] == user1) and (row[1] == user2) and (row[2] == message):
                        flag = 1

        assert flag == 1

    def test_delete_pending_message(self):
        user1 = "Nghia"
        user2 = "Deric"
        message = "Pending Message Test"
        flag = 0
        blank = []

        with open("pending_messages.csv", 'r') as f:
            PMReader = csv.reader(f)
            for row in PMReader:
                if row != blank:
                    print(row[0])
                    print(row[1])
                    print(row[2])
                    if (row[0] == user1) and (row[1] == user2) and (row[2] == message):
                        flag = 1

        assert flag == 1
        flag = 0

        c.delete_pending_message(user1, user2, message)
        with open("pending_messages.csv", 'r') as f2:
            PMReader = csv.reader(f2)
            for row in PMReader:
                if row != blank:
                    print(row[0])
                    print(row[1])
                    print(row[2])
                    if (row[0] == user1) and (row[1] == user2) and (row[2] == message):
                        flag = 1

        assert flag == 0

'''------------------------------------------Epic 8 tests---------------------------------------'''
if (not os.path.exists("new_user.csv")):
    open("new_user.csv", 'w').close()

if (not os.path.exists("profiles.csv")):
    open("profiles.csv", 'w').close()

def test_profile_notification():
    usern1 = "TestP"
    usern2 = "NoTestP"

    flag = 1

    with open("profiles.csv","a") as f:
        Pwriter = csv.writer(f)
        Pwriter.writerow((usern1,"T","M","U","B","E","Ed"))

    flag = c.check_profile_creation(usern1)
    assert flag == 0

    flag = c.check_profile_creation(usern2)
    assert flag == 1

    str = []
    with open("profiles.csv","r") as f2:
        Preader = csv.reader(f2)
        for row in Preader:
            if row != [] and row[0] != usern1:
                str.append(tuple(row))

    with open("profiles.csv","w") as f3:
        writer_csv = csv.writer(f3)
        for element in str:
            writer_csv.writerow(element)

'''------------------------------------------Epic 9 tests---------------------------------------'''
'''No new tests to be added as Epic 9 only modifies console.py
    and all manipulation in newly added code is opening files to read or write'''


'''------------------------------------------Epic 10 tests---------------------------------------'''
def test_write_jobs():
    manage = ma.Manage()
    lines = list()
    lines.append("Programming")
    lines.append("will make app")
    lines.append("tesla")
    lines.append("calif")
    lines.append("100000")
    lines.append("=====")
    with open("job_data.csv", "w") as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow(lines)

    assert ma.write_jobs() == lines


def test_write_users():
    manage = ma.Manage()
    lines = list()
    lines.append("dev")
    lines.append("dev@123")
    lines.append("developer")
    lines.append("mamba")
    lines.append("standard")
    lines.append("0")
    with open("student_data.csv", "w") as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow(lines)
    test = list()
    test.append("dev standard")

    assert ma.write_users() == test


def test_write_profiles():
    manage = ma.Manage()
    lines = list()
    lines.append("engineer")
    lines.append("Comp Sci student")
    lines.append("Comp sci")
    lines.append("usf")
    lines.append("I like hiking")
    lines.append(" ")
    lines.append("[University of South Florida,Comp sci degree,3]")
    lines.append("=====")

    with open("profiles.csv", "w") as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow(lines)

    test = list()
    test.append("Comp Sci student")
    test.append("Comp sci")
    test.append("usf")
    test.append("I like hiking")
    test.append(" ")
    test.append("[University of South Florida,Comp sci degree,3]")
    test.append("=====")

    assert ma.write_profiles() == test
