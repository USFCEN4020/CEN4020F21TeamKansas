import manage as m
import console
import utility
import csv

FILENAME_STUDENT = "student_data.csv"
FILENAME_SETTINGS = "settings.csv"
FILENAME_PROFILE = "profiles.csv"
FILENAME_FRIEND = "friends.csv"
FILENAME_REQUEST = "requests.csv"
blank_string = " "


def search_friend(sname):
    manage = m.Manage()
    sent = 0
    decision = 0

    print()
    while sent == 0:
        results = list()
        entry = [" ", " ", " ", " "]
        print("Friend Search")
        print("Select one of the below options:")
        print("1. Search by Last Name")
        print("2. Search by University")
        print("3. Search by Major")
        print("4. Go back to previous screen: Log-in Screen")
        decision = input("Your selection: ")
        # check that user provided acceptable input
        decision = utility.checkUserInput(decision, 1, 4)

        if (decision == "1"):
            lname = input("Enter Last Name: ")
            print()
            names = list()
            names = manage.return_friend_lastname(lname)
            for uname in names:
                lastname_results = list()
                lastname_results = manage.return_students(uname)
                for entry in lastname_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_friend_requests(sname, names)
        elif (decision == "2"):
            univ = input("Enter University: ")
            print()
            names = manage.return_friend_university(univ)
            for uname in names:
                lastname_results = list()
                lastname_results = manage.return_students(uname)
                for entry in lastname_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_friend_requests(sname, names)
        elif (decision == "3"):
            major = input("Enter Major: ")
            print()
            names = manage.return_friend_major(major)
            for uname in names:
                lastname_results = list()
                lastname_results = manage.return_students(uname)
                for entry in lastname_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_friend_requests(sname, names)
        elif (decision == "4"):
            console.Login_Page(sname)


