# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions and classes
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Diego Mejia>,<11/18/24>, <Created Script>
# ------------------------------------------------------------------------------------------ #

import json
import sys
# Define the Data Constants
MENU: str = """
--- Course Registration Program ---
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
-----------------------------------
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
file_obj = None
menu_choice: str = ''
students: list = []


class File_Processor:
    global file_obj
    global students
    global FILE_NAME
    
    @staticmethod

    def read_data_from_file():
        try:
            with open(FILE_NAME, 'r') as file_obj:
                json_data = json.load(file_obj)
                return json_data 
                file_obj.close() 
        except FileNotFoundError:
            IO.output_error_messages(f'There is no file {FILE_NAME}')
            
            file_obj = open(FILE_NAME,'w')
        except Exception:
            IO.output_error_messages("There was an error opening the file")
               
        finally:
            print("Closing File")
            file_obj.close()
            
            
    def write_data_to_file():  
        try:
            with open(FILE_NAME, "w") as file_obj:
                json.dump(students,file_obj)
                for student in students:
                    if "FirstName" not in student:
                        raise KeyError("First name not in dict{}")
                    elif "LastName" not in student:
                        raise KeyError("Last name not in dict{}")
                    elif "CourseName" not in student:
                        raise KeyError("Course name not in dict{}")
                    else:
                        print("All keys found in dict{}")
                    
        except IOError:
            IO.output_error_messages(f'Error writing data into {FILE_NAME}')
            
        finally:
            print("Closing file")
            file_obj.close()
            print(f'{student["FirstName"]} {student["LastName"]} has registered for {student["CourseName"]} in this last user session!')
       

class IO:
    global MENU
    global students
    global json_data
    global menu_choice
    
    @staticmethod
    
    def input_student_data():
        try:
            student_first_name = input("Enter Student's First Name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must contain only letters")
                
            student_last_name  = input("Enter Student's Last Name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must contain only letters")
                
            course_name = input("Enter Course Name: ")
            json_data = {"FirstName":student_first_name, "LastName":student_last_name, "CourseName":course_name} 
            students.append(json_data) 
        except ValueError:
            IO.output_error_messages("First and Last name must only contain letters")
            
        
    def output_student_courses():
        print('Current List Table: Full Table of all students registered ')
        print(students)
         
    def output_error_messages():
        print(__doc__)
        
    
        

    def input_menu():
        # Present the menu of choices
        menu_choice = input('What would you like to do? ')
        
        if menu_choice == '1':
            IO.input_student_data()
        
        elif menu_choice == '2':
            IO.output_student_courses()                      
              
        elif menu_choice == '3':
            File_Processor.write_data_to_file()
                        
        elif menu_choice == '4':
            print('Program Ended')
            sys.exit()
        
        else:
            print("INVALID CHOICE: Please choose options 1, 2, or 3")
        return menu_choice
    
    def output_menu():
        print(MENU)
      
        
File_Processor.read_data_from_file()        
        
while True:
    # Present the menu of choices
    IO.output_menu()
    IO.input_menu()
    
    print('All Done!')
    

    





    
  