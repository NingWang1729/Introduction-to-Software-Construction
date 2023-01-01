# Chapter 4: Python Libraries

4. [Python Libraries](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#chapter-4-python-libraries)
  - 4.1 [Agreeable Argparse](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#41-agreeable-argparse)
  - 4.2 [Logical Logging](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#42-logical-logging)
  - 4.3 [Potent PDB](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#43-potent-pdb)
  - 4.4 [Nifty NumPy](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#44-nifty-numpy)
  - 4.5 [Practical Pandas](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#45-practical-pandas)
  - 4.6 [Pretty Pickle](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#46-pretty-pickle)
  - 4.7 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#47-succinct-summary)

# 4.1 Agreeable Argparse

With more complex tasks, it is often useful to write a Python script, that is, a file that contains multiple lines of Python code. While we could edit the code to handle various files by hard coding in various values, this is not practical when you may need to run code multiple times with different values. Thus, it is useful to have a library, or collection of well documented code with a specific purpose, for handling command line arguments. To import a `module`, an instance of a library, you can use the keyword `import`, followed by the module name. Python modules are organized inside "packages". Imports also work for importing code from your own Python files. When importing functions from a ".py" file, place the name of the file (without the ".py") after the `import` keyword. Note that the file name has a higher priority than a library import, so it is highly recommended to not name your files the same name as a library import to avoid self-inflicted confusion.  

```
import argparse # Imports the argparse library
import temperature_conversion # Imports functions from temperature_conversion.py
```

To use the `argparse` library, we will first begin with creating an instance of the argument parser object. It is standard to name this object "parser". Inside the parentheses, you can also use the optional `prog` keyword to specify the name of the program, which defaults to the name of the file. After adding your arguments, you can parse the arguments using the "parse_args" method, which reads arguments from command line with no arguments. Alternatively, you can manually insert a list of strings for the parser to parse, which are the command line arguments separated by spaces that would otherwise be in the shell command.  

```
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(prog='Thermometer')
args = parser.parse_args()
args = parser.parse_args(['10', 'Celsius', 'Fahrenheit'])
```

After creating a parser, you may want to add some arguments for the parser to handle. This is done by calling the "add\_argument" method from the parser object. These arguments have a wide variety of actions that can be used for the arguments. The simplest, and default, action is "store", which simply stores the input value for a given attribute of the parser. These attributes can either be positional, where the order of the argument in the command line usage matters, or an optional argument, which uses a flag. The positional arguments are specified by simply having the name of the attribute as the first argument of the "add\_argument" method of the parser. As with any other identifier in Python, the name of this attribute must start with a letter or an underscore and can only contain letters, numbers, and underscores.  

```
parser.add_argument('temperature', action='store')
```

Flags are similar to the flags you would find with shell commands, which use a dash for short-hand notation, and two dashes for long format.  

```
parser.add_argument('-t', '--temperature', action='store')
```

To change the name of the attribute that the argument is stored in, you can set a destination using the "dest" argument, which defaults to the text in the long form argument name, with any dashes in the name (excluding the flags) converted to underscores.  

```
parser.add_argument('-t', '--temperature', dest='temp', action='store')
```

With multiple options, clear documentation is important for making your code easy to use for others. You can add a help message for each argument using the "help" optional argument, which is displayed whenever the "-h" or "--help" flag is used, rather than running the script itself.  

```
parser.add_argument('-t', '--temperature', dest='temp', action='store', help='Specify a temperature to convert to other units.')
"""
bash$ python3 temperature_conversion.py -h
usage: Thermometer [-h] [-t TEMP]

options:
  -h, --help            show this help message and exit
  -t TEMP, --temperature TEMP
                        Specify a temperature to convert to other units.
"""
```

As you can see, the usage is indicating that the temperature argument is represented as "TEMP", which is the "dest" argument in all capital letters. To change this meta variable, you can specify the "metavar" argument for the usage representation.  

```
parser.add_argument('-t', '--temperature', dest='temp', metavar='Temperature', action='store', help='Specify a temperature to convert to other units.')
"""
bash$ python3 temperature_conversion.py -h
usage: Thermometer [-h] [-t Temperature]

options:
  -h, --help            show this help message and exit
  -t Temperature, --temperature Temperature
                        Specify a temperature to convert to other units.
"""
```

As the input from command line will be in text format, it is only natural that the default of the argument values to be `str`, but you can specify a type for the parser to convert the argument into using the `type` keyword. For simplicity, we will use `float` type for our temperature.  

```
parser.add_argument('-t', '--temperature', type=float, dest='temp', metavar='Temperature', action='store', help='Specify a temperature to convert to other units.')
```

By default, the number of arguments expected for each argument is 1, which stores the input value as the value of the corresponding attribute, but you can change this amount using the "nargs" option. You can either specify a numerical integer, which will store the specified number of arguments in a `list` for the specified argument. Notably, setting "nargs" to 1 will create a `list` of length one. You can also specify a variable length for the number of arguments, with '?' representing 0 or 1 arguments, '*' representing 0 or more arguments, and '+' representing 1 or more arguments. Often, the '?' will be used for optional arguments with a default value. Note that these are consistent with their representations in bash.  

```
parser.add_argument('-rt', '--room-temperature, type=float, nargs='?', default=20, dest='temp', metavar='Room Temperature', action='store', help='Specify the current room temperature in the same units as the input.')
```

If we fail to pass in a value, the default option will be used. If the "default" optional argument is not used, then the default will be `None`. On the other hand, if we want an argument to be mandatory, you can set the "required" option to be `True`.  

```
parser.add_argument('-t', '--temperature', type=float, required=True, dest='temp', metavar='Temperature', action='store', help='Specify a temperature to convert to other units.')
```

Sometimes, it may be useful to have a boolean flag to flip on or off. With `argparse`, we can choose to set "action" to "store\_true" or "store\_false", with the default values being `False` and `True`, respectively. Rather than accepting an argument, using this flag simply toggles a boolean variable. A common use case for this type of argument is for verbosity. (Obviously, these types of actions should not be set as a required argument, which would be creating an overly convoluted way for setting an attribute to a predetermined boolean value.)  

```
parser.add_argument('-v', '--verbose', action='store_true', help='Toggle verbosity.')
```

Other times, it may be useful to have multiple mutually exclusive groups. In this temperature script, we will be handling Celsius, Fahrenheit, and Kelvin units for measuring temperature. Rather than adding a singular argument to the parser using the "add\_argument" method, we can add a mutually exclusive group to the parser using the "add\_mutually\_exclusive\_group" method and add arguments to the group itself using the "add\_argument" method.  

```
input_units = parser.add_mutually_exclusive_group()
input_units.add_argument('-if', '--input-fahrenheit', action='store_false')
input_units.add_argument('-ic', '--input-celsius', action='store_true')
input_units.add_argument('-ik', '--input-kelvin', action='store_true')
ouput_units = parser.add_mutually_exclusive_group()
ouput_units.add_argument('-of', '--output-fahrenheit', action='store_true')
ouput_units.add_argument('-oc', '--output-celsius', action='store_false')
ouput_units.add_argument('-ok', '--output-kelvin', action='store_true')
```

With argparse, Python scripts can become versatile command line tools. However, you may have functions that can be useful in other scripts within the same file. Thus, you may wish to only use the command line parsing for when you are executing the script itself, rather than when importing functions or classes to another Python file. To do so, we can use the special if statement "if \_\_name\_\_ == '\_\_main\_\_':", which only runs the code in the if statement if the file itself is being executed. All together, our code currently looks as follows.  

```
# Library imports
import argparse


# Temperature conversion formulas
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def celsius_to_kelvin(temp):
    return temp + 273.15


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def fahrenheit_to_kelvin(temp):
    return celsius_to_kelvin(fahrenheit_to_celsius(temp))


def kelvin_to_celsius(temp):
    return temp - 273.15


def kelvin_to_fahrenheit(temp):
    return kelvin_to_celsius(celsius_to_fahrenheit(temp))


# Main function
if __name__ == '__main__':
    # Set arguments
    parser = argparse.ArgumentParser(prog='Thermometer')
    parser.add_argument('-t', '--temperature', type=float, required=True, dest='temp', metavar='Temperature', action='store', help='Specify a temperature to convert to other units.')
    parser.add_argument('-rt', '--room-temperature', type=float, nargs='?', default=20, dest='room', metavar='Room Temperature', action='store', help='Specify the current room temperature in the same units as the input. Default=20° Celsius')
    parser.add_argument('-v', '--verbose', action='store_true', help='Toggle verbosity.')

    # Add unit conversions
    conversions = parser.add_mutually_exclusive_group()
    conversions.add_argument('-cf', '--celsius-to-fahrenheit', action='store_false')
    conversions.add_argument('-ck', '--celsius-to-kelvin', action='store_true')
    conversions.add_argument('-fc', '--fahrenheit-to-celsius', action='store_true')
    conversions.add_argument('-fk', '--fahrenheit-to-kelvin', action='store_true')
    conversions.add_argument('-kc', '--kelvin-to-celsius', action='store_true')
    conversions.add_argument('-kf', '--kelvin-to-fahrenheit', action='store_true')

    # Parse arguments
    args = parser.parse_args()

    if args.celsius_to_fahrenheit:
        print(celsius_to_fahrenheit(args.temp))
    elif args.celsius_to_kelvin:
        print(celsius_to_kelvin(args.temp))
    elif args.fahrenheit_to_celsius:
        print(fahrenheit_to_celsius(args.temp))
    elif args.fahrenheit_to_kelvin:
        print(fahrenheit_to_kelvin(args.temp))
    elif args.kelvin_to_celsius:
        print(kelvin_to_celsius(args.temp))
    else:
        print(kelvin_to_fahrenheit(args.temp))

    # Check if room temperature is hot
    if args.verbose:
        if args.room > args.temp:
            print("Less than room temperature")
        else:
            print("Greater than or equal to room temperature")

"""
bash$ python3 temperature_conversion.py -t 10
50.0
bash$ python3 temperature_conversion.py -t 21 --fahrenheit-to-kelvin -v
69.8
Greater than or equal to room temperature
bash$ 
"""
```

Argparse provides a modern approach to parsing command line arguments. For further reference, please refer to the [official argparse documentation](https://docs.python.org/3/library/argparse.html). Also, you may wish to reference the `system` and `os` modules, which are sometimes used together with argparse.  

# 4.2 Logical Logging
Python is a high level language, which means it provides many syntactic sugars to make it easier for the programmer to write code, abstracting away the lower level implementations of the code. For example, while the `print` function will output some text, it does not immediately execute the print operation after the line of code telling Python to print is executed. This may be problematic if you were expecting the `print` statement to provide a log of how the program is performing as it is running in real time. While you could set the "flush" argument to 'True', forcing the print statement to immediately execute, manually formatting every print statement would be both tedious and redundant when you could simply use the Python logging module. 

To import the logging module, simply `import logging`. To mimic the behavior of print statements, you can use the lowest level of logging, which is "DEBUG". There are 6 default levels of logging, which are "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", and "CRITICAL", which have the numerical values of 0, 10, 20, 30, 40, and 50 respectively. If you were to use your own levels, they should account for the numerical levels relative to the default values. To output a log message with a specified level, you can simply call that level's respective method, with the string you would like to output as the argument.  

```
import logging
logging.debug('Hello World!')
```

With all these levels of logging, it can become overwhelming to decide which levels to use. The logging levels offer an alternative to using multiple if statements to toggle verbosity manually. To set a basic configuration to use for most instances, you can take advantage of the `basicConfig` method, where you can set options such as a level of logging to display and a format string to use. However, this basic configuration must come first before any other logging. It will not be able to override any existing settings you may have set earlier.  

```
format = "%(levelname)s - %(funcName)s - %(lineno)d - %(asctime)s - %(message)s"
logging.basicConfig(level = logging.WARNING, format = format)
```

Note that in the format string, we are passing in multiple attributes from the LogRecord. You can also use `string.format()`  For a complete list of attributes, please refer to the [Official LogRecord Attributes Documentation](https://docs.python.org/3/library/logging.html#logrecord-attributes).  


The level indicates which level of logging you would like to display. This can be combined with argparse to set specific verbosity levels. To change the level afterwards, you can use the `setLevel` method.  

```
logging.setLevel(logging.ERROR)
```

The logging module can be as simple or as complex as you wish it to be. Currently, we have covered the basics of setting levels using the logging module directly. You can also create named logger objects for each file you use, as well as custom handler and formatter objects. This works similarly to creating argparse instances and attaching objects to the parsers.  

```
import logging

# Initiate logging object
logger = logging.getLogger(__name__)

# Initialize handlers
default_handler = logging.StreamHandler()
logger.addHandler(default_handler)
verbose_handler = logging.FileHandler(logfile) # Assume passed in via argparse
logger.addHandler(verbose_handler)

# Initialize logging level
default_handler.setLevel(logging.ERROR)
verbose_handler.setLevel(logging.DEBUG)

# Initialize formatters
default_format = logging.Formatter("%(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(asctime)s - %(message)s")
default_handler.setFormatter(default_format)
verbose_format = logging.Formatter("%(levelname)s - %(pathname)s - %(funcName)s - %(lineno)d - %(asctime)s - %(message)s")
verbose_handler.setFormatter(verbose_format)
```

Finally, it is useful to log exceptions that may occur in your code. In Python, we can use try-except blocks to catch exceptions. Additionally, it is highly recommended to use specific exceptions rather than a general catch all. We will use the following integer division code to demonstrate how the logging module can be used with exception handling. For more information on Python exceptions, please refer to the [Official Built-in Exceptions Documentation](https://docs.python.org/3/library/exceptions.html).  

```
import logging

try:
	# Load two numbers
	a = int(input())
	b = int(input())
except ValueError:
	# Non integer inputs
	logging.error("Inputs must be integers!")
except ZeroDivisionError:
	# Division by zero
	logging.error("Divison by Zero is undefined.")
except Exception as e:
	# Unexpected exception
	logging.error("Unexpected exception", exc_info=True)
```

Furthermore, you can add more detailed filters as well as adjust module level settings. If you are interested in more complex usage of the logging module, please refer to the [Official Logging Documentation](https://docs.python.org/3/library/logging.html).

# 4.3 Potent PDB
It would be remiss to discuss logging and debugging without mentioning the built in Python debugger, pdb. The pdb module can be used either as a module import, or on the command line. For the purposes of this tutorial, we will use pdb while executing the command line temperature script. Note that "(Pdb)" is the prompt for executing debugging instructions.  

```
bash$ python3 -m pdb temperature_conversion.py -t 20 -cf
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(2)<module>()
-> import argparse
(Pdb) 
```

At the first line of our script, we see that we have "import argparse". The "->" arrow indicates which line is next to be executed. To execute this line of code and move on to the next line, we can enter "n(ext)". The parenthesis indicate the full command, with the first letter being the shorthand notation. Thus, you can either enter the word "next", or just the letter, 'n'.  

```
(Pdb) next
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(6)<module>()
-> def celsius_to_fahrenheit(temp):
```

In our code, we see numerous function declarations. We will want to call this "celsius\_to\_fahrenheit" function later, so we will run the code "unt(il)" the line after the end of this function. Note that the debugger will skip empty lines and stop after it reaches a line greater than or equal to the input number.  

```
(Pdb) until 9
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(11)<module>()
-> def celsius_to_kelvin(temp):
(Pdb) 
```

If we wanted to check "w(here)" we are in our call stack, or "l(ist)" the surrounding lines of code, we can use these respective commands to find our position. Also, we can adjust how many lines to display, with the default being 11 lines. You can also specify a range of lines to display.  

```
(Pdb) w
  /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/bdb.py(597)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(11)<module>()
-> def celsius_to_kelvin(temp):
(Pdb) l
  6  	def celsius_to_fahrenheit(temp):
  7  	    # Convert Celsius to Fahrenheit
  8  	    return (temp * 9 / 5) + 32
  9  	
 10  	
 11  ->	def celsius_to_kelvin(temp):
 12  	    # Convert Celsius to Kelvin
 13  	    return temp + 273.15
 14  	
 15  	
 16  	def fahrenheit_to_celsius(temp):
(Pdb) l .
  6  	def celsius_to_fahrenheit(temp):
  7  	    # Convert Celsius to Fahrenheit
  8  	    return (temp * 9 / 5) + 32
  9  	
 10  	
 11  ->	def celsius_to_kelvin(temp):
 12  	    # Convert Celsius to Kelvin
 13  	    return temp + 273.15
 14  	
 15  	
 16  	def fahrenheit_to_celsius(temp):
(Pdb) l 9,15
  9  	
 10  	
 11  ->	def celsius_to_kelvin(temp):
 12  	    # Convert Celsius to Kelvin
 13  	    return temp + 273.15
 14  	
 15  	
(Pdb) 
```

Since we will not be executing all these functions given our command line arguments, we can "j(ump)" ahead in our code. This command requires specifying a line to jump to, which can be either earlier or later in the code. However, some parts of the code cannot be jumped into, i.e. into the middle of a for loop.  

```
(Pdb) j 36
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(36)<module>()
-> # Main function
(Pdb) 
```

With debuggers, it is often useful to set breakpoints. Now that we reached our "if \_\_name\_\_ == '\_\_main\_\_'", we can set a "b(reak)" point at where we call our temperature conversion function by specifying the line number.  

```
(Pdb) b 68
Breakpoint 1 at /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py:68
(Pdb) 
```

With a break point set, we can "c(ontinue)" until we reach the end of our code or the first break point we encounter from our current location in the code. Altogether, the "unt(il)", "b(reak)", and "c(ontinue)" commands allow easy control over the program over an extended number of lines of code to run. This is especially helpful when you may need to repeat multiple lines of code in a loop.  

```
(Pdb) continue
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(68)<module>()
-> print(celsius_to_fahrenheit(args.temp))
(Pdb) 
```

Here, we see that we have two function calls. The `print` function is being passed a function call to the `celsius\_to\_fahrenheit` function, which in turn takes in the "temp" argument. Before we "s(tep)" into our functions, we can take a look at the current state of our identifiers in our program.  

```
(Pdb) args.temp
temp = 20.0
(Pdb) args
temp = 20.0
(Pdb) print(args)
Namespace(temp=20.0, room=20, verbose=False, celsius_to_fahrenheit=True, celsius_to_kelvin=False, fahrenheit_to_celsius=False, fahrenheit_to_kelvin=False, kelvin_to_celsius=False, kelvin_to_fahrenheit=False)
```

To "s(tep)" into a function, we will move from the current line of code to inside the code for the function we are stepping into. Here, we first step into print, which in turn calls the `celsius\_to\_fahrenheit` function.  

```
(Pdb) s
--Call--
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(6)celsius_to_fahrenheit()
-> def celsius_to_fahrenheit(temp):
(Pdb) n
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(8)celsius_to_fahrenheit()
-> return (temp * 9 / 5) + 32
(Pdb) n
--Return--
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(8)celsius_to_fahrenheit()->68.0
-> return (temp * 9 / 5) + 32
(Pdb) n
68.0
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(71)<module>()
-> if args.verbose:
(Pdb) 
```

After the `return`, the `print` function is then able to print the resulting temperature, "68.0", to the console. As we have finished examining the code that we will be running, we can simply "c(ontinue)" until we reach the end of the program and "exit" the debugger. Alternatively, you can exit the debugger at any point in time using `Ctrl+D`.  

```
(Pdb) c
The program finished and will be restarted
> /Users/foobar/Introduction-to-Software-Construction/temperature_conversion.py(2)<module>()
-> import argparse
(Pdb) exit
bash$ 
```

Here, we demonstrated some of the basic usages of the built-in Python debugger, pdb. Debugging is an important skill for software construction, and the pdb debugger is both straight forward and easy to use. For further details and clarification, please refer to the [Official pdb Documentation](https://docs.python.org/3/library/pdb.html).  

# 4.4 Nifty NumPy
NumPy is one of the most commonly used packages for data science in Python. While Python has the native `list` data structure, more computational programs will often require large, multi-dimensional arrays. As an interpreted languages, Python is simply too slow for larger applications. However, with compiled C code, packages such as NumPy allow the user to enjoy both the easy to use syntax of Python along with the efficiency of compiled C libraries. NumPy's primary usage revolves the `ndarray`, which allows versatile, multi-dimensional arrays, as well as basic high level math operations. However, unlike `lists`, ndarrays must contain elements of the same type.  

To import NumPy, it is standard to use the following import:  

```
bash$ python3
>>> import numpy as np
>>> 
```

To create an ndarray, or colloquially, a NumPy array, you can convert an existing `list` object into an ndarray or create an ndarray from scratch.  

```
>>> a = [1, 2, 3]
>>> a = np.array(a)
>>> a
array([1, 2, 3])
>>> b = np.array([1, 2, 3])
>>> b
array([1, 2, 3])
>>> c = np.array([1, 2, 3, 4])
>>> c
array([1, 2, 3, 4])
>>> d = np.array([[1, 2, 3], [4, 5, 6]])
>>> d
array([[1, 2, 3],
       [4, 5, 6]])
>>> e = np.array([[1, 2], [3, 4], [5, 6]])
>>> e
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> 
```

To check the dimensions, or shape, of an ndarray, you can simply access the `shape` attribute. This returns a tuple containing the dimensions of your array.  

```
>>> a.shape
(3,)
>>> b.shape
(3,)
>>> c.shape
(4,)
>>> d.shape
(2, 3)
>>> e.shape
(3, 2)
>>> 
```

Given two ndarrays of the same shape, you can perform various matrix operations across the values in the matrix. For example, you can compare the values, add the values, subtract the values, multiply the values, divide the values, or exponentiate the values.  

```
>>> a == b
array([ True,  True,  True])
>>> a + b
array([2, 4, 6])
>>> a - b
array([0, 0, 0])
>>> a / b
array([1., 1., 1.])
>>> a // b
array([1, 1, 1])
>>> a * b
array([1, 4, 9])
>>> a ** b
array([ 1,  4, 27])
>>> 
```

When working with arrays with different shapes, you may be able to broadcast the shapes of the array depending on whether the matrices have some dimensions that align.  

```
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (3,) (4,) 
>>> a + d
array([[2, 4, 6],
       [5, 7, 9]])
>>> 
```

To perform matrix operations, you can use some of the matrix operations from NumPy. For example, you can multiply matrices with `np.matmul`. For programs with many matrix multiplications, this may become unwieldy, so instead, you can use the `@` symbol as syntactic sugar for matrix multiplication.  

```
>>> np.matmul(d, e)
array([[22, 28],
       [49, 64]])
>>> np.matmul(e, d)
array([[ 9, 12, 15],
       [19, 26, 33],
       [29, 40, 51]])
>>> d @ e
array([[22, 28],
       [49, 64]])
>>> e @ d
array([[ 9, 12, 15],
       [19, 26, 33],
       [29, 40, 51]])
>>> 
```

Some operations may differ between what would mathematically be valid and how NumPy can interpret the operation. For example, you can use `np.matmul` to perform a dot product operation between one dimensional matrices of the same shape.  

```
>>> np.matmul(a, b)
14
>>> a @ b
14
>>> np.matmul(b, a)
14
>>> b @ a
14
>>> 
```

Additionally, matrix operations on one dimensional arrays are more flexible.  

```
>>> d
array([[1, 2, 3],
       [4, 5, 6]])
>>> a
array([1, 2, 3])
>>> np.matmul(d, a)
array([14, 32])
>>> d @ a
array([14, 32])
>>> 
```

To change the shape of an array, you can use the `np.reshape()` function. This keeps the data within the array but changes the order of the elements. Alternatively, you can invoke the `reshape` method on an ndarray.  
```
>>> np.reshape(a, (3, 1))
array([[1],
       [2],
       [3]])
>>> a.reshape((3,1))
array([[1],
       [2],
       [3]])
>>> a
array([1, 2, 3])
>>> d @ a.reshape((3,1))
array([[14],
       [32]])
>>> 
```

By default, this follows the row-major ordering in C-like languages. You can specify the ordering you wish using the `order` optional parameter.  

```
>>> d.reshape((3, 2), order='F')
array([[1, 5],
       [4, 3],
       [2, 6]])
>>> 
```

Furthermore, if you do not know the full dimensions of your array, but would like a specific earlier dimensions in the shape, you can use -1 to allow NumPy to infer the shape of your reshaped ndarray, as long as the total size is divisible by your specified dimensions.  

```
>>> d.reshape((6, -1))
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
>>> d.reshape((4, -1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot reshape array of size 6 into shape (4,newaxis)
>>> 
```

Given any ndarray, you can "flatten" the array by using the `ravel()` method. This returns a copy of the values in the array in one dimension. This has the effect of reshaping to dimensions (-1).  

```
>>> d.ravel()
array([1, 2, 3, 4, 5, 6])
>>> d.reshape((-1))
array([1, 2, 3, 4, 5, 6])
>>> 
```

Additionally, it is often useful to generate an array of zeros or ones of the same shape as an existing ndarray. Luckily, we can use `np.zeroes_like()` and `np.ones_like()` functions to create such ndarrays.  

```
>>> np.zeros_like(d)
array([[0, 0, 0],
       [0, 0, 0]])
>>> np.ones_like(d)
array([[1, 1, 1],
       [1, 1, 1]])
>>> 
```

Like lists, you can use slicing to access a view of an ndarray using the same syntax as you would with slice lists.  

```
>>> a[0]
1
>>> a[:-1]
array([1, 2])
>>> d[0]
array([1, 2, 3])
>>> d[0][:-1]
array([1, 2])
>>> d.ravel()[::2]
array([1, 3, 5])
>>> 
```

You can also treat NumPy ndarrays as matrices and transpose their orientation.  

```
>>> d = np.array([[1, 2, 3], [4, 5, 6]])
>>> d
array([[1, 2, 3],
       [4, 5, 6]])
>>> d.T
array([[1, 4],
       [2, 5],
       [3, 6]])
```

Finally, you can apply basic mathematical functions to elements in an ndarray.  

```
>>> np.max(d)
6
>>> np.min(d)
1
>>> np.log(d)
array([[0.        , 0.69314718, 1.09861229],
       [1.38629436, 1.60943791, 1.79175947]])
>>> np.cos(d)
array([[ 0.54030231, -0.41614684, -0.9899925 ],
       [-0.65364362,  0.28366219,  0.96017029]])
>>> np.sin(d)
array([[ 0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ]])
>>> 
```

As evident, NumPy offers a wide variety of matrix operations that allow easy to use ndarrays that are more efficient than using lists in Python. These ndarrays are crucial building blocks in other data science libraries, such as Pandas.  

# 4.5 Practical Pandas
Another common data science import is the Pandas package. Pandas allows the use of dataframes, which builds upon NumPy ndarrays with additional metadata. These dataframes are generally two dimensional ndarrays with row and column labels.  

To import Pandas, it is standard to use the following import:  

```
bash$ python3
>>> import pandas as pd
>>> 
```

To create a Pandas DataFrame, you can pass in a Python dictionary. The keys to the dictionary become the columns to the DataFrame. By default, the index (rows) of the DataFrame will be zero-indexed integers.  

```
>>> df = pd.DataFrame({ 'A' : [1, 2, 3], 'B' : [4, 5, 6], 'C' : [7, 9 ,9]})
>>> df
   A  B  C
0  1  4  7
1  2  5  9
2  3  6  9
>>> df.columns
Index(['A', 'B', 'C'], dtype='object')
>>> df.index
RangeIndex(start=0, stop=3, step=1)
>>> 
```

You can directly alter the index or columns of the DataFrame object by passing in an iterable of the same length.  
```
>>> df.index = [2, 4, 6]
>>> df.columns = ['a', 'b', 'c']
>>> df
   a  b  c
2  1  4  7
4  2  5  9
6  3  6  9
>>> 
```

An alternative to creating a DataFrame through a dictionary is to pass in an ndarray as input to the DataFrame or list. You can also pass in optional parameters for the index and columns of the DataFrame.  

```
>>> df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
>>> df
    c1  c2  c3
r1   1   2   3
r2   4   5   6
r3   7   8   9
>>> 
```

While these DataFrame examples are small, it may be infeasible to display a larger DataFrame. To take a peak at the first rows or last rows of the DataFrame, you can use the `head()` and `tail()` methods. You can specify the number of rows as an argument to how many rows to display.  

```
>>> df.head(2)
    c1  c2  c3
r1   1   2   3
r2   4   5   6
>>> df.tail(1)
    c1  c2  c3
r3   7   8   9
>>> 
```

Having row and column metadata is useful for accessing specific entries in the DataFrame by name. Otherwise, you may as well simply use an ndarray. To access entries by column, you can use similar syntax to accessing dictionaries by key. You can also access columns by accessing the column name like an attribute. However, there are advantages to accessing by column name, such as for selecting multiple entries in an order of your choosing.  

```
>>> df['c1']
r1    1
r2    4
r3    7
Name: c1, dtype: int64
>>> df.c1
r1    1
r2    4
r3    7
Name: c1, dtype: int64
>>> df[['c1', 'c2']]
    c1  c2
r1   1   2
r2   4   5
r3   7   8
>>> df[['c1', 'c2']]
    c1  c2
r1   1   2
r2   4   5
r3   7   8
>>> df[['c2', 'c2', 'c1']]
    c2  c2  c1
r1   2   2   1
r2   5   5   4
r3   8   8   7
>>> 
```

To access rows by the index, you can use `.loc`, with similar syntax for accessing the row names.  

```
>>> df.loc['r1']
c1    1
c2    2
c3    3
Name: r1, dtype: int64
>>> df.loc[['r1', 'r2', 'r1']]
    c1  c2  c3
r1   1   2   3
r2   4   5   6
r1   1   2   3
>>> 
```

To retrieve the NumPy ndarray from a given Pandas DataFrame, you can access the `values` attribute of the Pandas DataFrame. This will be in the same shape (index, columns) as the DataFrame.  

```
>>> df.values
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> assert (len(df.index), len(df.columns)) == df.values.shape
>>> 
```

With these ndarrays, you may want to check which values are present in the ndarrays. To find unique values, you can use either `pd.unique()` or `np.unique()` on an ndarray. In general, it is recommended to use `pd.unique()` if you simply want to find the unique values, as `np.unique()` will also sort the unique values. Thus, `pd.unique()` is an O(N) operation, whereas `np.unique()` will be O(NlogN), for N unique values. There are also some slight differences in usage. Using `np.unique()`, you can directly pass in a Pandas DataFrame, whereas you will need to `ravel()` the `values` attribute from the Pandas DataFrame using `pd.unique()`.  

```
>>> np.unique(df2)
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> pd.unique(df2.values.ravel())
array([1, 2, 3, 6, 5, 4, 7, 8, 9])
>>> 
```

Other than unique values, you may want to find a subset of values that are present in some other iterable. The `np.isin()` function allows you to return an one-hot encoding of booleans of whether or not each element in your Pandas DataFrame or NumPy ndarray is present in your other iterable.  

```
>>> np.isin(df2, [1, 2, 3])
array([[ True,  True,  True],
       [False, False, False],
       [False, False, False]])
>>> assert np.isin(df2, [1, 2, 3]).shape == df2.shape
>>> 
```

With Pandas DataFrames, you may encounter a situation where you may wish to combine two or more Pandas DataFrames together. If these Pandas DataFrames have the same columns, we can simply concatenate them together using `pd.concat`. This returns a new Pandas DataFrame containing the values of an iterable of Pandas DataFrames.  

```
>>> pd.concat([df, df2])
    c1  c2  c3
r1   1   2   3
r2   4   5   6
r3   7   8   9
r1   1   2   3
r2   6   5   4
r3   7   8   9
>>> pd.concat((df, df2))
    c1  c2  c3
r1   1   2   3
r2   4   5   6
r3   7   8   9
r1   1   2   3
r2   6   5   4
r3   7   8   9
>>> 
```

You can also merge Pandas DataFrames based on shared values in the same columns. This is useful for finding intersecting rows of two or more Pandas DataFrames. By default, using the `merge` method on a Pandas DataFrame with another Pandas DataFrame will return a new Pandas DataFrame with the rows that have the same values that are shared between the two Pandas DataFrames.  

```
>>> df.merge(df2)
   c1  c2  c3
0   1   2   3
1   7   8   9
>>> 
```

 Additionally, you can use specify "how" you want to merge the Pandas DataFrames. This allows for some basic Structured Query Language (SQL) commands, such as "left" and "right". Joining on "left" will include all values present on the "left" Pandas DataFrame (the Pandas DataFrame invoking the "merge") along with the intersecting rows, whereas joining on "right" will include all the values of the Pandas DataFrame that is input as the first argument. Of course, this will not be as useful if the Pandas DataFrames all share the same columns.  
 
```
>>> df.merge(df2, how='left')
   c1  c2  c3
0   1   2   3
1   4   5   6
2   7   8   9
>>> df.merge(df2, how='right')
   c1  c2  c3
0   1   2   3
1   6   5   4
2   7   8   9
>>> 
```

This difference is made more apparent when only some columns are shared. Here, "df" and "df3" share the columns "c1" and "c2", so the intersecting values (using the default "inner" join) will have the same values in those two columns. Upon using a "left join" or "right join", also known as an "left outer join" and an "right outer join" using SQL terminology, we will have values that aren't defined int he other Pandas DataFrame. Instead, we will see "NaN" values, which stand for "Not a Number".  

```
>>> df3 = pd.DataFrame([[1, 2, -3], [6, 5, -4], [7, 8, -9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c4'])
>>> df3
    c1  c2  c4
r1   1   2  -3
r2   6   5  -4
r3   7   8  -9
>>> df.merge(df3)
   c1  c2  c3  c4
0   1   2   3  -3
1   7   8   9  -9
>>> df.merge(df3, how='inner')
   c1  c2  c3  c4
0   1   2   3  -3
1   7   8   9  -9
>>> df.merge(df3, how='left')
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  NaN
2   7   8   9 -9.0
>>> df.merge(df3, how='right')
   c1  c2   c3  c4
0   1   2  3.0  -3
1   6   5  NaN  -4
2   7   8  9.0  -9
>>> 
```

Having "NaN" values will often cause issues in computational methods. To drop rows with "NaN" values, we can use the "dropna()" method.  

```
>>> left_df = df.merge(df3, how='left')
>>> left_df
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  NaN
2   7   8   9 -9.0
>>> left_df.dropna()
   c1  c2  c3   c4
0   1   2   3 -3.0
2   7   8   9 -9.0
>>> 
```

By default, "NaN" values will be dropped by row, which are along axis 0. You can specify which axis to use when dropping "NaN" values.  

```
>>> left_df.dropna(axis=0)
   c1  c2  c3   c4
0   1   2   3 -3.0
2   7   8   9 -9.0
>>> left_df.dropna(axis=1)
   c1  c2  c3
0   1   2   3
1   4   5   6
2   7   8   9
>>> 
```

In general, Pandas methods and functions will return new Pandas DataFrames. If you wanted to modify the current object, you can use the optional parameter "inplace" and set it to True. Here, we will replace the "NaN" values with 0 rather than dropping the "NaN" values.  

```
>>> left_df.fillna(0)
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  0.0
2   7   8   9 -9.0
>>> left_df
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  NaN
2   7   8   9 -9.0
>>> left_df.fillna(0, inplace=True)
>>> left_df
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  0.0
2   7   8   9 -9.0
>>> 
```

Moreover, you may wish to iterate over the values in a Pandas DataFrame. Two common ways are to use the "itertuples" and "iterrows" methods to obtain an iterable that you can loop over. Note that you can use a '*' in front of a variable name to expand multiple values into a tuple object.  

```
>>> for index, *values in left_df.itertuples():
...     print(index, values)
... 
0 [1, 2, 3, -3.0]
1 [4, 5, 6, 0.0]
2 [7, 8, 9, -9.0]
>>> for index, *values in left_df.iterrows():
...     print(index, values)
... 
0 [c1    1.0
c2    2.0
c3    3.0
c4   -3.0
Name: 0, dtype: float64]
1 [c1    4.0
c2    5.0
c3    6.0
c4    0.0
Name: 1, dtype: float64]
2 [c1    7.0
c2    8.0
c3    9.0
c4   -9.0
Name: 2, dtype: float64]
>>> for values in left_df.iterrows():
...     print(values)
... 
(0, c1    1.0
c2    2.0
c3    3.0
c4   -3.0
Name: 0, dtype: float64)
(1, c1    4.0
c2    5.0
c3    6.0
c4    0.0
Name: 1, dtype: float64)
(2, c1    7.0
c2    8.0
c3    9.0
c4   -9.0
Name: 2, dtype: float64)
>>> 
```

Additionally, like NumPy ndarrays, you can transpose Pandas DataFrames.  

```
>>> left_df.T
      0    1    2
c1  1.0  4.0  7.0
c2  2.0  5.0  8.0
c3  3.0  6.0  9.0
c4 -3.0  0.0 -9.0
>>> for index, *values in left_df.T.itertuples():
...     print(index, values)
... 
c1 [1.0, 4.0, 7.0]
c2 [2.0, 5.0, 8.0]
c3 [3.0, 6.0, 9.0]
c4 [-3.0, 0.0, -9.0]
>>> for index, *values in left_df.T.iterrows():
...     print(index, values)
... 
c1 [0    1.0
1    4.0
2    7.0
Name: c1, dtype: float64]
c2 [0    2.0
1    5.0
2    8.0
Name: c2, dtype: float64]
c3 [0    3.0
1    6.0
2    9.0
Name: c3, dtype: float64]
c4 [0   -3.0
1    0.0
2   -9.0
Name: c4, dtype: float64]
>>> for values in left_df.T.iterrows():
...     print(values)
... 
('c1', 0    1.0
1    4.0
2    7.0
Name: c1, dtype: float64)
('c2', 0    2.0
1    5.0
2    8.0
Name: c2, dtype: float64)
('c3', 0    3.0
1    6.0
2    9.0
Name: c3, dtype: float64)
('c4', 0   -3.0
1    0.0
2   -9.0
Name: c4, dtype: float64)
>>> 
```

Finally, you may wish to save your Pandas DataFrames into secondary storage, where it will be saved when your program finishes. One common format to save these files is as Comma Separated Values (CSV). We can simply do this using the `to_csv()` method for any Pandas DataFrame.  

```
>>> left_df
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  0.0
2   7   8   9 -9.0
>>> left_df.to_csv("left_df")
>>> 
```

To load a CSV file in Python, we can use the `pd.read_csv()` function to load a CSV file into a Pandas DataFrame.  

```
>>> left_df = pd.read_csv("left_df.csv")
>>> left_df
   Unnamed: 0  c1  c2  c3   c4
0           0   1   2   3 -3.0
1           1   4   5   6  0.0
2           2   7   8   9 -9.0
>>> 
```

As you see, we have a slight indexing issue, as our original index did not have an index name, and was thus, left as "Unnamed: 0" when loaded back into memory. To indicate that a specific column should be used as an index, we can specify an "index_col" number when reading the CSV.  

```
>>> left_df = pd.read_csv("left_df.csv", index_col=0)
>>> left_df
   c1  c2  c3   c4
0   1   2   3 -3.0
1   4   5   6  0.0
2   7   8   9 -9.0
>>> 
```

Now, we can reliably save and store Pandas DataFrames to and from memory.  

# 4.6 Pretty Pickle
While you can save Pandas DataFrames as CSV files, it may become too slow and inefficient to save large Pandas DataFrames into CSV files. Additionally, you may have other Python objects that are not as easily formatted as CSV. Instead, you can save the binary values of the Python object using the `pickle` library.  

```
>>> import pickle
>>> radish = [1, 2, 3]
```

To save an object into a `pickle` file, you need to open a file with "wb" permission, as you are writing to a file in binary mode.  

```
>>> with open("radish.pkl", 'wb') as f:
...     pickle.dump(radish, f)
... 
>>> 
```

To load the pickle file again, you will need to open the file with "rb" permission to read a file in binary mode into memory.  

```
>>> import pickle
>>> with open("radish.pkl", 'rb') as f:
...     radish = pickle.load(f)
... 
>>> radish
[1, 2, 3]
```

Loading pickle files is more efficient, as these are already Python objects. However, this also poses a significant security risk, as it is more difficult to inspect the contents of a pickle file compared to a CSV. Do NOT open a pickle file unless you are absolutely certain that it is safe and trusted.  

# 4.7 Succinct Summary
Python is a simple and easy to understand programming language. The basic syntax is much more similar to English and more user friendly than the more rigid C-like languages. Moreover, Python has a wide variety of libraries that can be used for nearly any imaginable task. While interpreted code is almost always slower than compiled code, Python libraries can leverage the improved runtime efficiency of compiled C code to achieve a balance between ease of use and high performance. In this chapter, we visited some of the most popular, general use and data science libraries that Python has to offer. More advanced and machine learning specific Python libraries are beyond the scope of this course.  

#### [Return to Main Table of Contents](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/README.md#table-of-contents)
Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
