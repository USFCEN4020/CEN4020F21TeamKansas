import manage as m
import console
import utility
import csv

FILENAME_STUDENT = "student_data.csv"
FILENAME_FRIEND = "friends.csv"
FILENAME_REQUEST = "requests.csv"
blank_string = " "


def search_friend(SearchName):
    manage = m.Manage()
    request = 0
    decision = 0

    print()
    while request == 0:
        results = list()
        entry = [" ", " ", " ", " "]
        print("\nSearch Friend")
        print("Select one of the options below:")
        print("1. Search by Last Name")
        print("2. Search by University")
        print("3. Search by Major")
        print("4. Return to Main Menu")
        decision = input("Your selection: ")
        # check that user provided acceptable input
        decision = utility.checkUserInput(decision, 1, 4)

        if decision == "1":
            lastname = input("Enter Last Name: ")
            print()
            names = list()
            names = manage.return_friend_lastname(lastname)
            for username in names:
                lastname_results = list()
                lastname_results = manage.return_students(username)
                for entry in lastname_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_friend_requests(SearchName, names)
        elif decision == "2":
            univ = input("Enter University: ")
            print()
            names = manage.return_friend_university(univ)
            for username in names:
                lastname_results = list()
                lastname_results = manage.return_students(username)
                for entry in lastname_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_friend_requests(SearchName, names)
        elif decision == "3":
            major = input("Enter Major: ")
            print()
            names = manage.return_friend_major(major)
            for username in names:
                lastname_results = list()
                lastname_results = manage.return_students(username)
                for entry in lastname_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_friend_requests(SearchName, names)
        elif decision == "4":
            console.Login_Page(SearchName)


def check_requests(RequestName):
    manage = m.Manage()
    blank = []
    count1 = 0
    count2 = 0
    request = 0
    add1 = list()
    add2 = list()
    lines = list()
    lines1 = list()
    lines2 = list()

    with open(FILENAME_REQUEST, 'r') as rFile:
        r2 = csv.reader(rFile)
        for row2 in r2:
            if row2 != blank:
                lines2.append(row2)
                count2 += 1
                if lines2[count2 - 1][1] == RequestName:
                    request += 1

    if request > 0:

        print("You have one or more pending friend requests. Do you want to review them?")
        print("1. Yes\t0. No")
        decision = input("Your selection: ")
        # check that user provided acceptable input
        decision = utility.checkUserInput(decision, 0, 1)
        if decision == "1":
            with open(FILENAME_REQUEST, 'r') as rFile:
                read1 = csv.reader(rFile)
                for row1 in read1:
                    if row1 != blank:
                        if row1[1] != RequestName:
                            lines.append(row1)

            with open(FILENAME_REQUEST, 'r') as rFile:
                read2 = csv.reader(rFile)
                for row1 in read2:
                    if row1 != blank:
                        lines1.append(row1)
                        count1 += 1
                        if lines1[count1 - 1][1] == RequestName:
                            print("\nYou have a pending friend request from " + lines1[count1 - 1][0])
                            print("Accept request? \n1. Yes\n0. No")
                            accept = input("")
                            accept = utility.checkUserInput(accept, 0, 1)
                            if accept == "1":
                                add1.append(RequestName)
                                add2.append(lines1[count1 - 1][0])

            i = 0
            while i < len(add1):
                manage.add_friend(add1[i], add2[i])
                i += 1

            with open(FILENAME_REQUEST, "w") as wFile:
                write = csv.writer(wFile)
                for line in lines:
                    write.writerow(line)


def show_connection(name):
    print("\nFriends:")
    print("Select one of the options below:")
    print("1. Friends List")
    print("2. Friend Requests")
    print("3. Friend Profile")
    print("4. Remove Friend")
    print("5. Return to Main Menu")
    decision = input("Your selection: ")
    print()

    if decision == "1":
        fri_list(name)
    elif decision == "2":
        show_friend_requests(name)
    elif decision == "3":
        fri_pro(name)
    elif decision == "4":
        remo_fri(name)
    elif decision == "5":
        console.Login_Page(name)


