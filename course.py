"""
Nhat Truong
Class: CS 521 - Spring 1
Date: 2/18/2024
Homework Problem # Final project
Description of class(1-2 sentence summary in your own words):
This class contains information for a course
"""
class Course:
    __offered_by ="Boston University Metropolitan College"

    course_ID_core ={"METCS521": "Information Structures with Python", "METCS526": "Data Structures and Algorithms", "METCS622": "Advanced Programming Techniques",
                  "METCS665": "Software Design and Patterns", "METCS673": "Software Engineering", "METCS682": "Information Systems Analysis and Design"}
    
    course_ID_elective ={"METCS601":"Web Application Development", "METCS602": "Server-Side Web Development", "METCS633":"Software Quality, Testing, and Security Management",
                    "METCS634":"Agile Software Development", "METCS664": "Artificial Intelligence", "METCS669": "Database Design and Implementation for Business",
                      "METCS677": "Data Science with Python", "METCS683": "Mobile Application Development with Android", "METCS701": "Rich Internet Application Development",
                        "METCS763": "Secure Software Development", "METCS767": "Advanced Machine Learning and Neural Networks"}
    def __init__(self, ID=0, Title = "", Credits = 0, Description = "", Prerequisite = ""):
        self.ID = ID
        self.Title = Title
        self.Credits = Credits
        self.Decription = Description
        self.Prerequisite = Prerequisite
        
    def get_course(self, ID):
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
            exit()

    def set_description(self, ID, descsription):
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
            status =[0, ID, descsription]
        else:
            status =[1, ID, descsription]
        finally:
            return status
            


    def __open_file(self, file_name):
        """
        Private method to read a file 
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

    def __check_course(self,ID):
        """
        Check if a course is required or elective
        Parameters:
        ID (str): unique id of a course
        Returns:
        tuple: a tuple of a course type (e.g. core or elective).
        """
        if ID in self.course_ID_core.keys():
            return (True, "CORE")
        elif ID in self.course_ID_elective.keys():
            return(True, "ELECTIVES")
        else:
            return (False,)
    def __str__(self):
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
    c = Course("METCS601")
   # d = c.get_course("METCS768")
   # print(d)
    l =c.set_description("METCS601", "this is a test")
    for i in l:
        print(i)
    
   
    
    