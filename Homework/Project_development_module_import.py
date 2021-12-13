# • Create a directory of "Project development, module import" in the Homework directory
# • In the "Project development, module import" directory create the file course.py
# • In the file course.py create an object class Course, which should have the properties name, teacher, duration,
# as well as method teach(), which would print "Training in progress!"
# • Create a second file python_course.py in the "Project development, module import" directory
# • Create an object class PythonCourse in the python_course.py file that inherits everything
# from the Course class and overwrites it with teach() method which prints: "Programming in progress!"
# • Create a file Project_development_module_import.py in the Homework directory
# • Import the PythonCourse module (file) in the Project_development_module_import.py file
# • In the Project_development_module_import.py file, initialize the Course object with the desired properties
# • Initiate a PythonCourse object with the desired properties in the Project_development_module_import.py file
# • Run the method for both objects teach()

from abc.python_course import PythonCourse, Course

course = Course("Java", "John", 40)
python_course = PythonCourse("Python", "Anton", 80)

course.teach()
python_course.teach()
