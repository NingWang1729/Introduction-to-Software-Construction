# Chapter 4: Python Libraries

4. [Python Libraries](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#chapter-4-python-libraries)
  - 4.1 [Agreeable Argparse](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#41-agreeable-argparse)
  - 4.2 [Logical Logging](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#42-logical-logging)
  - 4.3 [Potent PDB](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#43-potent-pdb)
  - 4.4 [Nifty NumPy](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#44-nifty-numpy)
  - 4.5 [Practical Pandas](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#45-practical-pandas)
  - 4.6 [Pretty Pickle](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#46-pretty-pickle)
  - 4.7 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%204:%20Python%20Libraries.md#47-python-libraries)

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

# 4.4 Nifty Numpy
NumPy is one of the most commonly used packages for data science in Python. While Python has the native `list` data structure, more computational programs will often require large, multi-dimensional arrays. As an interpreted languages, Python is simply too slow for larger applications. However, with compiled C code, packages such as NumPy allow the user to enjoy both the easy to use syntax of Python along with the efficiency of compiled C libraries. NumPy's primary usage revolves the `ndarray`, which allows versatile, multi-dimensional arrays, as well as basic high level math operations. However, unlike `lists`, ndarrays must contain elements of the same type.  

To import NumPy, it is standard to use the following import:
```
bash$ python3
>>> import numpy as np
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
```

By default, this follows the row-major ordering in C-like languages. You can specify the ordering you wish using the `order` optional parameter.  

```
>>> d.reshape((3, 2), order='F')
array([[1, 5],
       [4, 3],
       [2, 6]])
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
```

Given any ndarray, you can "flatten" the array by using the `ravel()` method. This returns a copy of the values in the array in one dimension. This has the effect of reshaping to dimensions (-1).  

```
>>> d.ravel()
array([1, 2, 3, 4, 5, 6])
>>> d.reshape((-1))
array([1, 2, 3, 4, 5, 6])
```

Additionally, it is often useful to generate an array of zeros or ones of the same shape as an existing ndarray. Luckily, we can use `np.zeroes_like()` and `np.ones_like()` functions to create such ndarrays.  

```
>>> np.zeros_like(d)
array([[0, 0, 0],
       [0, 0, 0]])
>>> np.ones_like(d)
array([[1, 1, 1],
       [1, 1, 1]])
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
```

As evident, NumPy offers a wide variety of matrix operations that allow easy to use ndarrays that are more efficient than using lists in Python. These ndarrays are crucial building blocks in other data science libraries, such as Pandas.  

# 4.5 Practical Pandas
# 4.6 Pretty Pickle
# 4.7 Succinct Summary

Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
