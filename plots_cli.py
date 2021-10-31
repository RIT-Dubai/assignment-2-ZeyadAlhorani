import csv
import plotter

def main():
# this funtion will ask the user to quit or not
    command = input(">> ")
    z = command.split()


    if (z[0] == "stu"):
       student_average(["stu",r'C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv','zeyad','bonita'])

    if (command == "avg"):
        print_average()

    if (command == "cavg"):
        class_average()

    if (command == "help"):
        help()

    if z[0] == str("quit"):
         quit()
         print("Goodbye!")

    else:
        try:
            if z[0] == str("quit"):
                quit()
                print("Goodbye!")

            #elif command != str("quit"):
                #print("   Failed input")
                #print("   Enter a command or enter 'quit' to quit please: ")
                #main()

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


def student_average(stu_string):
# a_string = "stu, filename, firstname, lastname"
   stu_string = ["stu",r"C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv", "Zeyad", "Bonita", plotter.plot(trace_plot=True)]
   namefile = [1]
   if len(stu_string) != 4:
       print("Usage: stu <filename> <first name> <last name>")

   if (stu_string[1] == None):
         print("No such file: foo.csv")

   else:
    try:
       with open(r"C:\Users\Zeyad\GCIS.123.600-assignment2-sample.csv") as namefile:
        csv_reader = csv.reader(namefile)
       fisrtname = stu_string[2]
       lastname = stu_string[3]
       row = []
       for row in csv_reader:
           while fisrtname in row:
               if lastname in row:
                   print(row)
                   plotter.init("my graph", "X-axis", "Y-axis")
    except:

     if (stu_string[4] == True):
       print("“Plot finished (window may be hidden).")
     #else:
       #stu_string[4] == False
       #print("Plot failed (no such student)")





def print_average(avg_string):
    avg_string = ["avg","filename", "gradeitem", plotter.plot_point("70", "98", "red")]

    if len(avg_string) != 4:
       print("Usage: stu <filename> <first name> <last name>")

    try:
        if (avg_string == True):
            print("Average:")
        if (avg_string[0] == None):
            print("Usage: avg <filename> <grade item>")
        if (avg_string[1] == None):
            print("Usage: avg <filename> <grade item>")
        if (avg_string[2] == None):
            print("Usage: avg <filename> <grade item>")

        if (avg_string[1] == None):
            print("No such file: foo.csv")

        if (avg_string[2] != int()):
            print("Grade item must be a number")

    except:
        return


def class_average(class_string):
    class_string = ["cavg", "filename", plotter.plot_data_points(data_points, dot_color, trace_plot=True)]

    try:
        if (class_string == True):
            print("Plot is finished (window may be hidden).")

        if (class_string[0] == False):
            print("Usage: cavg <filename>")
        if (class_string[1] == False):
            print("No such file: foo.csv")

    except:
        return


def help():
    print("stu <filename> <first name> <last name> - plot student grades")
    print("cavg <filename> - plot class average")
    print("avg <filename> <number> - prints the average for the grade item")
    print("quit - quits")
    print("help - displays this message")









if __name__ == '__main__':
    main()