def check_requests(sign_name):
    manage = m.Manage()
    blank = []
    count = 0
    count2 = 0
    request = 0
    addUser1 = list()
    addUser2 = list()
    superLines = list()
    lines = list()
    lines2 = list()

    with open(FILENAME_REQUEST, 'r') as readFile:
        reader2 = csv.reader(readFile)
        for row2 in reader2:
            if row2 != blank:
                lines2.append(row2)
                count2 += 1
                if lines2[count2 - 1][1] == sign_name:
                    request += 1

    if request > 0:

        print("You have one or more pending friend requests. Do you wish to review them?")
        print("Enter '1' if yes and '0' if no")
        decision = input("Your selection: ")
        # check that user provided acceptable input
        decision  = utility.checkUserInput(decision , 0, 1)
        if decision == "1":
            with open(FILENAME_REQUEST, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row != blank:
                        if (row[1] != sign_name):
                            superLines.append(row)

            with open(FILENAME_REQUEST, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row != blank:
                        lines.append(row)
                        count = count + 1
                        if lines[count - 1][1] == sign_name:
                            print()
                            print("You have a pending friend request from " + lines[count - 1][0])
                            print("Do you accept it? Enter '1' for yes and '0' for no")
                            accept = input("Your selection: ")
                            accept = utility.checkUserInput(accept, 0, 1)
                            if accept == "1":
                                addUser1.append(sign_name)
                                addUser2.append(lines[count - 1][0])

            i = 0
            while i < len(addUser1):
                manage.add_friend(addUser1[i], addUser2[i])
                i = i + 1

            with open(FILENAME_REQUEST, "w") as writeFile:
                writer = csv.writer(writeFile)
                for line in superLines:
                    writer.writerow(line)

def show_connection(name):
    print("\nSelect one of the below options:")
    print("1. Show Friends List")
    print("2. Check Friend Requests")
    print("3. Display Friend Profile")
    print("4. Remove Friend")
    print("5. Return to Main Menu")
    decision = input("Your selection: ")
    print()

    if decision == "1":
        fri_list(name)
    elif decision == "2":
        show_requests(name)
    elif decision == "3":
        fri_pro(name)
    elif decision == "4":
        remo_fri(name)
    elif decision == "5":
        console.Login_Page(name)


def show_requests(name):
    blank = []
    count = 0
    requests = 0
    lines = list()

    with open(FILENAME_REQUEST, 'r') as readFile:
        read = csv.reader(readFile)
        for row2 in read:
            if row2 != blank:
                lines.append(row2)
                count = count + 1
                if lines[count-1][1] == name:
                    requests = requests + 1
    print()
    if requests == 0:
        print("No Pending Friend Requests")
    elif requests > 0:
        print("Your pending friend requests are: ")
        with open(FILENAME_REQUEST, "r") as file:
            req_reader = csv.reader(file)
            data = list(req_reader)
        with open(FILENAME_STUDENT, "r") as sfile:
            ureader = csv.reader(sfile)
            user = list(ureader)
        for request in data:
            if name in request:
                index = request.index(name)
                if index == 0:
                    fri = 1
                elif index == 1:
                    fri = 0
                uname = request[fri]
                num = -1
                for i in user:
                    num += 1
                    if num % 2 == 0:
                        if i[0] == uname:
                            print(i[2]+' '+i[3])
                            break
    show_connection(name)


def fri_list(name):
    with open(FILENAME_FRIEND, 'r') as f:
        checker = len(f.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        # go to log in screen
        console.Login_Page(name)
    else:
        with open('student_data.csv', newline='') as f2:
            UserR = csv.reader(f2)
            UserN = list(UserR)
        print("Current Friends: ")
        with open("friends.csv", newline='') as f3:
            FriendR = csv.reader(f3)
            FriendD = list(FriendR)
        for user in FriendD:
            if name in user:
                ind = user.index(name)
                if ind == 0:
                    friend = 1
                    Uname = user[friend]
                    number = -1
                    for i in UserN:
                        number = number + 1
                        if (number % 2 == 0):
                            if i[0] == Uname:
                                print(i[2] + ' ' + i[3])
                                break
    show_connection(name)


def remo_fri(name):
    with open("friends.csv", 'r') as f:
        checker = len(f.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        console.Login_Page(name)
    else:
        UserN = ''
        with open('student_data.csv', newline='') as f2:
            UserR = csv.reader(f2)
            UserD = list(UserR)
        RF = input("Enter First name: ")
        RL = input("Enter Last name: ")
        num = -1
        for User in UserD:
            num = num + 1
            if (num % 2 == 0):
                if (User[2] == RF and User[3] == RL):
                    UserN = User[0]  # username of the student
        if (UserN == ''):
            print("User not found.")
            show_connection(name)
        with open("friends.csv", newline='') as f3:
            FriendR = csv.reader(f3)
            FriendD = list(FriendR)

        with open("friends.csv", "w", newline="") as f4:
            write = csv.writer(f4)
            num = -1
            for pair in FriendD:
                num = num + 1
                if (num % 2 == 0):
                    if (pair[0] == name and pair[1] == UserN) or (pair[0] == UserN and pair[1] == name):
                        continue
                    else:
                        write.writerow((pair[0], pair[1]))
                        write.writerow("")
        print("Friend removed.")
    show_connection(name)


def fri_pro(name):
    UserN = ''
    with open("friends.csv", 'r') as f:
        checker = len(f.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        # go to log in screen
        console.Login_Page(name)
    else:
        with open('student_data.csv', newline='') as f2:
            UserR = csv.reader(f2)
            UserNS = list(UserR)
        print("Your Current Friends: ")
        with open("friends.csv", newline='') as f3:
            FriendR = csv.reader(f3)
            FriendD = list(FriendR)
        for User in FriendD:  # checks all friends
            if name in User:  # if user is found in a friend pairing
                index = User.index(name)
                if index == 0:
                    fri = 1
                    UN = User[fri]
                    num = -1
                    for i in UserNS:  # searches through student data for first and last name
                        num = num + 1
                        if (num % 2 == 0):
                            if i[0] == UN:
                                print(i[2] + ' ' + i[3])
    print("Enter your friend's name to view their profile:")
    FirstN = input('First name: ')
    LastN = input('Last name: ')

    with open("student_data.csv", newline='') as f4:       #finds the username of the friend
        UserR = csv.reader(f4)
        UserD = list(UserR)
    num = -1
    for User in UserD:
        num = num + 1
        if(num%2==0):
            if(User[2]==FirstN and User[3]==LastN):
                UserN = User[0]
    if(UserN==''):
        print("User not found. ")
        show_connection(name)

    man = m.Manage()
    man.view_profile(UserN)
    f4.close()
    show_connection(name)