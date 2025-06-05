# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates creating and using data classes
# to manage data
# Change Log: (Who, When, What)
# Tellrell White,06/02/25,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.

    ChangeLog:
        - Tellrell White, 06.02.2025: Created the class.
    """


    # Constructor with private attributes for the first_name and last_name data
    def __init__(self, first_name: str = '', last_name: str = ''):
        """ This function sets values for an objects attributes for first name and last name when created

               ChangeLog: (Who, When, What)
               Tellrell White,06/02/25,Created function

               #add params in
               :param self: refers to data found in object instance

               :return:   None
               """
        self.first_name = first_name
        self.last_name = last_name

    # Property getter and setter for first name using the same code as in the Student class
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        """ This function returns a value for an objects first name

                      ChangeLog: (Who, When, What)
                      Tellrell White,06/02/25,Created function

                      #add params in
                      :param self: refers to data found in object instance

                      :return: first_name
                      """
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        """ This function sets a value for an objects first name. Also includes error handling for
        checking that first name is all aphabetic characters.

                              ChangeLog: (Who, When, What)
                              Tellrell White,06/02/25,Created function

                              #add params in
                              :param self: refers to data found in object instance
                              :param value: string value for first name

                              :return: None
                              """
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # Creates a property getter and setter for last name using the same code as in the Student class
    @property
    def last_name(self):
        """ This function returns a value for an objects last name

                            ChangeLog: (Who, When, What)
                            Tellrell White,06/02/25,Created function

                            #add params in
                            :param self: refers to data found in object instance

                            :return: last_name
                            """
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        """ This function sets a value for an objects last name. Also includes error handling for
                checking that a last name name is all aphabetic characters.

                                      ChangeLog: (Who, When, What)
                                      Tellrell White,06/02/25,Created function

                                      #add params in
                                      :param self: refers to data found in object instance
                                      :param value: string value for first name

                                      :return: None
                                      """
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        """ This function overrides the default default __str__() method's behavior and return a coma-separated
        string of data

                                              ChangeLog: (Who, When, What)
                                              Tellrell White,06/02/25,Created function

                                              #add params in
                                              :param self: refers to data found in object instance

                                              :return: string of CSV data for first name and last name
                                              """
        return f'{self.first_name},{self.last_name}'

class Student(Person):
    """
    A class representing student data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): The course information.

    ChangeLog: (Who, When, What)
    Tellrell White,06.02.2025,Created Class
   
    """

    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        """ This function utilizes the constructor of the Parent class (Person) which initializes
        first name and last name, and includes an addtional property, course name.

                       ChangeLog: (Who, When, What)
                       Tellrell White,06/02/25,Created function

                       #add params in
                       :param self: refers to data found in object instance
                       :param first_name: string value for first name
                       :param last_name: string value for last name
                       :param course_name: string value for course information

                       :return:   None
                       """

        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        """ This function returns a value for an objects course name

                              ChangeLog: (Who, When, What)
                              Tellrell White,06/02/25,Created function

                              #add params in
                              :param self: refers to data found in object instance

                              :return: course_name """
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        """ This function sets a value for an objects course name.

                                      ChangeLog: (Who, When, What)
                                      Tellrell White,06/02/25,Created function

                                      #add params in
                                      :param self: refers to data found in object instance
                                      :param value: string value for course_name

                                      :return: None
                                      """

        self.__course_name = value
        

    def __str__(self):
        """ This function overrides the Parent __str__() method behavior to return a coma-separated
        string of data

                                              ChangeLog: (Who, When, What)
                                              Tellrell White,06/02/25,Created function

                                              #add params in
                                              :param self: refers to data found in object instance

                                              :return: string of CSV data for first name, last name, and course name
                                              """

        return f'{self.first_name},{self.last_name},{self.course_name}'




# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Tellrell White,06.02.2025,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        Tellrell White,06.02.2025,Created function

        :param file_name: string data with name of file to read from

        :return: list
        """

        try:
            file=None
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            list_of_dictionary_data:list =[]
            list_of_dictionary_data = json.load(file)

            for row in list_of_dictionary_data:  # Convert the list of dictionary rows into Student objects
                student_object: Student = Student(first_name=row["FirstName"],
                                                  last_name= row["LastName"],
                                                  course_name=row["CourseName"])
                student_data.append(student_object)
            file.close()

        except FileNotFoundError  as e:
            IO.output_error_messages(message="Error: Text file must exist before running this script!", error=e)

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file and file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Tellrell White,06.02.2025,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            # Converts Student objects into dictionaries
            file = None
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            print("The following data was saved to file!")
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Tellrell White,06.02.2025,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Tellrell White,06.02.2025,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Tellrell White,06.02.2025,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Tellrell White,06.02.2025,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:

            # TODO Add code to access Student object data instead of dictionary data
            print(f'Student {student.first_name} '
                  f'{student.last_name}is enrolled in {student.course_name} ')

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Tellrell White,06.02.2025,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student = Student()
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")

            student_data.append(student)
            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was an invalid type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

#------------------------------  End of Class definitions--------------------------------------------------#


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
