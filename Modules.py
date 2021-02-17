'''module is a file containing python definitions and statements, that means a module contains python class, functions and variables
a module can help to compile your code by reusing already defined logics for specific feaures you want to develop
the key word "import + module name " give you access to predefined classes, functions and variables defined in modules
in python we already have pre defined modules like maths "import math" to list the predefined modules use "help("modules")
you can also create your module call it "yourmodule.py and import it in your script "import yourmodule" to reuse code'''

import math
dir(math)  # gives this command to python consolle and get all the operations available for the specific module
help(math) # always on python consolle gives you documentation

print(math.pow(3)) # to use power function in math module

# there are 2 types of modules: 1) defauld modules 2) third party modules

C:\Users\u6017127\PycharmProjects\pythonProject\venv\Scripts\pip install boto3 #example to install modulesto work with aws
# to import third party module you can use pip install command from command promt ( find your pip location first if not in default variable)

# another option is to import only specific operation from a module

from math import * # from math import all in this occasion by using star

print(pow(3)) #in this occasion you can access the functions pow directly

from math import pow # with this syntax we are only importing power function
from math import pi,pow # or multiple functions

import math as m #  you can create alias name and use the functions by using the alias

print(m.pow(3)) # now you are using m in your script to access maths functions 