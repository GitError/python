'''
Using modules and packages
'''

# calling a function from another internal module
# must be imported and in the same directory 

from mymodule import func  
 
func()

# calling a function from an internal package
# must be imported and 

from mainpackage import main_module
from mainpackage.subpackage import sub_module

main_module.main_report()
sub_module.sub_report()

