import time
import console

def main():  # controller of program
    
    story = open("success_story.txt", "r")
    print()
    print()
    print(story.read())
    print()
    print()
    time.sleep(2)
    
    console.Welcome_Page()

if __name__ == "__main__":
    # execute only if run as a script
    main()
