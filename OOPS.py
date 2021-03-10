"""OOPS = Object oriented programming concept
it's about class, object inheritance, Polymorphism, data abstraction and data encapsulation
"""

"""
Object  everuthing that can exist in real time such as : car, human , jenkins , code , path ect ect 
 each object has caratheristic and functions like: 
      human = 
          carateristichs: age, name , surname, address etc 
          funtions: speach, walking , running etc 

Why are we creating objects? = to group related functions (methods)
                                to create a emplate or blueprint
        is a cpmcept where charateristic and functions of a real objcet is packages in a single entity in the code 

"""

####################### Class and Object Attributes  ##################################################

# Class is a template/blueprint to create an object
# Class is a combination of attributes and methods
# We can define Attributes for Class and Objects

# -- Example maintain data for 2 employees

class employees:      # first of all I am defining the blueprint for employees (rmember this is a templete and it won't execute untill it is called by the object)
    def get_name_age_salary(self,name,age,salary):  # I am defining method and attributes for the employees ( remember slef has to be passed as it will hold the objcet name iself for the method to be used)
        self.name=name       # self has to be used to define the variables as those variables belong to the object and self is placeholder for the object
        self.age=age
        self.salary=salary
#       self.display_details() # remember to display a method inside a class you need to use self placeholder to be executed
        return None
    def display_details(self): # we do not need to pass the attributes name, age , salary to the display methods as thay are stll accessible indide the CLass
        print("Employee Name: ", self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        return None


employee_1=employees()  # now I am creating employee "object" 1 and I am assining the templete employees created
employee_2=employees()  # employee_2 object with releveant template employees templete now I ve got 2 objects with his own template

# now I have to pass the attribute name to the employees objcets created by using the relebant method

employee_1.get_name_age_salary("Marco","46","£45000") # I am now using the method for the created object to pass the informations
employee_2.get_name_age_salary("Katia","49","£75000") # passing different values to second object by using the same method

# now I can display the values for each employee objcet created by using display_details method in the class

employee_1.display_details()  # to call the method outside Class object name dot method name
employee_2.display_details()

# to access the variables stored in the object from outside you need to use object name instead of slef as in the memory location the valued is stored with "objname.var"
print(employee_1.salary)  # use created object name and variable name to access (self stores the object name cteated)

######## find how many objects have been created by using this template ################

class employees_new:  # I am creating another Class employees_new for the new requirement
    count=0   # I am defining the varibale count outside a method, this variable belongs to the Class and can be accessed externally with classname.variable
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.increase_count() # I am calling the method to increase the counter every time object is created
        return None
    def increase_count(self): # I am creating a method to increase the count number every time an object is created
        employees_new.count=employees_new.count+1 # note the variable is defined as employees_new as it belongs to the class
        return None
    def display_details(self): # we do not need to pass the attributes name, age , salary to the display methods as thay are stll accessible indide the CLass
        print("Employee Name: ", self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        return None

####### Remember COUNT=Class attribute ######### SELF.VARIBALE=Object attributes ( self is placeholder for oject name) ############

employee_3=employees_new() # I am creating new employee_3 object with new template
print("starting count is: ",employees_new.count) # remember count is a variable for the class non the object as it is defined outside a method and can be accessed by using class name
employee_3.get_name_age_salary("Gino","35","£30000")
print("the new variable is: ",employees_new.count) # see the counter is up

##################################### CONSTRUCTOR OF A CLASS #############################################################

# a Constructor is a special method defined in yur class that gets called by default whenever you create an object for that class

class init:
    def __init__(self):  # syntax to define init constructor method
        print("Constructur method will get executed by default every time")
        return None
display=init() # see the method gets executed by default on creation ( print out displyed)

### let's modify the previously created employees_new to implement count with Constructor method

class employees_count:
    count=0
    def __init__(self): # I am creating a constructor method to increase the count number every time an object is created
        employees_count.count=employees_count.count+1
        print("the new counter is: ",employees_count.count)
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        return None
    def display_details(self): # we do not need to pass the attributes name, age , salary to the display methods as thay are stll accessible indide the CLass
        print("Employee Name: ", self.name)
        print("Employee Age: ",self.age)
        print("Employee Salary: ",self.salary)
        return None

employee_4=employees_count() # now init method will execute and counter increase every time you create a new object

class per(object): #### use this syntax when createing a class as it will be usefull when using inheritance
    def __init__(self,name,surname):  # now I am giving argument to the init method
        self.name=name
        self.surname=surname
        print(f"The given name is:{self.name}\nthe given surname is: {self.surname}")
        return None
person=per("Marco","Moro") # as init method has to argumments now you need to pass them on creation of the object

####################################### DSTRUCTOR OF A CLASS ################################################

# is a method when it gets called the object gets destroyed

del person # you cac delete an object with del also but destractors are more useful in python

# python had got garbage collector that handles memory mangment automatically

class persn(object): #### use this syntax when createing a class as it will be usefull when using inheritance
    def __init__(self,name,surname):  # now I am giving argument to the init method
        self.name=name
        self.surname=surname
        print(f"The given name is:{self.name}\nthe given surname is: {self.surname}")
        return None
    def __del__(self):   # syntax for destructior method
        print("The created object is now deleted")
        return None

person2=persn("Gino","Laino")  ## see autput the object gets deleted

############################## INHERITANCE AND POLYMORPHISM ################################################

# Polymorphism in python allows us to define same methods in different Classes also known as method overriding

class JavaVersion(object):
      def __init__(self,javaV):
          self.javaV=javaV
          print("java created")
          return None
      def display(self):
          print("the vesrion of java is: ",self.javaV)
          return None
class PythonVersion(object):
    def __init__(self, PythonV):
        self.PythonV = PythonV
        print("python created ")
        return None
    def display(self):
        print("the vesrion of Python is: ", self.PythonV)
        return None
# note both Classes uses same method display

java=JavaVersion("1.3.4")
python=PythonVersion("3.7")
java.display()     # it will olnly access Display method in javaVesrion Class
python.display()    # it will only access Display method in PyhtonVesrsion Class
# thi is called polymorphism as same methods can cohexist without interfering

######################################## INHERITANCE #############################################

# inheritance is a mechanism that allows you to create new classes known as child Class that ia bases upon existing Class "Parent Class"

# using the below example the display method is exactly the same so we can use inheritance by passing JavaVesrion2 methods to PyhtonVersion2 Class
class JavaVersion2(object):
    def __init__(self, Version):
        self.Version = Version
        print("java created")
        return None
    def display(self):
        print("Vesrion is: ", self.Version)
class PythonVersion2(JavaVersion2): # in this way I am passing all methods of JavaVersion2 to PythonVersion2
    def __init__(self, Version):
        self.Version = Version
        print("python created ")
        return None
# display method is now inherited from JavaVersion2 Class

#### NOW PythonVesrion2 is Child and JavaVersion2 is Parent ( or superclass) ######

java2=JavaVersion2("1.3.8")
python2=PythonVersion2("3.9")
# see Python2 objec can use display method inherited
python2.display()
java2.display()


###################################### ENCAPSULATION #################################################

# we can restrict access of Method and variables outside a class ( syntax is double underscore )

class myself(object):
    def get_name_Surname(self,name,surname):
        self.__name=name  # this variable cannot be accessed outside the Class
        self.surname=surname
        self.__display() # only here you can access the method
        return None
    def __display(self):   # this method cannot be accessed outside the Class
        print(f"The given name is:{self.__name}\nthe given surname is: {self.surname}")
        return None

Marco=myself()
Marco.get_name_Surname("Marco","Moro")
print(Marco.__name) # it won't be accessible see error

########## this is called encapsulation and prevent data of being modified #####################







