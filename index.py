import sys


def main():
    option = sys.argv[1].lower()

    if option == "/name":
        print("My name is Talha Ali but my preferred name is T. This is my senior year.")

    elif option == "/why":
        print("To sum it all up, I got into CS because I was and still am passionate to learn more about what goes on behind the scenes of the mobile apps we use, the video games we play, and other entertainment media we consume.")

    elif option == "/what":
        print("After graduating, I am keeping myself flexible to start small anywhere I can, just to get my foot in the door. As a long term goal, I'd love to work in either healthcare or in the entertainment industry")
    
    elif option == "/fact":
        print("I can flawlessly play almost every Guitar Hero song on expert difficulty. (Seriously, I grew up on that stuff)")

    else:
        print("Sorry, try another option?")


if __name__ == "__main__":
    main()
