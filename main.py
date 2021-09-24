import time
import console

def main():  # controller of program
    
    story = open("success_story.txt", "r")
    print()
    print()
    print(story.read())
    print()
    print()
    time.sleep(3)
    print("Welcome to InCollege! An application designed for college students hoping to connect with other college students in effort to land a job!")
    print("")
    print("Are you a new user? Or do you already have an account? Select an option below")
    decision = input("1. Create an account\n"
    "2. Login\n"
    "3. Find someone you know \n"
    "4. Play the video \n"
    "0. Exit\nYour selection: ")

    console.welcome(decision)

if __name__ == "__main__":
    # execute only if run as a script
    main()
