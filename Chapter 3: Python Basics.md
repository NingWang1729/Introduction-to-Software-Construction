# Chapter 3: Python Basics

3. [Python Basics](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%203:%20Python%20Basics.md#chapter-3-python-basics)
- 3.1 [Simple Syntax](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%203:%20Python%20Basics.md#31-simple-syntax)
- 3.2 [Building Blocks](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%203:%20Python%20Basics.md#32-building-blocks)
- 3.3 [Critical Classes](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%203:%20Python%20Basics.md#33-critical-classes)
- 3.4 [Advanced Actions](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%203:%20Python%20Basics.md#34-advanced-actions)
- 3.5 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%203:%20Python%20Basics.md#35-succinct-summary)

## 3.1 Simple Syntax

Python is the easiest to learn programming language. With English-like syntax, it is easy for anyone who is fluent in English to pick up Python as a programming language, especially if they are already familiar with traditional, C-like object oriented languages. In this chapter, we will cover many of the core Python syntax and features, excluding any library imports, which will be covered in the next chapter. In general, you will be writing Python code in a Python script, a Python source code file with the ".py" extension. To start working with Python, however, we will use the command `python3`, which will open the Python 3 REPL in the terminal. You may be able to use just `python` to run Python 3. If you are running a Python script named "foo.py", you can run the script using `python3 foo.py`, or use the corresponding path for your Python command.  

For the purposes of this tutorial, we will be using Python 3 version 3.10 or higher, rather than the older Python 2, which has slightly different syntax from Python 3. From here on out, we will be referring Python exclusively to Python 3, unless otherwise specified. Some later features in the "Advanced Actions" sub-chapter will also require Python version 3.10 or higher, while the rest of the contents will only be requiring Python version 3.7 or higher. To check `which` version you are using, you can use `which` to find the path where the command is located, and you can use "--version" flag after the respective `python` command to check for the exact version number you are using.  

```
bash$ python3
>>> 
```

The Python REPL will use ">>> " to delimit the start of the active Python command line. Rather than using shell commands, we will be evaluating lines of Python code. Before writing any code, it is useful to know that unlike most languages, Python is very strict with indentation. You can use either two spaces, four spaces, or tabs, but you cannot mix and match. Unless the syntax requires indentation, do not indent lines of Python code.  

As with most programming languages, we will begin with a simple program to print out the `str` "Hello World". A `str`, string, contains a sequence of characters, enclosed within either double quotes, "", or single quotes, ''. In Python, `str` is an example of a `type`, which describes what category an object falls under. Objects can be thought of as the building blocks of any object oriented programming (OOP) language. Objects in Python contain data and methods, which are functions that belong to an object or class. Objects are instances of a class, which is the kind of object the object is. In this case, the `str` class falls under the `type`. In other words, strings are a subclass of types. In English, this just means that things that look like "some text" are strings.  

```
>>> type("Hello World")
<class 'str'>
>>> type(str)
<class 'type'>
>>> 
```

Python initially required using single quotes for strings. Soon, however, the developers allowed using double quotes for strings to appease newcomers who were more familiar with C-like languages, where chars used single quotes and strings used double quotes. To print out an object, such as a string, we will use the `print` function by passing in the string, "Hello World", as its positional "value" argument. Positional arguments are required and must be in the corresponding position for the code to run as intended. Also note that `print` will add a newline at the end by default, similar to the `print` shell command.  

```
bash$ print Hello World
Hello World

>>> print("Hello World")
Hello World
>>> 
```

The `print()` function has 4 optional parameters. To find out what they are, we will need some help. Rather than using the `man` shell command, we will use the `help` function, passing in the print function as its argument. As with most manual pages, you will need to hit 'q' on your keyboard to exit the manual. To open up the help utility to search for help on various topics, you can use `help()` without any input argument. To exit this interactive tutorial, just enter "quit" into the terminal. The '#' character creates as a single line comment. This allows the user to add comments to the code. The text until the '\n' at the end of the line will not be evaluated as code. It is important to use comments to help explain your code for other users to understand. Here, we used a comment to show explain the usage of the help manual and a comment to display the usage of the `print` function, as described in said help manual.  

```
>>> help(print) # Hit 'q' when finished reading the help manual
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
```

The `print` function has the default arguments "sep", "end", "file", and "flush". Default arguments to a function can be readily distinguished from positional arguments as they must always come after all positional arguments and will have an '=' after the argument, which specifies the default value. To change the value of an default argument, simply add the '=' followed by the intended value. The "..." indicates you can input more than one argument. Thus, you can print multiple objects using the `print` function, separated by the "sep" string. After printing out all the input objects, the `print` function will end by printing out the "end" string. For now, you can ignore the "file" and "flush" arguments until more experienced with either Python or C-like languages.  

```
>>> print("Hello", "World", sep='_', end='!\n')
Hello_World!
>>>
```

Note that functions are evaluated only when they have the parentheses, "()", after the name of the function. Otherwise, the function name acts the same any other identifier, aka variable, as `print` simply acts as a reference to a function that prints out objects. Everything in Python is an object, and identifiers are just pointers to objects. Thus, we can assign values, using the assignment operator `=`, by passing the object reference to the identifier.  

```
>>> foo = print
>>> foo("bar")
bar
>>> 
```

The opposite of printing out to standard output is reading from standard input. You can use the `input` function to read strings of text. Two other `type`s to know are the numerical data types `int`, which are integers, and `float`, which are floating points (aka decimals). If you want to read an `int` or a `float`, you can cast them `str` with `int` or `float`. To convert between data types, you can use the type's corresponding identifier as a function, if valid.  

```
>>> input()
foo
'foo'
>>> float(input())
1.0
1.0
>>> int(input())
1
1
>>> int(input())
1.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.0'
>>> float(input())
1.0 is a float.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '1.0 is a float.'
```

This also works for casting integers to floating point numbers, and vice versa. Notably, Python rounds towards 0 for casting integers to floats.  

```
>>> int(0.9)
0
>>> int(1.0)
1
>>> int(1.1)
1
>>> int(-0.9)
0
>>> int(-1.0)
-1
>>> int(-1.1)
-1
>>> float(1)
1.0
>>> 
```

Using the assignment operator, you can assign values or references to identifiers. Python is a dynamically typed language, as the code is evaluated as it is interpreted at run time. This means you do not need to specify a `type` for your identifiers, and the same identifier can be assigned references or literals of different types. Note that in the REPL, you can enter an identifier that has been defined to examine its value. However, you cannot assign values or references to literals, which are not identifiers.  

```
>>> foo = "bar"
>>> foo
"bar"
>>> one = 1
>>> one
1
>>> foo = one
>>> foo
1
>>> fou
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fu' is not defined
>>> 1 = one
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> 
```

Some operations will change the `type` of the objects involved. For example, an arithmetic operation involving an `int` and a `float` will return a float. If performing division, however, you can pick between integer division with `//`, or non-integer divsion, using `/`. Unlike casting a `float` to `int`, however, integer division will round towards negative infinity, rather than rounding towards zero.  

```
>>> 1 + 1.0
2.0
>>> 1 / 2
0.5
>>> - 1 // 2
-1
>>> 
```

Other common arithmetic operations include modulus division (i.e. remainders) and exponentiation. You can also use the `pow` function for exponentiation. The order of operations in Python mostly follows the Parentheses, Exponents, Multiplication and Division, and Addition and Subtraction (PEMDAS) rule. However, only parentheses, "()" are allowed for changing precedence, as only the regular parentheses can be used for grouping together function calls. Also, it is useful to note that floating point numbers may have slight inaccuracies, due to the implementation of floating numbers in binary format.  

```
>>> 1 % 2
1
>>> 2 ** 3
8
>>> pow(2, 3)
8
>>> 1.1 ** 2
1.2100000000000002
>>> 9 ** 0.5
3.0
>>> 2 ** 2 / 2
2.0
>>> 2 % 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 
```

Strings can be concatenated with the addition operator. However, unlike some languages, integer types are not implicitly cast to string. Instead, you can use formatted string literals, or f-strings, to incorporate objects into a string. With a lowercase 'f' in front of the opening quotation, either single or double, you can create an f-string. To insert an object, simply pass it in with curly braces {}. This can be any valid piece of python code. You can also use the `format` method for regular strings to insert objects on the fly with keyword arguments. Floating point formatting can be specified using a colon inside the curly brace after the object.__

```
>>> "foo" + "bar"
'foobar'
>>> 1 + "1"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> f"One equals {1}."
'One equals 1.'
>>> f"This is a function: {print}."
'This is a function: <built-in function print>.'
>>> foo = 'bar'
>>> f"{foo}"
'bar'
>>> "Foo{fou}".format(fou = foo)
'Foobar'
>>> "Hello {place}".format(place = "world")
'Hello world'
>>> f"Easy as Pi: {3.1415:.2f}"
'Easy as Pi: 3.14'
>>> "Two decimals of Pi: {pi:.2f}".format(pi = 3.1415)
'Two decimals of Pi: 3.14'
>>> "Three digits of Pi: {pi:.3}".format(pi = 3.1415)
'Three digits of Pi: 3.14'
>>> 
```

Working with strings in Python is easy. To `find` sub-strings, you can use the `find` string method, which returns the zero-based index of the start of the first instance of the target sub-string. If there is no match, the `find` method returns -1. You can also pass in default arguments for the start and end of the string to search for the value.  

```
>>> "'foobar is not fubar' -- foo".find("foo")
1
>>> "'foobar is not fubar' -- foo".find("fou")
-1
>>> "'foobar is not fubar' -- foo".find("foo", 10)
25
>>> "'foobar is not fubar' -- foo".find("not", 5, 10)
-1
>>>
```

Some other common uses for strings include reversing strings and taking sub-strings out of the string. In Python, this can be done with slicing. To slice a sequence, such as a string, you can put square brackets, "[]" at the end of a `str` or `list`. Inside the square brackets, you can put delimiters separated by colons. The syntax for list slicing is `[start:end:stride]`, where "start" has a default value of 0, "end" represents the index to stop at (exclusive), and "stride" represents how far to move to the next index, with a default value of 1. The "start" and "end" can also be negative, where you index from the end, or right side, of the sequence. Conveniently, this also allows for reversing strings, using negative strides. You can also leave out colons in the slicing. Notably, if you use no colons at all, you are simply taking the value at the index.  

```
>>> "foobar"[0:3:1]
'foo'
>>> "foobar"[:3]
'foo'
>>> "foobar"[3:]
'bar'
>>> "foobar"[::2]
'foa'
>>> "foobar"[::-1]
'raboof'
>>> "foobar"[-1::-1]
'raboof'
>>> "foobar"[-1:2:-1]
'rab'
>>> "foobar"[-4::-1]
'oof'
>>> "foobar"[0]
'f'
>>> "foobar"[-1]
'r'
>>> "foobar"[::0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: slice step cannot be zero
>>> 
```

## 3.2 Building Blocks

Strings are an example of a sequence, which are ordered groups of objects. Strings in Python are immutable, meaning that a string cannot change its value once it is initialized. Changing the value of an identifier that currently has a string value is simply assigning a different object reference to that identifier. The most commonly used type of sequence in Python is the `list`, which is equivalent to dynamically allocated arrays in other languages. Python lists can contain objects of any type and are mutable, meaning you can change the values inside the `list`. When initialized, lists have a certain amount of memory allocated for storing the references. If a list runs out of space, it will allocate twice the amount of memory to store these references, and copy over the previously stored elements' references. Thus, inserting elements into a list has an amortized time complexity of O(1), meaning insertion is very fast in a Python list.  

To initiate a `list`, you can either use square brackets, "[]", or the `list` function. To start with an empty list, you would leave the `list` empty, or not put any values in it at the start. To initialize a list with square brackets with some starting values, you can separate the objects using commas, ','. While spaces after the commas are not strictly necessary, having clear spacing and indentation style that you maintain over time will help make your code more clear and easier to read. To convert an existing sequence to a list, you can pass the reference to the sequence object to the `list` function. To find the length of a sequence, you can pass the reference to the sequence into the `len` function.  

```
>>> []
[]
>>> len([])
0
>>> len(foo)
3
>>> list()
[]
>>> list(foo)
['b', 'a', 'r']
>>> len(['f', 0, 'o'])
3
>>> 
```

Strings and lists are often used together. For example, you might want to split a string in to a list of substrings, based on some delimiter. This is useful for parsing words in a sentence. Inversely, you may want to join a `list` of strings together, using some delimiter between strings. The `split` and `join` functions allow easy string manipulation.  

```
>>> "This is a sentence.".split(' ')
['This', 'is', 'a', 'sentence.']
>>> " ".join(['This', 'is', 'a', 'sentence.'])
'This is a sentence.'
>>> 
```

While one of the flexible benefits of `lists` is their mutable nature, we may want a sequence that stores multiple objects but is immutable. For example, you may want a "list" of items that does not change, regardless of the rest of the code. One example may be to store the days of the week in an immutable sequence. In Python, you can create a `tuple` using parentheses, "()", with elements separated by commas. You can slice the tuples the same way you would with any other sequence.  

```
>>> (1, '2', "3")
(1, '2', 3)
>>> (1, '2', "3")[0]
1
>>> (1, '2', "3")[::2]
(1, '3')
```

Furthermore, you can unpack the values in a tuple. Crucially, unpacking allows directly swapping identifier references without defining a temporary helper variable. While this can be done with other sequence types, this is generally avoided, as list are `mutable`, meaning the length of the `list` may change, and there are significantly fewer instances where unpacking a `str` would be the first solution that would come to mind, as most developers would instinctively just index the `str`. This unpacking also works with lists, but again, are not used as often compared to unpacking tuples.  

```
>>> one, two, three = (1, '2', "3")
>>> one, two, three
(1, '2', '3')
>>> f, o, o = foo
>>> f
'b'
>>> o
'r'
>>> o
'r'
>>> f, o = o, f
>>> f
'r'
>>> o
'b'
```

Essentially, Python can unify identifiers on the left hand side with values on the right hand side, evaluating from left to right.

```
>>> [a, b] = [1, 2]
>>> a
1
>>> b
2
>>> c, d = [3, 4]
>>> c
3
>>> d
4
>>> [a, b] = (b, a)
>>> a
2
>>> b
1
>>> a, b = 1, 2
>>> a, b = b, a
>>> a
2
>>> b
1
>>> a, b = 1, 2
>>> a, b, a = b, a, a
>>> a
1
>>> b
1
>>> 
```

You can `append` items to a `list`, which adds an element to the end (right side) of a list. You can also specify an index to `insert` into a list, specifying the index, followed by the object, separated by a comma. Inversely, you can remove and return an item from the end of a list with the `pop` method, and you can `pop` from an index by specifying an index to `pop` from.

```
>>> my_list = [1, 2, 3]
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> my_list.pop()
4
>>> my_list
[1, 2, 3]
>>> my_list.insert(0, 0.0)
>>> my_list
[0.0, 1, 2, 3]
>>> my_list.pop(0)
0.0
>>> my_list
[1, 2, 3]
>>> 
```

If you have multiple identical values to add to a list, you can use the `*` operator as syntactic sugar as a shorthand notation for specifying a number of repeated elements.  

```
>>> [0] * 10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> 
```

For some lists, you can use the `min`, `max`, and `sum` functions over a list to obtain the smallest value, largest value, and sum of the elements (for numerical data types). These will be using the built-in Python functions.  

```
>>> min([_ for _ in range(10)])
0
>>> max([_ for _ in range(10)])
9
>>> sum([_ for _ in range(10)])
45
>>> 
```

You will often want to sort and reverse sequences. The `sorted` function will return a `list` of the elements of a sequence. However, this only works when the elements in the sequence are all supported by the less than operator, '<'. Additionally, you can also change the sort order from ascending to descending by setting the default argument "reverse" to `True`. With mutable sequences, such as a `list`, you can sort in place using the `sort` method.  

```
>>> sorted(foo)
['a', 'b', 'r']
>>> sorted((1, '2', "3"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> sorted((1, 2, 3), reverse=True)
[3, 2, 1]
>>> my_list = [1, 2, 3]
>>> my_list.sort(reverse=True)
>>> my_list
[3, 2, 1]
>>> 
```

Sometimes, you will want an unordered sequence with no duplicate values. In python, you can use a `set`, which is uses curly braces, "{}", with elements separated by commas. However, to initialize an empty set, you must use `set()`, as this would conflict with an empty dictionary, which will be described shortly. To remove an element from a `set`, you can use the remove method. Since a set is unordered, you can `pop` from a set, but the element removed will be arbitrary. You can remove a specific element using the `remove` method, if it exists. It is useful to use sets for operations, such as `union` and `intersection`.  

```
>>> my_set = set()
>>> my_set.add(1)
>>> my_set.add(1)
>>> my_set.add(3)
>>> my_set.add(2)
>>> my_set
{1, 2, 3}
>>> my_set.add(5)
>>> my_set
{1, 2, 3, 5}
>>> my_set.remove(5)
>>> my_set
{1, 2, 3}
>>> my_set.remove(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5
>>> your_set = {2, 4, 6}
>>> my_set.union(your_set)
{1, 2, 3, 4, 6}
>>> my_set.intersection(your_set)
{2}
>>> 
```

While Python does not have built-in ordered sets, you can use a Python dictionary instead. A `dict` is the equivalent to a hashmap in other languages, where you store key-value pairs. You can initialize an empty `dict` using either curly braces, "{}", or using the `dict` function. To initialize a `dict` with key-value pairs, you can have the pairs separated using commas, as per usual, but the key-values are delimited using colons. To access values, you can use square brackets to access values by their key. To insert a value into a `dict`, you can use square brackets to assign a value to the key. As of Python 3.7, dictionaries in Python are ordered, so you can use the keys of a dictionary as an ordered set.  

```
>>> my_dict = {}
>>> my_dict = dict()
>>> my_dict = { "foo" : foo }
>>> my_dict["fou"] = "baz"
>>> my_dict["fou"]
'baz'
>>> my_dict.keys()
dict_keys(['foo', 'fou'])
>>> my_dict.values()
dict_values(['bar', 'baz'])
>>> my_dict
{'foo': 'bar', 'fou': 'baz'}
>>>
>>> my_dict["foobar"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foobar'
>>> 
```

To check if a key is in a dictionary, you can use the `in` keyword. This can be used to avoid key errors, in conjunction with an if-statement. The syntax for these control structures is to have a colon at the end of the control statement, with an indentation to indicate which lines of code fall under the control. With Python, the "else-if" is simplified to the `elif` keyword. In the REPL, the ... provide the necessary padding for the indentation to line up. It is not part of the Python code itself. Note that the `boolean` values in Python are `True` and `False`.  

```
>>> "foo" in my_dict
True
>>> "foobar" in my_dict
False
>>> if "foobar" in my_dict:
...     print(my_dict["foobar"])
... elif "foo" in my_dict:
...     print(my_dict["foo"])
... else:
...     print("baz")
... 
bar
>>> 
```

Following conditionals, there are two basic loops in Python, which are the `for` loop and `while` loop. A `while` loop runs until the condition is `False`, similar to most languages. The `for` loop in python is closer to a "for-each" loop in other languages, where you can looping over a sequence. To mimic an integer based for loop, we can use a `range`, which works similar to the slicing syntax. You can use the `break` keyword to `break` out of a loop, which returns the control to the indentation level before the loop, or the `continue` keyword, which stops running the code in the loop and goes back to the start of the loop at the next iteration.  

```
>>> while True:
...     break
... 
>>> range(10)
range(0, 10)
>>> for i in range(10):
...     print(i)
... 
0
1
2
3
4
5
6
7
8
9
>>> for _ in range(0, 12, 3):
...     if _ % 2 == 0:
...             continue
...     print(_)
... 
3
9
>>> _
9
>>> for _ in [_]:
...     _ += 1
... 
>>> _
10
>>> 
```

For loops are often also combined with the `zip` and `enumerate` functions, which allow for more detailed iteration. The `enumerate` provides a tuple of the index of an element, along with the element itself, at the current iteration. The `zip` function allows you to iterate over multiple sequences at the same time.  

```
>>> for index, value in enumerate(['a', 'b', 'c']):
...     print(index, value)
... 
0 a
1 b
2 c
>>> for digit, alpha in zip([1, 2, 3], ['a', 'b', 'c']):
...     print(digit, alpha)
... 
1 a
2 b
3 c
>>> 
```

Note that the underscore, '_', is often used as a placeholder identifier that will generally not be used later. However, it is still a valid variable and within the scope of the program after the loop finishes. The underscore is often also used as a placeholder for list comprehensions, which are syntactic sugar for creating lists. List comprehensions make it easy to modify values from an existing sequence, as well as filter out certain values. You can also use `lambda` functions, or unnamed/anonymous functions, to create a temporary function. Note that you may need careful parentheses placement to ensure the code is evaluated in the intended order.  

```
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [_ for _ in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [_ ** 2 for _ in range(10) if _ % 2 == 1]
[1, 9, 25, 49, 81]
>>> [_ ** 2 for _ in range(10) if (lambda x : "1" in str(x ** 2))(_) ]
[1, 16, 81]
>>> [(lambda x : x ** 2 if "1" in str(x ** 2) else x)(_) for _ in range(10)]
[0, 1, 2, 3, 16, 5, 6, 7, 8, 81]
>>> [lambda x : x ** 2 if "1" in str(x ** _) else x for _ in range(10)][2](10)
100
>>> 
```

As the readability of lambda functions is usually lower than named functions, some consider it bad practice to use lambda functions at all. Instead, you can declare named functions using the `def` keyword, followed by the name of the function and any arguments enclosed in parenthesis. You can also have keyword arguments, or default arguments, to make arguments optional. It is important to note that all keyword arguments must follow non-keyword arguments. It is also sometimes useful to take in a variable number of arguments. These identifiers have a * in front of the name. Note that the '*' is not part of the identifier name, and that the type of the identifier will be a `tuple`.  

```
>>> def square(x):
...     return x ** 2
... 
>>> square(2)
4
>>> square(-1)
1
>>> def power(base, exponent=2):
...     return base ** exponent
... 
>>> power(2, 4)
16
>>> power(3, 3)
27
>>> def power(*bases, exponent=2):
...     return [base ** exponent for base in bases]
... 
>>> power(1, 2, 3)
[1, 4, 9]
>>> power(1, 2, 3, exponent=4)
[1, 16, 81]
>>> power(exponent=10000, 1, 2, 3)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> def powerful(*bases):
...     return type(bases) == tuple
... 
>>> powerful()
True
>>>
```

To return a value from a function, you can use the `return` keyword. In Python, you can return a tuple by simply putting multiple values after a `return` statement, separated by commas. This is particularly useful when modifying a fixed number of objects and can help avoid functions with side effects. If there is no `return` keyword, the function will return `None`.  

```
>>> def hello_world():
...     print("Hello World")
... 
>>> hello_world()
Hello World
>>> hi = hello_world()
Hello World
>>> hi
>>> type(hi)
<class 'NoneType'>
>>> hi is None
True
```

In general, `None` and `[]` will be treated as `False` in conditionals, while most other objects will be regarded as `True`. Given a sequence of `booleans`, you can use `all` and `any` to check for certain conditions.  

```
>>> []
[]
>>> if []:
...     print("Non-empty")
... 
>>> if [1]:
...     print("Non-empty")
... 
Non-empty
>>> all([True, False])
False
>>> any([True, False])
True
>>> all([True, True])
True
```

You can also use binary logical operators on booleans, such as `and`, `or`, and `not`. In contrast, Python does not support C-like operators, such as "&&", "||", and "!".  
 
```
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> not True
False
>>> not False
True
>>> not None
True
>>> not []
True
>>> 
```

However, Python does support bitwise operators, such as bitwise AND, '&', bitwise OR, '|', bitwise XOR, '^', bitwise NOT, '~', and bitwise shifts, '<<' and '>>'. These compare use the bits of the binary representations of objects. The 8-bit version of the binary representation is shown in the comments. Python uses Two's Complement for its binary representations of signed integers. As an aside, the first bit of a signed integer represents the sign, with 1 indicating negative and 0 indicating non-negative. To represent a negative number, take the binary representation of the positive number, flip every bit, and add 1. Unlike other languages, there is no explicit upper or lower bound on integers.  

```
>>> 4 & 2 # 0000 0100 & 0000 0010
0 # 0000 0000
>>> 5 & 3 # 0000 0101 & 0000 0011
1 # 0000 0001
>>> 4 | 3 # 0000 0100 | 0000 0011
7 # 0000 0111
>>> 3 ^ 1 # 0000 0011 ^ 0000 0001
2 # 0000 0010
>>> ~4 # 0000 0100
-5 # 1111 1011
>>> ~0 # 0000 0000
-1 # 1111 1111
>>> 
```

## 3.3 Critical Classes

Python is an object-oriented programming (OOP) language, meaning its basic building blocks revolve around objects, which are instances of classes. To create a class, you can use the keyword `class`, followed by the name of your class and a colon. Within each class, there are class methods, which allow the object to call pieces of code, and attributes, which are objects that belong to the class. Every class must have a constructor, which is called upon instantiating the class. If the user does not define one, Python will have a default constructor that does not do anything special. This constructor will always have the name `__init__`. Note that we used `pass` to avoid adding any code to the "animal" class. This is due to Python syntax not allowing colons without any lines of code indented afterwards. The keyword `pass` is a "no-op", which is code that simply exists but does not do anything. Class methods will also always have `self`, a reference to the instance of the class, as the first positional argument.  

```
>>> class animal:
...     pass
... 
>>> animal.__init__
<slot wrapper '__init__' of 'object' objects>
>>> class animal:
...     def __init__(self, species):
...         self.species = species
>>> a = animal("birb")
>>> 
```

Classes have attributes, which are stored as identifiers that belong to the class. The "dot" operator allows anyone to access attribute or methods from the class. In Python, there is no such thing as a private variable. Instead, the naming of the attribute or method should indicate whether outside actors should interact directly with said identifier.  

```
>>> a.species
'birb'
>>> a.species = 'snek'
>>> a.species
'snek'
>>> 
```

In Python, you can use two underscores in front of an attribute or method to mangle the name of the attribute or method, which will change the name of said attribute or method to an underscore appended in front of the name of the class, followed by two underscores, and then the original "true name" of the attribute or method. This will make it more difficult to access the attribute or method by accident but does not prevent access. This allows developers who know what they are doing to interact more directly with their code. As this mangling can be tedious to deal with, it is recommended to use just a single underscore to indicate intended "private" identifiers instead. In the REPL, it is difficult to add newlines for spacing conventions. In a python file, it is recommended to use one line of spacing in between methods, and two lines of spacing between functions and classes.  

```
>>> class demo:
...     def __init__(self):
...             self.__private_attribute = None
...             self._protected_attribute = None
...             self.public_attribute = None
...     def __private_method(self):
...             pass
...     def _protected_method(self):
...             pass
...     def public_method(self):
...             pass
... 
>>> print(demo.__dict__)
{'__module__': '__main__', '__init__': <function demo.__init__ at 0x2a478b32f7c0>, '_demo__private_method': <function demo.__private_method at 0x2a475b32f450>, '_protected_method': <function demo._protected_method at 0x2a475b32f0c0>, 'public_method': <function demo.public_method at 0x2a475b32f3d0>, '__dict__': <attribute '__dict__' of 'demo' objects>, '__weakref__': <attribute '__weakref__' of 'demo' objects>, '__doc__': None}
```

Every object will have a `__dict__` attribute, which returns a `dict` of its attributes. These methods with double underscores are special and referred to as "dunder" or "magic" methods. You can override these methods by defining a method with the same name (i.e. making your own `__init__` constructor). Another such method is the `__new__` method, which creates the object before `__init__` initializes the object. Two more useful methods to override are the `__str__` and `repr` methods. The `__str__` method is intended to provide a string to informally represent or summarize the object, while the `__repr__` method is intended to provide a more comprehensive representation of the object.  

```
>>> class animal:
...     def __init__(self, species):
...         print(f"A {species} appeared.")
...         self.species = species
...         self.hp = 1
...         self.atk = 1
...     def eat(self, prey):
...         if self.atk >= prey.hp:
...             self.hp += prey.hp
...             self.atk += prey.atk
...             prey.hp = 0
...         else:
...             print("The prey escaped!")
...     def __str__(self):
...         return f"{self.species}"
...     def __repr__(self):
...         return f"A {self.species} with {self.hp} hp and {self.atk} atk"
... 
>>> bird = animal("bird")
A bird appeared.
>>> bug = animal("bug")
A bug appeared.
>>> bird.eat(bug)
>>> bird
A bird with 2 hp and 2 atk
>>> bug
A bug with 0 hp and 1 atk
>>>
```

While classes are cool, animals have an evolutionary hierarchy. Thus, it is useful to have polymorphism in class hierarchies. For example, we can use a subclass of the animal class for the species of "birb" and "bug". A sub-class will have all the methods from its super class as well as exclusive methods of its own. You can access super class methods by accessing methods or attributes from `supper()`. Also notice how passing in an animal object as an argument to an animal object calls the `__str__` method of the animal, rather than the `__repr__` method.  

```
>>> class bird(animal):
...     def __init__(self, species):
...         super().__init__("bird")
...         print(f"It's a wild {species}bird.")
...         self.species = species
...         self.hp = 10
...         self.atk = 2
...     def eat(self, prey):
...         if self.atk >= prey.hp:
...             self.hp += prey.hp
...             self.atk += prey.atk
...             prey.hp = 0
...         else:
...             print("The early bird gets the worm!")
...     def chirp(self, cheep):
...             print(cheep)
...     def __str__(self):
...         return f"a {self.species}bird"
...     def __repr__(self):
...         return f"a {self.species}bird with {self.hp} hp and {self.atk} atk"
... 
>>> birb = bird("mocking")
A bird appeared.
It's a wild mockingbird.
>>> bug2 = animal(bug)
A bug appeared.
>>> birb.eat(bug2)
>>> birb.chirp(f"I am {birb.__repr__()}.")
I am a mockingbird with 11 hp and 3 atk.
>>> 
```

## 3.4 Advanced Actions

Some advanced concepts include structural pattern matching, iterators, decorators, and file handling. Structural pattern matching, introduced in Python 3.10, combines features from other languages, such as switch-case, "cond", and match statements from C-like languages, Lisp languages, and ML-like languages, respectively. Rather than nesting numerous if-statements, structural pattern matching allows a more structured format for finding matches within a list. Like most control statements in Python, pattern matching uses the `match` keyword, followed by a list to match with, and then a colon to start the indentation. In each `case`, you can have some sort of pattern to match.  

```
>>> match "foobar":
...     case ["foobar"]:
...             print("foobar")
... 
>>> match "foobar".split():
...     case ["foobar"]:
...             print("foobar")
... 
foobar
>>> match "foo bar".split(' '):
...     case ["foo"]:
...             print("foo")
...     case ["foo", "bar"]:
...             print("foobar")
... 
foobar
>>> 
```

In the above example, we matched for specific `str` patterns. We can use the `match` statement to make more generalized matches for variable patterns. As per usual with Python, you can add an asterisk, '*', in front of an identifier to allow variable length arguments.  

```
>>> match "go West".split():
...     case ["go", direction]:
...         print(f"You went {direction}.")
...     case ["go", *directions]:
...         for _ in directions:
...             print(f"You went {_}")
... 
You went West.
>>> match "go North East South West".split():
...     case ["go", direction]:
...         print(f"You went {direction}.")
...     case ["go", *directions]:
...         for _ in directions:
...             print(f"You went {_}")
... 
You went North
You went East
You went South
You went West
>>> 
```

The underscore is often used as a placeholder. In Python, you can use an underscore to match with anything and nothing. Thus, it may be useful to have a default case to address any patterns that are not matched.  

```
>>> match None:
...     case _:
...         print("This is a default case.")
... 
This is a default case.
```

If there are multiple cases that should have the same behavior, you can use an "or pattern" using the '|' operator to group multiple possible patterns within a case. This can also be used to match subexpressions.  

```
>>> match "jump".split():
...     case ["jump"] | ["double", "jump"]:
...         print(f"Woosh!")
...     case ["dash"] | ["jump", "dash"]:
...         print("I am speed.")
...     case _:
...         print("Sneak 100")
... 
Woosh!
>>> match "double jump".split():
...     case ["jump"] | ["double", "jump"]:
...         print(f"Woosh!")
...     case ["dash"] | ["jump", "dash"]:
...         print("I am speed.")
...     case _:
...         print("Sneak 100")
... 
Woosh!
>>> match "go North".split():
...     case ["go", ("North" | "South" | "East" | "West")]:
...         print(f"Compass!")
...     case _:
...         print("Maybe try an astrolabe.")
... 
Compass!
>>> match "go North-South".split():
...     case ["go", ("North" | "South" | "East" | "West")]:
...         print(f"Compass!")
...     case _:
...         print("Maybe try an astrolabe.")
... 
Maybe try an astrolabe.
```

Furthermore, you can check if the identifier you match also passes some other requirements, such as using the `in` keyword.  

```
>>> cardinal_directions = ("North", "South", "East", "West")
>>> match "go North".split():
...     case ["go", direction] if direction in cardinal_directions:
...         print(f"This is not a GPS.")
...     case _:
...         print("Try using a map.")
... 
This is not a GPS.
>>> match "go here".split():
...     case ["go", direction] if direction in cardinal_directions:
...         print(f"This is not a GPS.")
...     case _:
...         print("Try using a map.")
... 
Try using a map.
>>> 
```

Iterators in Python are not explicitly used as commonly as loops and list comprehensions. However, a benefit of using an iterator is to save memory, as you do not need to allocate memory for the entirety of the iterable when the iterator is initialized. Moreover, you can explicitly create your own custom iterables, provided your class has a `__next__` and an `__iter__` method. For example, we can create simple range-like object for floating point numbers rather than integers.__

```
>>> class float_range:
...     def __init__(self, end, start=0.0):
...         self.start = start
...         self.end = end
...     def __iter__(self):
...         self.it = self.start
...         return self
...     def __next__(self):
...         if self.it >= self.end:
...             raise StopIteration
...         curr = self.it
...         self.it += 1
...         return curr
... 
>>> list(float_range(10.0))
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
>>> for _ in float_range(10.0):
...     print(_)
... 
0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
>>> 
```

Rather than using a custom iterator, you can use the `map` function to map values over an iterable. The `map` function requires a function that can be called on each item in the iterable and an iterable to map.  

```
>>> list(map(lambda x : float(x), range(10)))
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
>>> for _ in map(lambda x : float(x), range(10)):
...     print(_)
... 
0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
>>> 
```

A generator is another way of creating an iterator. Using the `yield` keyword, you can quickly create an iterator from a function. This can be much easier and faster to implement than a class that implements an iterator.  

```
>>> def float_gen(end, start=0.0):
...     while start < end:
...        yield start
...        start += 1
... 
>>> list(float_gen(10))
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
>>> for _ in float_gen(10):
...     print(_)
... 
0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
>>> 
```

Finally, it can be useful to modify functions with decorators. These are higher order functions that take in a function as an input and performs some action that modifies a function. This is syntactic sugar for explicitly passing in function calls into other functions. To decorate a function, you can place an '@' symbol in front of the identifier of a decorator above the definition of a function. You can wrap functions with multiple decorators.  

```
>>> def pretty_print(fun):
...     def wrapper(*args, **kwargs):
...         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
...         output = fun(*args, **kwargs)
...         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
...         return output
...     return wrapper
... 
>>> def fancy_print(fun):
...     def wrapper(*args, **kwargs):
...         print("================================================================================")
...         output = fun(*args, **kwargs)
...         print("================================================================================")
...         return output
...     return wrapper
... 
>>> @pretty_print
... @fancy_print
... def super_print(value):
...     print(value)
... 
>>> super_print("foobar")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
================================================================================
foobar
================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> 
```

Finally, Python has the ability to interact with files using the `open`, `close`, `read`, and `write` functions. As it is mandatory to close a file after it is opened, it is highly recommended to open files using the `with` keyword. The `open` function takes in a path as well as some parameters in a string. The 'r' character represents reading from a file, the 'a' character represents append to a file, the 'w' character represents writing over a file, and the 'x' character represents creating a file, if it does not currently exist. You can also use 'rb', 'wb', and 'ab' to use binary mode, which is situationally useful.  

```
>>> with open("hw.txt", 'r') as f:
...     print(f.read())
... 
Hello!
Goodbye!

>>> 
```

## 3.5 Succinct Summary

Python is a simple, easy to understand language with roughly an S-shaped learning curve. Its primary strengths lie in its easy to use syntax, which reads like English or pseudocode, and the numerous open source Python libraries, which allow Python to easily handle nearly any task. Python is an object oriented, imperative, and interpreted language, with the ability to be compiled into bytecode for faster future runtimes. With pass by object reference, Python avoids the unwieldy syntax that encumbers C-like languages while still allowing easy use of pointers. In this chapter, we covered the basics of the Python scripting language. Next chapter, we will look at some of the numerous libraries that make Python even more versatile. For further reference, please refer to the official [Python3 tutorial](https://docs.python.org/3/tutorial/).  

#### [Return to Main Table of Contents](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/README.md#table-of-contents)
Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
