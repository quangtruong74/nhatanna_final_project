"""
Nhat Truong
Class: CS 521 - Spring 1
Date: 2/18/2024
Final project
Description of class(1-2 sentence summary in your own words):
This class contains information for a course
"""
from typing import Any


class Course:
    __offered_by ="Boston University Metropolitan College"
    #Dictionary of core and electives 
    __course_ID_core ={"METCS521": "Information Structures with Python", "METCS526": "Data Structures and Algorithms", "METCS622": "Advanced Programming Techniques",
                  "METCS665": "Software Design and Patterns", "METCS673": "Software Engineering", "METCS682": "Information Systems Analysis and Design"}
    
    __course_ID_elective ={"METCS601":"Web Application Development", "METCS602": "Server-Side Web Development", "METCS633":"Software Quality, Testing, and Security Management",
                    "METCS634":"Agile Software Development", "METCS664": "Artificial Intelligence", "METCS669": "Database Design and Implementation for Business",
                      "METCS677": "Data Science with Python", "METCS683": "Mobile Application Development with Android", "METCS701": "Rich Internet Application Development",
                        "METCS763": "Secure Software Development", "METCS767": "Advanced Machine Learning and Neural Networks"}
    def __init__(self, ID= "", Title = "", Credits = 0, Description = "", Prerequisite = ""):
        self.ID = ID
        self.Title = Title
        self.Credits = Credits
        self.Decription = Description
        self.Prerequisite = Prerequisite
        
    def get_course(self, ID:str)->"Course":
        """
        search for a course using course id
        Parameters:
        ID (str): unique id of a course
        Returns:
        Course Object: a Course object for a specific course id.
        """
        course_verification = self.__check_course(ID) #validate course ID

        #Return a dictionary of a course details (e.g. ID, credit, summary, prerequisite)
        if course_verification[0] and course_verification[1] == "CORE":
            return self.__open_file("./curriculum/core_courses/"+ID+".txt")
        elif course_verification[0] and course_verification[1] == "ELECTIVES":
            return self.__open_file("./curriculum/electives/"+ID+".txt")
        else:
            print("Course Id does not exist.")
            return Course()
            exit()

    def get_all_courses(self)->list:
        """
        Print all title for all available courses
        Parameters:
        None       
        Returns:
        list: a list of course id and title
        """
        courses_list =[]
        with open("./curriculum/curriculum_summary/all_courses.txt", "r") as file:            
            for course_title in file.readlines():
                courses_list.append(course_title)
        return courses_list


    def set_description(self, ID: str, descsription: str)->list:
        """
        Update a course description
        Parameters:
        ID (str): unique id of a course
        description: a new course description to add to the course
        Returns:
        list: a list of status code (0: failed, 1: update successfully), course Id and new description
        """
        path=""
        
        course_details = self.get_course(ID)
        course_ID = course_details.ID.split(": ")[1].strip()
        if course_ID in self.__course_ID_core.keys():
            path = "./curriculum/core_courses/"+self.ID.strip()+".txt"
        elif course_ID in self.__course_ID_elective.keys():
            path = "./curriculum/electives/"+self.ID.strip()+".txt"
        
        try:
            with open(path,"w") as file:            
                file.write(course_details.ID)
                file.write(course_details.Title)
                file.write(course_details.Credits)
                file.write("Description: "+descsription+".\n")
                file.write(course_details.Prerequisite)
            
        except FileNotFoundError as e:
            print(f"No such file exists. Occurrred inside set_description method, Course class '{e.filename}'.")
            status =[0, ID, descsription] # failed
        else:
            status =[1, ID, descsription] #updated successfully
        finally:
            return status
            

    
    def __open_file(self, file_name:str)-> "Course":
        """
        Read and return a course details if file exists
        Parameters:
        file_name (str): path to a specific file
        Returns:
        Course object: a Course object of a specific course id
        """
        try:
            with open(file_name,"r") as file:
                lines = file.readlines()    
                return Course(lines[0], lines[1], lines[2], lines[3], lines[4])
        except FileNotFoundError as e:
            print(f"No such file. Exceptio occurred inside private __open_file method, Course clsss {e.filename}")
            exit()
        except IndexError as e:
            print(f"Index out of range when assigning readlines to object's attributes. Exception occurred insided '__open_file method, Course class'.")
            exit()
    
    def __check_course(self,ID: str)-> tuple:
        """
        Check if a course is required or elective
        Parameters:
        ID (str): unique id of a course
        Returns:
        tuple: a tuple of a course type (e.g. core or elective).
        """
        if ID in self.__course_ID_core.keys():
            return (True, "CORE")
        elif ID in self.__course_ID_elective.keys():
            return(True, "ELECTIVES")
        else:
            return (False,)
      
    def __getattr__(self, atrr: str) -> str:
        """
        Check if a course attribute exists
        Parameters:
        attr (str): an attribute name
        Returns:
        str: an empty string or an atrribute value
        """    
        if not atrr in ["ID", "Title", "Credits", "Description", "Prerequisite"]:
            return ""
        else:
            return self.atrr 
    
    def __str__(self)->None:
        """
        Get an object representation
        Parameters:
        none
        Returns:
        str: a string representation of an object attributes.
        """
        return f"Your requested class details are showed below: \n{self.ID}{self.Title}{self.Credits}{self.Decription}{self.Prerequisite.strip()}"

#Testing section       

if __name__ =="__main__":
    #Assert that the 'get_course' returns an identical course id
    course_id = "METCS526"
    assert Course(course_id).get_course(course_id).ID.strip().split()[1] == course_id, "Mismatch Course ID. Check the internal working of the \'get_course\' method, and course file."
    print(f"The \'get_course\' method works correctly. It returns a match course id: \'{course_id}\'.")

    #Assert that all 18 classes are included in the all_course.txt file
    # 6 entries in the all_course.txt file are not class title
 
    assert len(Course().get_all_courses()) - 6 == 17, "The total available courses should be 17. Check the logic of \'get_all_courses\' method, and the all_course.txt file."
    print("All 17 classes are included in the all_course.txt file, and the \'get_all_courses\' method works as expected.")
   
   



    
   
    
    