def show_friend_requests(name):
    newlist = []
    count = 0
    requests = 0
    lines = list()

    with open(FILENAME_REQUEST, 'r') as rFile:
        read1 = csv.reader(rFile)
        for row2 in read1:
            if row2 != newlist:
                lines.append(row2)
                count += 1
                if lines[count-1][1] == name:
                    requests += 1
    print()
    if requests == 0:
        print("No Pending Friend Requests")
    elif requests > 0:
        print("Your pending friend requests are: ")
        with open(FILENAME_REQUEST, "r") as file:
            read1 = csv.reader(file)
            data = list(read1)
        with open(FILENAME_STUDENT, "r") as sfile:
            read2 = csv.reader(sfile)
            user = list(read2)
        for request in data:
            if name in request:
                index = request.index(name)
                if index == 0:
                    friend = 1
                elif index == 1:
                    friend = 0
                uname = request[friend]
                num = -1
                for i in user:
                    num += 1
                    if num % 2 == 0:
                        if i[0] == uname:
                            print(i[2]+' '+i[3])
                            break
    show_connection(name)


def fri_list(name):
    with open(FILENAME_FRIEND, 'r') as file:
        checker = len(file.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        console.Login_Page(name)
    else:
        with open('student_data.csv', newline='') as file2:
            UserR = csv.reader(file2)
            UserN = list(UserR)
        print("Current Friends: ")
        with open("friends.csv", newline='') as file3:
            FriendR = csv.reader(file3)
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
    with open("friends.csv", 'r') as file:
        checker = len(file.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to Main Menu.")
        console.Login_Page(name)
    else:
        UserName = ''
        with open('student_data.csv', newline='') as file2:
            UserR = csv.reader(file2)
            UserD = list(UserR)
        remove_firstname = input("Enter First name: ")
        remove_lastname = input("Enter Last name: ")
        number = -1
        for User in UserD:
            number = number + 1
            if (number % 2 == 0):
                if (User[2] == remove_firstname and User[3] == remove_lastname):
                    UserName = User[0]
        if (UserName == ''):
            print("User not found.")
            show_connection(name)
        with open("friends.csv", newline='') as file3:
            FriendR = csv.reader(file3)
            FriendD = list(FriendR)

        with open("friends.csv", "w", newline="") as f4:
            write = csv.writer(f4)
            number = -1
            for p in FriendD:
                number = number + 1
                if (number % 2 == 0):
                    if (p[0] == name and p[1] == UserName) or (p[0] == UserName and p[1] == name):
                        continue
                    else:
                        write.writerow((p[0], p[1]))
                        write.writerow("")
        print("Friend Eliminated!")
    show_connection(name)


def fri_pro(name):
    UserName = ''
    with open("friends.csv", 'r') as file:
        checker = len(file.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        console.Login_Page(name)
    else:
        with open('student_data.csv', newline='') as file2:
            UserR = csv.reader(file2)
            UserNS = list(UserR)
        print("Your Current Friends: ")
        with open("friends.csv", newline='') as file3:
            FriendR = csv.reader(file3)
            FriendD = list(FriendR)
        for User in FriendD:
            if name in User:
                ind = User.index(name)
                if ind == 0:
                    fri = 1
                    UN = User[fri]
                    number = -1
                    for i in UserNS:
                        number = number + 1
                        if (number % 2 == 0):
                            if i[0] == UN:
                                print(i[2] + ' ' + i[3])
    print("Enter your friend's name to view their profile:")
    FirstName = input('First name: ')
    LastName = input('Last name: ')

    with open("student_data.csv", newline='') as file4:
        UserR = csv.reader(file4)
        UserD = list(UserR)
    number = -1
    for User in UserD:
        number = number + 1
        if(number%2==0):
            if(User[2]==FirstName and User[3]==LastName):
                UserName = User[0]
    if UserName == '':
        print("User not found. ")
        show_connection(name)

    man = m.Manage()
    man.view_profile(UserName)
    file4.close()
    show_connection(name)