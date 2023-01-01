# Chapter 2: GNU EMACS

2. [GNU EMACS](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%202:%20GNU%20EMACS.md#chapter-2-gnu-emacs)
  - 2.1 [Elegant Emacs](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%202:%20GNU%20EMACS.md#21-elegant-emacs)
  - 2.2 [Meaningful Movement](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%202:%20GNU%20EMACS.md#22-meaningful-movement)
  - 2.3 [Kinetic Keystrokes](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%202:%20GNU%20EMACS.md#23-kinetic-keystrokes)
  - 2.4 [Lisp Language](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%202:%20GNU%20EMACS.md#24-lisp-language)
  - 2.5 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%202:%20GNU%20EMACS.md#25-succinct-summary)

## 2.1 Elegant Emacs

Emacs is more than just a text editor. Emacs is love and life. Not only does Emacs provide superior text editor capabilities, with easy to use and remember keybindings, Emacs is a fully functional integrative development environment (IDE) with customizations and package installations. From testing code on the fly with interactive sub-shells to connecting to remote Linux servers, Emacs is a versatile tool for all software construction purposes. With its own web browser and compilation extensions, you can even browse the internet and watch YouTube videos from within Emacs.  

Even better, Emacs perfectly encapsulates the ideal of bootstrapping and open source software. With it's own variant of the Lisp programming language, any user can write custom functions and keybindings in Emacs Lisp to edit the Emacs source code itself from within Emacs while it is running. This chapter will explore some of the basic functionalities of Emacs, beginning with basic movement and ending with an introduction to Emacs Lisp (Elisp) programming language. First of all, it is important to ensure that Emacs is installed. On most Linux servers, Emacs will have already been installed, but on your local machine, you may want to use a custom installation or version, which you can download online or install manually from various sources. Finding the path and version of your Emacs can be done with two simple commands.  

```
bash$ which emacs
/usr/local/bin/emacs
bash$ emacs --version
GNU Emacs 29.0.50
Copyright (C) 2022 Free Software Foundation, Inc.
GNU Emacs comes with ABSOLUTELY NO WARRANTY.
You may redistribute copies of GNU Emacs
under the terms of the GNU General Public License.
For more information about these matters, see the file named COPYING.
bash$ 
```

For installation of the most up to date version of Emacs, you can use the `git` version control system to clone the remote Emacs repository from the maintainers at Savannah. For faster download, you can skip most of the version history by specifying a depth, as most users will not need to examine different branches and commits in the development of Emacs. Either way, a copy of the Emacs repository will be downloaded to your current working directory inside a directory named "emacs".  

```
bash$ git clone https://git.savannah.gnu.org/git/emacs.git
bash$ git clone --depth 1 https://git.savannah.gnu.org/git/emacs.git
bash$ cd emacs
bash$ 
```

To build Emacs, the existing source code will allow easy compilation with only a few commands.  

```
bash$ ./autogen.sh
bash$ ./configure
bash$ make install
bash$ 
```

On MacOS, the executable Emacs application will be located inside "nextstep/Emacs.app/Contents/MacOS/Emacs". If you use Finder to look at "nextstep/Emacs.app", you will notice that you can simply click on this icon to run Emacs. Alternatively, you can use the `open` command to open up a particular path in the Finder. In the shell, it is recommended to use an alias to simplify the path to the command, or to use a symbolic link. The exact alias path depends on where you installed Emacs.  

```
bash$ open nextstep
bash$ open nextstep/Emacs.app
bash$ alias emacs=$HOME/emacs/nextstep/Emacs.app/Contents/MacOS/Emacs
bash$ 
```

Notably, the Emacs you installed will likely be the full graphical user interface (GUI) version of Emacs. If Emacs came built into your operating system, it is likely to be the terminal version of Emacs, which is more limited in graphical features. If you would like to open the GUI version of Emacs as the terminal version, you can specify with the "-nw" flag to not open up Emacs in a new GUI window. Otherwise, `emacs` would open up the full GUI version that you installed. For accessibility, on MacOS, you can adjust the text size using `Command + '-'`, `Command + '+'`, or reset to default with `Command + 0`.  

```
bash$ emacs
bash$ emacs -nw
bash$ 
```

This is recommended if opening Emacs after logging on a remote machine, as the GUI version after connecting to a remote machine can be quite limited compared to connecting through the GUI version of Emacs on your local machine to remote servers. It is also faster if you simply need to make minor changes to a file and then exit. Speaking of which, while not strictly necessary, Emacs can be closed with the keybinding `C-x C-c`. While these are not executable pieces of code, it is helpful to separate these keybindings in code blocks for improved visual display.  

## 2.2 Meaningful Movement

Emacs has two modifier keys: Control, represented in keybindings with 'C', which means hold down the Ctrl key, and META, represented by 'M', which means hold down the alt key. On MacOS, you would hold down the option key or tap the escape key once whenever the META key is to be held down. A dash '-' between characters in keybindings indicate hold down the keys in that particular order, releasing after the last key in the sequence pressed down. Spaces between sequences of keystrokes indicate that there may be a pause between the sets of keystrokes, i.e. the previous keystrokes do not all have to be held down until the entire set of keystrokes are finished. To record your keystrokes, you can open a dribble file using the keybinding `M-x open-dribble-file`, which asks you to specify the path to store the dribble file (use the .drib file extension).  

To move to the start of a line, simply use the keybinding `C-a`. To move to the end of a line, use the keybinding `C-e`. To help you remember these two keybindings, you can think of the letter 'a' as the start of the alphabet, and the word "end" starting with the letter 'e'. Conveniently, these two keybindings also work inside the Linux terminal as well as Emacs, so there is some overlap in the movement keybindings. To move to a particular location in the Linux terminal, or inside terminal Emacs, you can hold down the option key and click with the cursor. In the GUI version of Emacs, you can directly click with the mouse to where you wish to move your cursor.  

To move forward by one character, use the keybinding `C-f`. Inversely, to move backwards by one character, use the keybinding `C-b`. To move forward by one word, meaning a group of one or more characters separated by delimiters, you can use the keybinding `M-f`. To move backwards by one word, you can use the keybinding `M-b`. To move forward by one sentence, you can use the keybinding `M-e`. To move backwards by one sentence, you can use the keybinding `M-a`. There may be some variation in behavior, depending on the mode of the file. The mode of the file may also affect indentation and syntax formatting. To move forward by one line, you can use the keybinding `C-n`, and to move backwards by one line, you can use the keybinding `C-p`. These keybindings should be fairly intuitive, as they take the first letter of the respective movement words. In markdown mode, you can use `M-n` and `M-p` to move to the next markdown link and the previous markdown link, respectively.  

It may be useful to center the cursor (vertically) to the middle of the page. This can be done with `C-l`. Repeating this keybinding would cycle the location of the cursor to the top and bottom of the page, before repeating. To move forward by a page, you can use the keybinding `C-v`. The inverse, `M-v`, moves the file backwards by one page. You can think of the 'v' as a downwards arrow to help remember this keybinding. Note that here, `C-v` is not the paste keybinding. If you are using GUI Emacs, you can use the usual cut, copy, paste, and undo shortcuts: "Command + x", "Command + c", "Command + v", and "Command + z", but these keybindings are unlikely to work as reliably in the terminal version of Emacs. It may also be useful to move to the beginning of a file, with the keybinding `M-<`, or to the end of a file, with the keybinding `M->`. These are fairly intuitive, as the '<' and '>' characters point towards the start and ends of the file, respectively. Also note that you will need to hold down shift to use the '<' and '>' characters, so you would hold down shift after the META key.  

When opening up Emacs with the `emacs` command, the default buffer, region of displayed text, that will be opened will be the \*GNU Emacs\* welcome page, which contains numerous useful links, including the built in Emacs tutorial. If Emacs is called before a path or file name, Emacs will either open it, if it exists, or create and open a new empty file (similar to the `touch` command, except touch does not open the file). By default, Emacs starts with one buffer. To split a buffer in half horizontally, opening a second buffer below the current buffer, you can use the keybinding `C-x 2`. To open up a buffer to the right of the current buffer, splitting the space taken up by the current buffer in half vertically, you can use the keybinding `C-x 3`. To cycle between displayed buffers, you can use `C-x o` to cycle between currently visible buffers. In the GUI version of Emacs, you can use the mouse or cursor to click into buffers.  

To close the current buffer, you can use `C-x 0`, if there are other buffers visible. To close all other buffers besides the currently active buffer, you can use the keybinding `C-x 1`. These are easily remembered by thinking of the '0' as reducing the current buffer to nothing, and '1' as representing keeping only the one currently active buffer. To switch to a specific buffer, you can use the keybinding `C-x b`, to specify a specific buffer to switch to. If you would like to open a specific file instead, you can use `C-x C-f` to open a file. To open a buffer in a separate window, as opposed to the current buffer, you can use the keybinding `C-x 5 C-f`. These windows will still be part of the same Emacs session, as opposed to opening a separate instance of the Emacs application. As with earlier, if the file specified does not yet exist, Emacs will create an empty file at the specified file location. To save this file, or to save changes to existing files, you can save using the keybinding `C-x C-s`. This is easy to remember as you want to save the file, where you are executing a save command, whereas closing the file (and all other buffers), is to execute a close command, with the keybinding `C-x C-c`.  

If a file has been edited and saved, the last previous save will be stored with a save file with the same name, except with the '\~' character appended to the end of the name. Thus, you will often see files with '\~' at the end after editing files with Emacs. A similar save file are files with '#' around the start and end of the file. These are created when there are unsaved changes when an Emacs process is closed or interrupted. Every Emacs session will also have a \*scratch\* buffer, which contains text that is not saved. By default, when Emacs is opened, `C-x b` will default to scratch. The scratch buffer acts as a scratchpad for quick notes that are not intended to be saved, as well as an interactive environment for writing code in Emacs Lisp. You can save the contents of the scratch buffer the same way you would save any file, with the keybinding `C-x C-s`, where Emacs will then ask you to specify where you would like to save the scratch buffer.  

## 2.3 Kinetic Keystrokes

As with exiting programs, it is important to be able to quit from unintended commands and keybindings. To cancel out of an active function in the current buffer, you can use the keybinding `C-g`, which triggers the "keyboard-quit" command. As you may have noticed, at the bottom of the screen, there is a "mini-buffer". This mini-buffer will usually display useful information, such as the current combination of keystrokes, or for some commands, provide a location for providing user input. As with other buffers, when the mini-buffer is active, you can switch between buffers using `C-x o`. Unlike other buffers, however, you cannot "close" the mini-buffer with `C-x 0`, as it will always remain at the bottom of the screen.  

As with most modern text editors, it is useful to have keybindings for cut, copy, and paste. If you are using the GUI version of Emacs, you can simply use your mouse or cursor to select text and use the regular machine keyboard shortcuts. However, Emacs has numerous keybindings for versatile text manipulation. The most commonly used keybinding for cutting selections of text is to kill the current line, using `C-k`. What this means is that you are deleting from the current location of the cursor to the end of the line (i.e. until the newline '\n'). Notably, the kill-line command is the same when used in the Linux shell. The opposite of killing a line is to yank it back into the buffer, using the keybinding `C-y`. This is easy to remember, as you are yanking text back into the buffer.  

To kill from the cursor to the beginning of the line, you can wrap the kill-line command with the universal-argument command, `C-u`. This command can be used to repeat a command multiple times, or depending on the command, alter its behavior. For killing a line forwards to the start of the line, rather than to the end, you can use `C-u 0 C-k`. In general, `C-u` allows you to specify a number of times for a command to be repeated. For example, `C-u 4 C-f` attempts to move the cursor 4 characters forwards. By default, if no number is provided, then the numerical argument to the universal-argument command defaults to 4. In some contexts, you can also pass in negative numbers, putting a '-' in front of the number. For example, `C-u C-f` has the same effect as `C-u -4 C-b`.  

To select specific regions of text, you can set a mark using either `C-SPC` or `C-@`, where "SPC" refers to the space bar, and the '@' key uses "S-2", or the shift key followed by the '2' key. Afterwards, Emacs selects the region between wherever you set your mark and the cursor. An alternate way to select a region is to hold down shift and move using the arrow keys, which will select the region from the initial location of the cursor when the shift key is first pressed down, to wherever the cursor is located after the shift key is released. Finally, on the GUI version of Emacs, you can simply use the mouse or cursor to select regions of text, the same way you would on any region of text elsewhere. To kill this region of text, you can use the command `C-w`. To copy this region of text, you can use the keybinding `M-w`. This is effectively the same as killing and yanking the region.  

A text editor would be quite ineffective without the ability to search for strings or patterns of text. To perform an incremental search, that is, searching forward in the text, you can use the keybinding `C-s`. To search for the next instance of that string, you can use `C-s` again. When in the interactive mini-buffer, you can also re-use previously used entries by cycling with the arrow keys, or by viewing previous history items with `M-p`. Eventually, when you reach the end of the buffer, you will wrap around to search again from the start of the file. To perform an incremental search backwards, you can use the keybinding `C-r`. These search commands should be fairly intuitive, with 's' representing "search" and 'r' representing "reverse". To search and replace, you can use the keybinding `M-%`.

Regular expressions can be used for more advanced search queries. To do so, we will invoke a command directly using the keybinding `M-x`, which runs the command "execute-extended-command". This allows us to run Emacs commands. The previous keybindings mentioned can be searched for using the keybinding `C-h k`, which will reveal documentation in the \*Help\* buffer. The specific functions the keybindings are bound to can be looked up using `C-h f`. The keybinding `C-h` itself runs the command "view-order-manuals", which allows for viewing specific help manuals. These commands should be easy to remember, with 'h' representing "help", 'k' representing "keybinding", and 'f' representing "function". To perform a regular expression search, you can use `M-x re-search-forward` or `M-x re-search-backward`, which are self explanatory, given your comprehensive understanding of regular expressions from "Chapter 1: The Shell".

Returning to the shell can be done within Emacs. With `M-x shell`, `M-x term`, `M-x ansi-term`, and other similar commands, you can open up a limited version of the terminal or shell within Emacs. While some more advanced functionalities may have unexpected or unwanted behavior, basic commands should be fully capable of operating as intended. As the shell buffer is in Emacs, you can directly edit the contents as you would any other buffer, depending on the version of the shell or terminal you invoke within Emacs. To repeat previous commands within the shell buffer, you can use `M-p` to view previous history terms.

One reason to visit the shell is to examine the files in the current working directory. However, Emacs allows the user to browse files easily with "dired-mode". To change to dired mode, where Emacs displays a particular directory's files, you can use `M-x dired` or `C-x d`. Inside dired-mode, you can click on a file to open it. If you click on a directory, it will instead change the current working directory to the selected directory, updating the display of current file contents. A huge strength of dired-mode is that you can easily rename or update files using Emacs commands and keybindings, treating the directory contents as a regular file. To make the buffer interactive, you can use `C-x C-q`. To save your changes, you can use `C-c C-c`. To cancel your changes, you can use `C-c ESC`, where "ESC" is the escape key. 

The dired mode also allows easy file manipulation with simple character commands. For example, you can mark files for later commands using the 'm' key on your keyboard, and unmark files using the 'u' key. To mark a file for deletion, you can use a lowercase 'd', while to immediately request deletion of a file, you can use an uppercase 'D'. You can also hit the "delete" key to unmark a file and move back/up by one line at the same time and hit "enter" to open a file or directory. To open up a new window with the specified file or directory, you can hit the 'o' key. To compress a file, you can use a lowercase 'c', while an uppercase 'C' lets you copy files. Similarly, an uppercase 'R' allows you to rename a file. To update or refresh the directory contents, i.e. to see if there are any changes to the directory since it was last opened or updated, you can hit the 'g' on your keyboard when the cursor is inside the buffer.  

Sometimes, it may be necessary to compile pieces of code, depending on the language. To run compilation commands, you can use `M-x compile`. By default, this will have "make -k" in the mini-buffer. As this is likely not the compilation command you intend to use, you can just delete the current text and replace it with the appropriate compilation command, as if you were running the compilation command in the shell. To change your current working directory, you can use the "cd" command, with `M-x cd`, which works similarly to the shell command. This allows for changing where you are in your file system, making relative paths more easily accessible. While these features so far make Emacs incredibly versatile, one of the further benefits of using Emacs is that you can customize Emacs by editing its source code itself using the Emacs Lisp (Elisp) programming language.  

While some commands can be simply executed with `M-x`, it may be helpful to write snippets of Emacs Lisp code, to combine various Emacs functions or commands. You can use `M-:` to execute these code snippets in the mini-buffer. If you have a piece of lisp code in any buffer, you can execute the last expression, the last piece of lisp code, before the cursor using `C-x C-e`, with the result displayed in the mini-buffer. You can think of this keybinding as "execute expression". One example of `M-x` and `M-:` being used similarly is with count-words, where you can run `M-x count-words` or run a lisp expression with `M-: (count-words (point-min) (point-max))`.  

For testing various pieces of code, the \*scratch\* buffer can be used for experimenting with Lisp code, as it starts in Lisp mode. Here, you can use `C-j` to execute the last expression, outputting a newline before the result and moving the cursor to the following line. In normal buffers, `C-j` inserts a newline '\n', which is effectively the same as hitting "Return" or "Enter". In contrast, regular files start in "fundamental mode", which you can toggle with `M-x fundamental mode`, or `M-x fun`. You can also change the mode of regular file to lisp mode with `M-x lisp-mode`. Depending on your customizations, Emacs can also infer which mode should be used based on the file extension of the current buffer. At the top of the scratch buffer, you will see two lines of text with ";;" in front. This is due to ';' being the comment character in Lisp languages.  

## 2.4 Lisp Language

Before starting with the syntax of Emacs Lisp, it is necessary to know some of the background behind the family of Lisp languages and functional languages in general. Lisp was created in 1958 by John McCarthy, which makes it the second oldest language that is widely used today, with Fortran, used for scientific computing, being just one year older. Lisp is commonly used in its various dialects today, such as Common Lisp, Scheme, Racket, Clojure, and Emacs Lisp.  

Lisp is a functional language, meaning that programs are built around functions, focusing on passing data and information between functions. Each function may take some input and perform some task, returning one or more values, which can then be handled by other functions. Smaller functions may be used as building blocks and composed together into a larger function, or functions may be passed as arguments to higher level functions. Functions are first class citizens and are to be treated the same as data and variables. Furthermore, in Lisp, programs and data become almost interchangeable.  

In contrast, languages such as C, C++, Python, and Java are imperative languages, where each line of code, loosely speaking, is giving a command to update the state of the program. For example, you may see a line of code saying `int a = 1;`, or later, `a = a + 1`. While the former be fine to declare that "a" is an integer data type with value 1, from a mathematical point of view, the latter expression makes no sense. However, from an imperative point of view, we are simply re-assigning the value of the variable "a".  

While imperative languages may use functions (or methods) of their own, these functions often have side effects that alter the state of other parts of the environment. In contrast, functional programming paradigm prefers pure functions, which do not rely on the environment or have any side-effects that may alter the state of the program. With a pure function, the result will always be the same, regardless of the environment it is in. While it is possible to use imperative programming in Lisp, this would be detrimental and distracting from learning the fundamentals of functional languages. Thus, we will aim to avoid global variables or functions with side-effects in Emacs Lisp, e.g. `setq`.  

In most imperative languages, it is useful to begin with the basic data types. In Lisp, rather than primitives, it is more useful to compare data types as either an atom, symbol, function, or a list. An atom is the smallest building block in Lisp languages. These are your primitive data types, such as integers, strings, and floats. You can use the `type-of` function to return the data type of an object. Symbols are the equivalent of variables in other languages. Functions are special, as they are executable pieces of code. Lists, or rather, linked lists, are the most basic data structure used in List Processing (Lisp). Furthermore, lists are also the backbone of Lisp expressions, which are executable pieces of code.  

Lisp expressions are written using parentheses "()", with elements of the list separated by spaces. These nested parentheses may seem intimidating at first, but with proper indenting, can become almost somewhat manageable. When the first element of the list is a function, this creates an executable expression. Thus, Lisp uses prefix notation, where the function appears before the arguments. This differs from what you may be used to in most imperative languages, which use infix notation. For example, `1 + 2` in C, C++, and Python has the value 3. In contrast, in Lisp, we would write this expression as `(+ 1 2)`. The "+" function is a function that adds 0 or more numerical arguments. Similarly, we can evaluate other common numerical operations.  

```
(type-of 1)
integer

(type-of 1.0)
float

(+ 1 2)
3

(- 1 2)
-1

(* 1 2)
2

(/ 1 2)
0

(/ 1.0 2)
0.5

(/ 1 2.0)
0.5

(% 1 2)
1
```

These mathematical operators can take different numbers of arguments, including none. For addition, subtraction, and multiplication, we return the constant for those operations. With subtraction, using one argument returns the additive inverse. Notably, division cannot have no arguments. When using just one argument for division, we are dividing 1 by the argument, taking the multiplicative inverse. Also note that with multiple arguments, we apply the operator from left to right, folding the argument list to the right (fold right).  

```
(+ 1 2 3)
6

(+)
0

(- 1)
-1

(-)
0

(* 1 2 3)
6

(*)
1

(/ 120 6 2)
10

(/ 1)
1

(/ 2)
0

(/ 1.0)
1.0

(/ 0.5)
2.0
```

To work with lists in Lisp, it is important to understand the basics of the linked list data structure. Put simply, a linked list consists of a list of nodes. Each node contains a value, which is stored in its head, and a next pointer, which points to the next node in the list. In Lisp, this node is referred to as a `cons` object. If you pass in two atoms to the `cons`, you create an improper list, which is sometimes called a dotted pair, if there are two elements in the list. This is due to there being a dot present in the list, which indicates an improper list. You can create a list using the `list` function. An empty list, `'()`, or nil, does not contain any values. The head of an empty list is nil, and the tail of the empty list, is also nil.   
 
```
(cons 1 '())
(1)

(cons 1 2)
(1 . 2)

(list 1 2)
(1 2)
```  

To retrieve the head of a list, you can use the `car` function. To retrieve the tail of a list, or the rest of the list, you can use `cdr`. Notably, you can nest `car` and `cdr`, which will be evaluated right to left. To create a node, you will need to pass in a `car` and a `cdr`, which are an atom and a list, respectively. Also note that the order of the `car` and `cdr` is important; it is not valid take the `cdr` of a `car`, as an atom does not have a tail, whereas a list will have a both head and a tail. Meanwhile, taking the `cdr` of a dotted pair will return the second atom, rather than a list.  

```
(car (list 1 2 3))
1

(cdr (list 1 2 3))
(2 3)

(car (list 2 3))
2

(car (cdr (list 1 2 3)))
2

(cadr (list 1 2 3))
2

(car (cons 1 2))
1

(cdr (cons 1 2))
2
```

Unlike expressions, which use parenthesis to indicate the evaluation of a function, lists are considered data. To distinguish between an expression to evaluate and an expression to be treated literally as data as it is written, you can use a single quote, referred to as "quote", in front of an expression to treat it as is, without evaluating the list contents. Of course, `quote` is a function. However, for simplicity, we can use '\'' as "syntactic sugar" for a shorthand notation for the `quote` function. In Lisp, code and data are one and the same.  

```
'(+ 1 2)
(+ 1 2)
 
(quote (+ 1 2))
(+ 1 2)

(car '(+ 1 2))
+
 
(car (quote (+ 1 2)))
+

'()
nil

(quote ())
nil
```

 The symbol, nil, also happens to mean logical false, so nil and '() can be used interchangeably. In contrast, the equivalent symbol for true, t, means logical true. This is important to keep track of when performing boolean operations, such as `and`, `or`, `xor`, etc.  
 
Lisp has a special way of handling such operators. With logical `and`, lisp will stop execution as soon as a parameter has value nil, and returns nil. Notably, the number 0 is not treated as false. If no arguments have value nil, then the last value is returned instead.  

```
(and t t t)
t

(and t 0 100)
100

(and t nil 100)
nil

(and)
t
```

In contrast, the `or` function will stop execution as soon as it finds a non-nil value, returning that value. If all arguments have a value of nil, then nil is returned.  

```
(or t nil)
t

(or nil '())
nil

(or nil 0)
0

(or)
nil
```

While some boolean operators can take multiple values, including none, other operators, such as `xor`, require exactly two arguments.  

```
(xor t t)
nil

(xor t nil)
t

(xor nil t)
t

(xor nil nil)
nil
```

Unary operators, such as "not", will take exactly one argument.  
 
```
(not t)
nil
 
(not 1)
nil

(not nil)
t

(not '())
t
```
 
While working with lists, there are some common functions that you may find useful. A common interview question, for example, is to reverse a linked list. In Lisp, you already have linked lists, and you can reverse them with the `reverse` function.  
 
```
(reverse '(1 2 3))
(3 2 1)
```

You may also want to concatenate two lists, which you can do using `append`. Note that append will point the cdr of the last element in each list argument to the head of the next argument. Thus, while you can append improper lists to the end of a proper list, you cannot append a list to the end of an improper list, as the last element of an improper list is an atom, rather than a list, or `cons` object.  

```
(append '(! 2) '(3 4))
(1 2 3 4)

(append '(1 2) '(3 4) '(5 6))
(1 2 3 4 5 6)

(append '(1 2) '(3 . 4))
(1 2 3 . 4)
```

With basic syntax out of the way, it is logical to investigate control structures, beginning with conditionals. Like most languages, you can use if statements, with the syntax of `(if COND THEN ELSE...)`, where THEN is a single expression, and ELSE can be 0 or more expressions. If COND is nil, and ELSE has no expressions, then nil is returned. In general, if you see "..." in Lisp, this means the function can have a variable number of arguments.  

```
(if t
	t
  nil
  )
t

(if nil
	t
  nil
  )
nil

(if nil
	t
  )
nil
```

It can be useful to output text using the `message` function, which uses a format string. Note that here we are using `message`, which avoids side effects, rather than `print`, which not only returns an object, but also returns it, or `insert`, which inserts 0 or more strings at the current cursor location, and returns nil. The format strings work the same way as in the shell, or C-like languages. You can also nest conditionals, allowing for more complicated conditional expressions. Rather than using only t or nil, you can also use comparison operators to return boolean outputs, e.g. `>`, `<`, `<=`, `>=`, or `=`. Again, these operators use prefix notation and are located before the arguments, rather than between the arguments. Also, note that `=` is only for comparing numerical arguments only.  

```
(if t
	(message "Hello %s" "World")
  (message "Goodbye World")
  )
"Hello World"

(if (< 0 0)
	(message "Negative")
  (if (> 0 0)
	  (message "Positive")
	(message "Zero")
	)
  )
"Zero"
```

For general use equality comparison, you should use `equal`, which compares if two arguments have the same value. If you use `eq`, you are comparing whether or not two arguments have the same memory address. For some primitives, such as strings, Lisp will have the same address.  

```
(eq 1 1)
t

(eq 1 0)
nil

(eq 'a 'a)
t

(eq 'a 'b)
nil

(equal 'a 'a)
t

(equal 'a 'b)
nil
```

 To better demonstrate this difference, we will also introduce the `let` command, which lets us bind values to symbols. The syntax for `let` is `(let VARLIST BODY...)`, where VARLIST contains pairs of variable names and values to bind to the variable names, and BODY is 0 or more expressions. As per usual, if BODY has 0 expressions, the "let" expression will return nil.  

```
(let
	)
nil

(let (
	  )
  )
nil

(let ((a "a")
	  )
  )
nil

(let ((a "a")
	  )
  a
  )
"a"

(let ((a "a")
	  )
  (equal a "a")
  )
t

(let ((a "a")
	  )
  (eq a "a")
  )
nil
```

Already, the parenthesis have become quite formidable. If we have more complex if statements, this could become difficult to read, even with Emacs helping by automatically formatting parentheses in Lisp mode. Fortunately, we can use `cond` to match various conditions, similar to switch-case and pattern matching in other languages. The syntax for `cond` is `(cond CLAUSES)`, where each clause is a list with the first element returning a boolean value, and the second element evaluating some expression if the first element is not nil. As soon as one condition is met, the corresponding expression is evaluated, and no other conditions are considered. As per usual, if there are no matches, then the `cond` expression will return nil. Thus, it is usually useful to have the last element to be some default option.  

```
(cond
 ((< 0 0)
  (message "Negative"))
 ((> 0 0)
  (message "Positive"))
 (t
  (message "Zero"))
 )
"Zero"
```

Inside these conditionals, it is useful to be able to use reflection, which is when a language can inspect its objects without knowing specifically what the object is. For example, a function may wish to handle an atom differently from a list. Some useful reflexive functions include `atom`, which returns t if its argument is an atom, `listp`, which returns t if its argument is a list, `numberp`, which returns t if its argument is a number, `stringp`, which returns t if its argument is a string, and `null`, which returns t if its argument is nil. Notably, nil is an atom, list, and null, and the respective functions all return t for the argument of nil.  

```
(atom 1)
t

(atom nil)
t

(atom '(1))
nil

(listp '(1))
t

(listp nil)
t

(listp 1)
nil

(numberp 1)
t

(numberp "a")
nil

(stringp "a")
t

(stringp 1)
nil

(null '())
t

(null nil)
t

(null 1)
nil
```

Without further ado, we will finally explore the ability to write functions. In any functional programming language, functions are first class citizens. In Emacs Lisp, we can define our own functions using the `defun` function. Indeed, we are using a function to define functions, with the syntax `(defun NAME ARGLIST [DOCSTRING] [DECL] [INTERACTIVE] BODY...)`. The "NAME" argument is the name of the function. The "ARGLIST" is a list of input arguments to the function. The "DOCSTRING" is an optional string that contains any documentation you would like to specify for the function. The "INTERACTIVE" optional argument is simply `(interactive)`, which allows the function to be used interactively, meaning you can use `M-x` to call the function or invoke the function through keybindings. The "DECL" optional argument is well beyond the scope of this material. The `defun` function returns the function you have just defined.  

```
(defun greet-user (name)
  "Greets the user with a format string \"Hello\", followed by the input string argument."
  (message "Hello %s" name)
  )
greet-user
	
(greet-user 'Foobar)
"Hello Foobar"

(greet-user "World")
"Hello World"

(defun hello-world ()
  "Print out \"Hello World\""
  (interactive)
  (message "Hello World")
  )
hello-world

`M-x hello-world`
```

Last but not least, the functions you defined are not persistent. Once you close Emacs, these non-persistent data will be lost forever. To save these functions for later use, you can store them in a file. To load a Lisp file, you can use the `load` function. For example, to load up new changes to your Emacs configurations in your "~/.emacs.d/init.el" configuration file, you can use `(load "~/.emacs.d/init.el")`, which will return t if it succeeds. It is recommended to store configurations in the ".emacs.d" directory. Previously, an ".emacs" file was standard for these customizations. With your newfound knowledge of Emacs Lisp, you can customize your Emacs environment to your liking. Furthermore, there are numerous Emacs packages, such as spellcheckers and language specific modes, that you can install that can make your development environment easier to use. You can even browse the internet and watch YouTube videos from the comfort of your Emacs.  

## 2.5 Succinct Summary

Editor MACroS is more than a text editor. It is a fully customizable integrative development environment with its own variant of the Lisp family. In this chapter, we introduced a small number of features that may prove useful for your own software development experiences. We also introduced Emacs Lisp as a functional programming language, covering the basic syntax necessary to begin writing your own functions. It is important to note that while many of these concepts will translate over to other variants of the Lisp family, there are important syntactic differences to be careful of when switching between languages. You will revisit variants of the Lisp programming language in the upper division classes, Programming Languages (CS131), usually taught by [Professor Paul R. Eggert](https://samueli.ucla.edu/people/paul-eggert/), and Introduction to Artificial Intelligence (CS161), which is taught by multiple professors. For quick reference to Emacs keybindings, you can use the [Emacs Cheat Sheet](https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf).  

#### [Return to Main Table of Contents](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/README.md#table-of-contents)

Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)  
