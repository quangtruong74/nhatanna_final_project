"""
Nhat Truong
Class: CS 521 - Spring 1
Date: 2/17/2024
Final Project
Description of class:
This file displays a welcome message and prompts user to view/edit program courses.
"""
#import string
#import course_at_glance
import course

user_input =""
option_list = ["1: All Courses offered by the program", "2: A specific Course", "3: Edit a Course (Can only update a course description)" ,"4: To exit the program"]
valid_option_set ={1, 2, 3, 4} #These a set of valid option which user can select
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
        for course_title in course.Course().get_all_courses():
            print(course_title.strip())
        print("_"*50)
    elif int(user_input) == 2:        
        #print("Below are the core course ID of 'the MS in Software Development'")
        core_class_ID= course.Course()._Course__course_ID_core.keys()
        core_elective_ID= course.Course()._Course__course_ID_elective.keys()
        

        print()
        print("Below are the core course ID of 'the MS in Software Development'")
        for course_id in core_class_ID:
            print(f"{course_id:<}", end =" ")
        print()
        print("Below are the electives ID of 'the MS in Software Development'")
        for course_id in core_elective_ID:
            print(course_id, end =" ")
        print("\n")
        #print("Below are the electives ID of 'the MS in Software Development':")

        """TEST
        for course_id in core_class_ID:
            print(course_id)
        print("_"*50)
        print("Below are the electives ID of 'the MS in Software Development'")
        c = course.Course()
        for course_id in core_elective_ID:
            print(course_id)
        print("_"*50)
        """

        while True:
            course_id = input("Enter any of the course Id for addition information about the course. Or '0' return to the previous menu: ")
            # check if course_id is valid
            if course_id.upper() in course.Course()._Course__course_ID_core.keys() or course_id.upper() in course.Course()._Course__course_ID_elective.keys():
                specific_course = course.Course(course_id.upper())
                c = specific_course.get_course(course_id.upper())
                print()
                print(c)
                print("_"*100)
            elif course_id == "0":
                break            
            else: 
                print(f"Course ID '{course_id}' is invalid.")
    #edit a course description by course id            
    elif int(user_input) == 3:
        course_id =[] # list of core and electives course id

        for id in course.Course()._Course__course_ID_core.keys():   
            course_id.append(id)
        for id in course.Course()._Course__course_ID_elective.keys():
            course_id.append(id)
        
        print("_"*100)
        print("Select one of the following course ids to edit course description: ")
        print(course_id)
        while True:            
            course_ID_to_edit = input("\n\nEnter a Course ID: ").strip().upper()
            if not course_ID_to_edit in course_id:
                print(f"Course id {course_ID_to_edit} is invalid.")
                continue
            else:
                c = course.Course(course_ID_to_edit)
                c.get_course(c.ID)
                print(f"Below is current course description of {course_ID_to_edit}:\n")
                print(f"{c.get_course(c.ID).Decription}")
            break
        new_course_description = input("\n\nEnter a new course description: ")
        c = course.Course(course_ID_to_edit, Description = new_course_description)
        #update and check its status
        status = c.set_description(c.ID, c.Decription)
        if status[0] == 1:
            print(f"Course ID {status[1]} updated successfully.")
        else:
            print(f"Not able to update the course at the moment. Please try again later.")

    elif int(user_input) == 4:
        print("Thanks for your interest in our 'MS in Software Development by Boston University Metropolitan College.'\nGood Bye!")
        
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
if __name__ == "__main__":
    print("Welcome to 'MS in Software Development' by Boston University Metropolitan College.\nSelect one of the following options (e.g. 1-4) to get started.")
    display_option()
    display_user_request(validate_user_choice())





       
        
    

