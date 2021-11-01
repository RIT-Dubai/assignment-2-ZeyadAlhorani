import plots_cli
import plotter


def test_student_average():
# test to make sure the input is correct
    stu_correct = ["stu",r'C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv','zeyad','bonita']
    stu_wrong = ["stu",r'C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv','zey','bonita'] #wrong student
    assert plots_cli.student_average(stu_correct) == True
    assert plots_cli.student_average(stu_wrong) == False


def test_print_average():
# to make sure calculation is correct

def test_class_average():
# test to make sure output are sorted and correct
    cavg_correct = ["cavg",r'C:\Users\Zeyad\Desktop\GCIS.123.600-assignment2-sample.csv']
    cavg_wrong = ["cavg",] # no file here
    assert plots_cli.class_average(cavg_correct) == True
    assert plots_cli.class_average(cavg_wrong) == False
