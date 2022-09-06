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

Argparse provides a modern approach to parsing command line arguments. For further reference, please refer to the [official argparse documentation](https://docs.python.org/3/library/argparse.html). Also, you may wish to reference the `system` and `os` modules, which are often used together with argparse.  

# 4.2 Logical Logging
# 4.3 Potent PDB
# 4.4 Nifty Numpy
# 4.5 Practical Pandas
# 4.6 Pretty Pickle
# 4.7 Succinct Summary

Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
