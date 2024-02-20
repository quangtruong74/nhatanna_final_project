"""
Nhat Truong
Class: CS 521 - Spring 1
Date: 2/17/2024
Final Project
Description of class:
This file displays a welcome message and prompts user to view program courses.
"""
import string
import course_at_glance
import course
valid_option_set ={1, 2, 3, 4, 5, 6, 7} #These a set of valid option which user can select
user_input =""

option_list = ["1: All Courses offered by the program", "2: A specific Course", "3: Edit a Course" ,"4: Tuition", "5: Schedule", "6: Adimission Requirement", "7: To exit the program"]


def display_option():
    """
    Display choices from which user can select
    Parameters:
    None
    Returns:
    void
    """
    print()
    for option in option_list:
        print(option)

def display_user_request(user_input):
    """
    Display contents that user is interested in
    Parameters:
    user_input (str): a number ranging from 1-7
    Returns:
    void
    """
    if int(user_input) == 1:
        course_at_glance.get_all_courses()
        print("_"*50)
    elif int(user_input) == 2:
        print("Below are the core course ID of 'the MS in Software Development'")
        for course_id in course.Course().course_ID_core.keys():
            print(course_id)
        print("_"*50)
        print("Below are the electives ID of 'the MS in Software Development'")
        for course_id in course.Course().course_ID_elective.keys():
            print(course_id)
        print("_"*50)
        while True:
            course_id = input("Enter any of the course Id for addition information or '0' return to the previous menu: ")
            if course_id.upper() in course.Course().course_ID_core.keys() or course_id.upper() in course.Course().course_ID_elective.keys():
                specific_course = course.Course(course_id.upper())
                c = specific_course.get_course(course_id.upper())
                print(c)
                print("_"*100)
            elif course_id == "0":
                break            
            else: 
                print(f"Course ID '{course_id}' is invalid.")
    elif int(user_input) == 3:
        print("Enter a specific course id to edit: ")
        for id in course.Course().course_ID_core:
            print(f"{id}", end = ", ")
        for id in course.Course().course_ID_elective:
            print(f"{id}", end = ", ")
        course_to_edit = input("\n\nEnter a Course ID: ")
    elif int(user_input) == 6:
        exit()
    #call these function to prompt user choice again
    display_option()
    display_user_request(validate_user_choice())
    
    
def validate_user_choice():
    """
    Validate user choice. Valid if it is from 1-7
    Parameters:
    None
    Returns:
    return the option that user selected(e.g. 1-7)
    """
    while True:
        user_input =input("\nPlease make a selection: ")
        if not user_input.isdigit():
            print(f"'{user_input}' is not a digit from 1-7.")
            print("\nValid option are:")
            display_option()
            continue
        if not int(user_input) in valid_option_set:
            print(f"The number '{user_input}' is not a valid option.")
            print("\nValid option are:")
            display_option()
            continue
        break 
    return user_input 

#program starts here
print("Welcome to 'MS in Software Development' by Boston University Metropolitan College.\nSelect one of the following options to get started.")
display_option()
display_user_request(validate_user_choice())





       
        
    

