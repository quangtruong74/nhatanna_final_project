"""
Nhat Truong
Class: CS 521 - Spring 1
Date: 2/17/2024
Final Project
Description of class:
This file displays a summary of coureses of Master's in Sofware Development by Boston University Metropolitan College
"""
course = []
def get_all_courses():
    with open("./curriculum/curriculum_summary/all_courses.txt", "r") as file:
        
        for line in file.readlines():
            print(line.strip())
            course.append(line)

#test
if __name__ == "__main__":
    get_all_courses()


    

