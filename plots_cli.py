
import plotter

def main():
# this funtion will ask the user to quit or not
    quit_x = input("Enter a command: ")
    z = quit_x.split(" ")

    if (quit_x == "stu"):
       student_average()

    if (quit_x == "avg"):
        print_average()

    if z[0] == str("quit"):
         quit()
         print("Goodbye!")

    else:
        try:
            if quit_x != str("quit"):
                print("   Failed input")
                print("   Enter a command or enter 'quit' to quit please: ")
                main()

        except:
           return




def quit():
    # asks the user if sure or not
    print("Are you sure?")
    yes = input("If yes enter Y:- ")
    if yes == str("Y"):
        return True
    else:
        return False


def student_average(a_string):

# a_string = "stu, filename, firstname, lastname"
   a_string = ["stu", "filename", "firstname", "lastname", plotter.plot(trace_plot=True)]
   try:
     if (a_string[4] == True):
      print("“Plot finished (window may be hidden).")

     if (a_string[4] == False):
      print("Plot failed (no such student)")


     if (a_string[0] == None):
         print("Usage: stu <filename> <first name> <last name>")
     if (a_string[1] == None):
         print("No such file: foo.csv")
     if (a_string[2] == None):
         print("Usage: stu <filename> <first name> <last name>")
     if (a_string[3] == None):
         print("Usage: stu <filename> <first name> <last name>")

   except:
       return


def print_average(b_string):
    b_string = ["avg","filename", "gradeitem"]
    try:
        if (b_string[0] == None):
            print("Usage: avg <filename> <grade item>")
        if (b_string[1] == None):
            print("Usage: avg <filename> <grade item>")
        if (b_string[2] == None):
            print("Usage: avg <filename> <grade item>")

        if (b_string[1] == None):
            print("No such file: foo.csv")

        if (b_string[2] != int()):
            print("Grade item must be a number")

    except:
        return









if __name__ == '__main__':
    main()

