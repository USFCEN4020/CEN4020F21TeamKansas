import console
import manage as m
import utility
import csv


def search_friend(sname):
    manage = m.Manage()
    sent = 0
    choice = 0

    while sent == 0:
        results = list()
        entry = [" ", " ", " ", " ", " "]
        print("Select one of the options to search for friend")
        print("1. Search by last name")
        print("2. Search by University")
        print("3. Search by Major")
        print("4. Return to previous page")
        choice = input("Your selection: ")

        # check user input
        choice = utility.checkUserInput(choice, 1, 4)

        if choice == "1":
            last = input("Enter last name: ")
            names = list()
            names = manage.return_names(last)
            for uname in names:
                partial_results = list()
                partial_results = manage.return_students(uname)
                for entry in partial_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_requests(sname, names)
        elif choice == "2":
            univ = input("Enter University: ")
            print()
            names = manage.return_names_uni(univ)
            for uname in names:
                partial_results = list()
                partial_results = manage.return_students(uname)
                for entry in partial_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_requests(sname, names)
        elif choice == "3":
            major = input("Enter Major: ")
            print()
            names = manage.return_names_major(major)
            for uname in names:
                partial_results = list()
                partial_results = manage.return_students(uname)
                for entry in partial_results:
                    results.append(entry)
            for row in results:
                print(row[0] + ": " + row[2] + " " + row[3])
            manage.send_requests(sname, names)
        elif choice == "4":
            sent = 1


def check_requests(sname):
    manage = m.Manage()
    blank = []
    count1 = 0
    count2 = 0
    req = 0
    add1 = list()
    add2 = list()
    super_lines = list()
    lines1 = list()
    lines2 = list()

    with open(console.FILENAME_REQUEST, 'r') as readFile:
        reader2 = csv.reader(readFile)
        for row2 in reader2:
            if row2 != blank:
                lines2.append(row2)
                count2 += 1
                if lines2[count2 - 1][1] == sname:
                    req += 1

    if req > 0:
        print("You have one or more pending friend requests. Review them?")
        print("0. No")
        print("1. Yes")
        choice = input("Your selection: ")
        # check that user provided acceptable input
        choice = utility.checkUserInput(choice, 0, 1)
        if choice == "1":
            with open(console.FILENAME_REQUEST, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row != blank:
                        if row[1] != sname:
                            super_lines.append(row)

            with open(console.FILENAME_REQUEST, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row != blank:
                        lines1.append(row)
                        count1 += 1
                        if lines1[count1 - 1][1] == sname:
                            print()
                            print("You have a pending friend request from " + lines1[count1 - 1][0])
                            print("Do you accept it? Enter '1' for yes and '0' for no")
                            accept = input("Your selection: ")
                            accept = utility.checkUserInput(accept, 0, 1)
                            if accept == "1":
                                add1.append(sname)
                                add2.append(lines1[count1 - 1][0])

            i = 0
            while i < len(add1):
                manage.add_friend(add1[i], add2[i])
                i = i + 1

            with open(console.FILENAME_REQUEST, "w") as writeFile:
                writer = csv.writer(writeFile)
                for line in super_lines:
                    writer.writerow(line)


def show_connection(name):
    print("\nSelect one of the below options:")
    print("1. Show Friends List")
    print("2. Check Friend Requests")
    print("3. Display Friend Profile")
    print("4. Remove Friend")
    print("5. Return to Main Menu")
    choice = input("Your selection: ")
    print()

    if choice == "1":
        fri_list(name)
    elif choice == "2":
        show_requests(name)
    elif choice == "3":
        fri_pro(name)
    elif (choice == "4"):
        remo_fri(name)
    elif (choice == "5"):
        console.Login_Page(name)


def show_requests(name):
    blank = []
    count = 0
    requests = 0
    lines = list()

    with open(console.FILENAME_REQUEST, 'r') as readFile:
        read = csv.reader(readFile)
        for row2 in read:
            if row2 != blank:
                lines.append(row2)
                count += 1
                if lines[count-1][1] == name:
                    requests += 1
    print()
    if requests == 0:
        print("No Pending Friend Requests")
    elif requests > 0:
        print("Your pending friend requests are: ")
        with open(console.FILENAME_REQUEST, "r") as file:
            req_reader = csv.reader(file)
            data = list(req_reader)
        with open(console.FILENAME_STUDENT, "r") as sfile:
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
    with open("friends.csv", 'r') as f:
        checker = len(f.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        # go to log in screen
    else:
        with open('student_data.csv', newline=' ') as f2:
            UserR = csv.reader(f2)
            UserN = list(UserR)
        print("Current Friends: ")
        with open("friends.csv", newline=' ') as f3:
            FriendR = csv.reader(f3)
            FriendD = list(FriendR)
        for user in FriendD:
            if name in user:
                ind = user.index(name)
                if ind == 0:
                    friend = 1
                    UserN = user[friend]
                    number = -1
                    for i in UserN:
                        number = number + 1
                        if (number % 2 == 0):
                            if i[0] == UserN:
                                print(i[2] + ' ' + i[3])
                                break
    show_connection(name)


def remo_fri(name):
    with open("friends.csv", 'r') as f:
        checker = len(f.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        # go to log in screen
    else:
        UserN = ''
        with open('student_data.csv', newline='') as f2:
            UserR = csv.reader(f2)
            UserD = list(UserR)
        RF = input("What is the first name of the person you would like to remove? ")
        RL = input("What is the last name? ")
        num = -1
        for User in UserD:
            num = num + 1
            if (num % 2 == 0):
                if (User[2] == RF and User[3] == RL):
                    UserN = User[0]  # username of the student
        if (UserN == ''):
            print("User not found. Try again. ")
            remo_fri(name)
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
        print("Friendship eliminated, congratulations!")
    show_connection(name)


def fri_pro(name):
    UserN = ''
    with open("friends.csv", 'r') as f:
        checker = len(f.read().strip())
    if (checker == 0):
        print("Friends list empty. Returning to main menu")
        # go to log in screen
    else:
        with open('student_data.csv', newline=' ') as f2:
            UserR = csv.reader(f2)
            UserNS = list(UserR)
        print("Current Friends: ")
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
    print("Type in the first and last name of your friend to view their profile:")
    FirstN = input('Please input first name: ')
    LastN = input('Please input last name: ')

    with open("student_data.csv", newline='') as f4:       #finds the username of the friend
        UserR = csv.reader(f4)
        UserD = list(UserR)
    num = -1
    for User in UserD:
        num = num + 1
        if(num%2==0):
            if(User[2]==FirstN and User[3]==LastN):
                username = User[0]
    if(UserN==''):
        print("User not found. Try again. ")
        fri_pro(name)

    man = m.Manage()
    man.view_profile(UserN)
    f4.close()
    show_connection(name)