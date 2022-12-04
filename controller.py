from PyQt5.QtWidgets import *
from mainwindowgradescalc import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """
        Function to set up the methods for the buttons in the GUI and show/hide what widgets are needed to start
        :param args: the first parameter
        :param kwargs: the second parameter
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.radio_button_class_1.clicked.connect(lambda: self.radio_class_1())
        self.radio_button_class_2.clicked.connect(lambda: self.radio_class_2())
        self.radio_button_class_3.clicked.connect(lambda: self.radio_class_3())
        self.radio_button_class_4.clicked.connect(lambda: self.radio_class_4())
        self.radio_button_class_5.clicked.connect(lambda: self.radio_class_5())
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_calc.clicked.connect(lambda: self.calculate())
        self.button_reset.clicked.connect(lambda: self.reset())

        self.input_grade.hide()
        self.button_submit.hide()
        self.label_enter_grade.hide()
        self.label_wrong_input.hide()
        self.label_class_1.hide()
        self.label_class_2.hide()
        self.label_class_3.hide()
        self.label_class_4.hide()
        self.label_class_5.hide()

    def radio_class_1(self) -> None:
        """
        Function to show input box and submit button when class radio button is clicked and hide grade labels
        """
        self.label_wrong_input.hide()
        self.input_grade.show()
        self.button_submit.show()
        self.label_class_1.hide()
        self.label_grade_1.hide()
        self.label_enter_grade.show()
        self.input_grade.setText('')

    def radio_class_2(self) -> None:
        """
        Function to show input box and submit button when class radio button is clicked and hide grade labels
        """
        self.label_wrong_input.hide()
        self.input_grade.show()
        self.button_submit.show()
        self.label_class_2.hide()
        self.label_grade_2.hide()
        self.label_enter_grade.show()
        self.input_grade.setText('')

    def radio_class_3(self) -> None:
        """
        Function to show input box and submit button when class radio button is clicked and hide grade labels
        """
        self.label_wrong_input.hide()
        self.input_grade.show()
        self.button_submit.show()
        self.label_class_3.hide()
        self.label_grade_3.hide()
        self.label_enter_grade.show()
        self.input_grade.setText('')

    def radio_class_4(self) -> None:
        """
        Function to show input box and submit button when class radio button is clicked and hide grade labels
        """
        self.label_wrong_input.hide()
        self.input_grade.show()
        self.button_submit.show()
        self.label_class_4.hide()
        self.label_grade_4.hide()
        self.label_enter_grade.show()
        self.input_grade.setText('')

    def radio_class_5(self) -> None:
        """
        Function to show input box and submit button when class radio button is clicked and hide grade labels
        """
        self.label_wrong_input.hide()
        self.input_grade.show()
        self.button_submit.show()
        self.label_class_5.hide()
        self.label_grade_5.hide()
        self.label_enter_grade.show()
        self.input_grade.setText('')

    def submit(self) -> None:
        """
        Function to process input and show entered grade to user
        also checks for valid input with exception handling
        """
        self.input_grade.hide()
        self.button_submit.hide()
        self.label_enter_grade.hide()

        class_chosen = self.button_group_classes.checkedId()
        grade: str = self.input_grade.text()

        try:
            grade_check = float(grade)

            if grade_check < 0 or grade_check > 100:
                raise RuntimeError

            if class_chosen == -2 and grade_check >= 0:
                self.label_class_1.show()
                self.label_grade_1.show()
                self.label_grade_1.setText(f'{grade}%')

            elif class_chosen == -3 and grade_check >= 0:
                self.label_class_2.show()
                self.label_grade_2.show()
                self.label_grade_2.setText(f'{grade}%')

            elif class_chosen == -4 and grade_check >= 0:
                self.label_class_3.show()
                self.label_grade_3.show()
                self.label_grade_3.setText(f'{grade}%')

            elif class_chosen == -5 and grade_check >= 0:
                self.label_class_4.show()
                self.label_grade_4.show()
                self.label_grade_4.setText(f'{grade}%')

            elif class_chosen == -6 and grade_check >= 0:
                self.label_class_5.show()
                self.label_grade_5.show()
                self.label_grade_5.setText(f'{grade}%')

        except ValueError:
            self.label_wrong_input.show()
            self.label_wrong_input.setText('Enter positive number')

        except RuntimeError:
            self.label_wrong_input.show()
            self.label_wrong_input.setText('Enter number 0-100')

    def calculate(self) -> None:
        """
        Function to calculate GPA from the grades input
        does not factor in empty strings to the calculation of GPA
        """
        self.label_wrong_input.hide()
        self.input_grade.hide()
        self.button_submit.hide()

        grades_list = []

        grade: str = self.label_grade_1.text()
        if grade != '':
            grades_list.append(grade)

        grade: str = self.label_grade_2.text()
        if grade != '':
            grades_list.append(grade)

        grade: str = self.label_grade_3.text()
        if grade != '':
            grades_list.append(grade)

        grade: str = self.label_grade_4.text()
        if grade != '':
            grades_list.append(grade)

        grade: str = self.label_grade_5.text()
        if grade != '':
            grades_list.append(grade)

        try:
            total = 0
            for i in grades_list:
                num = float(i[0:-1])
                total += num

            average = total/len(grades_list)
            average_rounded = format(average, '.1f')

            if average >= 93.0:
                gpa = 4.0
            elif average >= 90.0:
                gpa = 3.7
            elif average >= 87.0:
                gpa = 3.3
            elif average >= 83.0:
                gpa = 3.0
            elif average >= 80.0:
                gpa = 2.7
            elif average >= 77.0:
                gpa = 2.3
            elif average >= 73.0:
                gpa = 2.0
            elif average >= 70.0:
                gpa = 1.7
            elif average >= 67.0:
                gpa = 1.3
            elif average >= 63.0:
                gpa = 1.0
            elif average >= 60.0:
                gpa = 0.7
            else:
                gpa = 0

            final_gpa = str(gpa)
            self.label_calc_gpa.setText(final_gpa)

        except:
            self.label_wrong_input.setText('Calculation malfunction')

    def reset(self):
        """
        Function resets all widgets to show or hide like the default GUI
        and clear all text from input and label boxes
        """
        self.label_class_1.hide()
        self.label_grade_1.hide()
        self.label_grade_1.setText('')
        self.label_class_2.hide()
        self.label_grade_2.hide()
        self.label_grade_2.setText('')
        self.label_class_3.hide()
        self.label_grade_3.hide()
        self.label_grade_3.setText('')
        self.label_class_4.hide()
        self.label_grade_4.hide()
        self.label_grade_4.setText('')
        self.label_class_5.hide()
        self.label_grade_5.hide()
        self.label_grade_5.setText('')
        self.label_enter_grade.hide()
        self.input_grade.hide()
        self.button_submit.hide()
        self.button_group_classes.setExclusive(False)
        self.radio_button_class_1.setChecked(False)
        self.radio_button_class_2.setChecked(False)
        self.radio_button_class_3.setChecked(False)
        self.radio_button_class_4.setChecked(False)
        self.radio_button_class_5.setChecked(False)
        self.label_wrong_input.hide()
        self.label_calc_gpa.setText('')
        self.button_group_classes.setExclusive(True)
