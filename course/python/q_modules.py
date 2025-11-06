# You can import functions from other files (modules) and use them by referencing the module name.
# Example: import <module>, then call the function with <module>.<function_name>()
# You can also create an alias (shortcut) for the module using "as".

import n_functions as a

a.greeting_9_with_name("Sulaiman")
a.game_1("9", "stop")

# You can also import specific functions, variables, or classes directly from a module.
# In that case, you don’t need to prefix them with the module name.
# You can still use "as" to rename imported items for convenience.

from n_functions import greeting_9_with_name as b, game_1 as c, name
from n_functions import Test

b("Test_2")
c("9", "stop")

# You can access imported variables and class attributes directly.
print(name)
print(Test.a)

# To use class properties or methods, you first need to create an instance of the class.
test_obj = Test()
print(test_obj.a)
