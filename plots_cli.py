
def main():
# this funtion will ask the user to quit or not
    quit_x = input("Enter a command or 'quit' to quit. ")
    z = quit_x.split(" ")

    if quit_x[0] == str("quit"):
         quit("Y")
         print("Goodbye!")

    else:
        try:
            if quit_x != str("quit"):
                print("Enter a command or enter 'quit' to quit")
                main()

        except:
           return


def quit():
    print("Are you sure?")
    input("If yes enter Y")







if __name__ == '__main__':
    main()
