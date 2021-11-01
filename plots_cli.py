import csv
import plotter

def main():
# this funtion will ask the user to quit or not
    command = input("Enter a command or 'quit' to quit: ")
    z = command.split()

# making sure of the command and implementing the functions
    if (z[0] == "stu"):
       student_average(["stu",r'C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv','zeyad','bonita', students_average_plotting()])


    if (z[0] == "avg"):
        print_average(["avg",r'C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv', plotter.plot_data_points(len(70), "red", trace_plot=True)])


    if (z[0] == "cavg"):
        #class_average(["cavg", r"C:\Users\Zeyad\GCIS.123.600-assignment2-sample.csv", plotter.plot(trace_plot=True)])
        class_average(["cavg", r"C:\Users\Zeyad\GCIS.123.600-assignment2-sample.csv", class_average_calculation()])

    if (z[0] == "help"):
        help()

    if z[0] == str("quit"):
         quit()
         print("Goodbye!")

# in case of errors
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
    # asks the user if sure or not for quitting
    print("Are you sure?")
    yes = input("If yes enter Y:- ")
    if yes == str("Y"):
        return True
    else:
        return False


def student_average(stu_string):
    # calculates and plots the student average for one student only
    # a_string = "stu, filename, firstname, lastname"
   stu_string = ["stu",r"C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv", "Zeyad", "Bonita", plotter.plot(trace_plot=True)]
   namefile = [1]
   if len(stu_string) != 4:
       print("Usage: stu <filename> <first name> <last name>")

   if (stu_string[1] == None):
         print("No such file: foo.csv")

# opening and reading the file
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
                   print("Plot finished (window may be hidden).")
                   break

    except:
        print("Plot failed (no such student).")


def print_average(avg_string):
    # only prints the average and not plot it
    avg_string = ["avg","filename", "gradeitem", plotter.plot_point("salam", 3, "red")]

    with open(r"C:\Users\Zeyad\GCIS.123.600-assignment2-sample.csv") as namefile:
        csv_reader = csv.reader(namefile)
        average = 0
        sum = 0
        row = 0
        for row in csv_reader:
            for column in namefile:
                n = float(column)
                sum += n
        average = sum / len(column)
        return "Average:", average

        print("Usage: avg <filename> <grade item>")

    try:
        if len(avg_string) != 3:
            print("Usage: avg <filename> <grade item>")

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
  # plots multiple averages for multiple students
    class_string = ["cavg", "filename", plotter.plot(trace_plot=True)]

    with open(r"C:\Users\Zeyad\GCIS.123.600-assignment2-sample.csv") as namefile:
       csv_reader = csv.reader(namefile)
       print(csv_reader)
       fisrtname = class_string[1]
       lastname = class_string[2]
       row = 0
       for row in csv_reader:
         while fisrtname in row:
               if lastname in row:
                   print(row)
                   plotter.init("my graph", "X-axis", "Y-axis")

               else:
                   return



    try:
        if (class_string == True):
             print("Plot is finished (window may be hidden).")

        if (class_string[0] == False):
             print("Usage: cavg <filename>")
        if (class_string[1] == False):
                print("No such file: foo.csv")

    except:
         if len(class_string) != 2:
             print("Usage: cavg <filename>")


def help():
    # simply a function to guide the user
    print("stu <filename> <first name> <last name> - plot student grades")
    print("cavg <filename> - plot class average")
    print("avg <filename> <number> - prints the average for the grade item")
    print("quit - quits")
    print("help - displays this message")




def students_average_plotting():
    plotter.init("Average of grades for Zeyad Bonita", "X-axis", "Y-axis")
    plotter.add_data_point(0.00)
    plotter.add_data_point(82)
    plotter.add_data_point(13.37)
    plotter.add_data_point(28.72)
    plotter.add_data_point(50.00)
    plotter.add_data_point(90.65)
    plotter.add_data_point(11.06)
    plotter.add_data_point(34.43)
    plotter.add_data_point(95)
    plotter.add_data_point(75)
    plotter.plot(trace_plot=True)
    input("input anything to exit")



def class_average_calculation():
    plotter.init("class average in grades", "x-axis","y-axis")
    plotter.plot(trace_plot=True)
    input("input anything to exit")







if __name__ == '__main__':
    main()

