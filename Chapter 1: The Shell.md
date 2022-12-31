# Chapter 1: The Shell

1. [The Shell](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%201:%20The%20Shell.md#chapter-1-the-shell)
  - 1.1 [Shell Shocked](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%201:%20The%20Shell.md#11-shell-shocked)
  - 1.2 [Safe Syntax](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%201:%20The%20Shell.md#12-safe-syntax)
  - 1.3 [Suspicious Summons](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%201:%20The%20Shell.md#13-suspicious-summons)
  - 1.4 [Shell Scripting](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%201:%20The%20Shell.md#14-shell-scripting)
  - 1.5 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%201:%20The%20Shell.md#15-succinct-summary)

## 1.1 Shell Shocked

Before writing shell scripts, it is important to know the basics of the Linux operating system, or Unix-like operating systems. For simplicity, we will refer to this family of operating systems as Linux for the rest of this manuscript. When your computer is on, you have files on your computer and processes which are running. Even as you read this document, you have processes running on your computer which enable your machine to display data and information. However, once you turn off your computer, these processes are killed, and their relevant information is lost. Unlike processes, files are persistent, or non-volatile, and continue to store the data that they contain. Some files contain executable code, which can be run by the machine, creating processes that execute some task. These special types of executable files are called programs.  

The shell is one such program that acts as an outer layer that holds together all the files, programs, and processes inside your operating system. Some common shells include sh, bash (Bourne Again Shell), and zsh (used on MacOS). In this manuscript, we will refer to this family of languages simply as the shell. The terminal provides an interface for the user to interact with the shell through various commands. The interpreter can read commands, evaluate the meaning of the commands, print the results, and loop the previous three steps. While not as pretty as clicking on graphical user interface (GUI) icons, this Read Evaluate Print Loop, or REPL, forms a useful interface for the user to efficiently interact with the internals of their machine. To access the terminal, simply open up the terminal application. On MacOS, this is simply called "Terminal" and can be found in Spotlight Search (⌘+ Shift). For Windows users, it is recommended to use a Linux virtual machine (VM), or even better, switch to an Unix-like operating system.  

## 1.2 Safe Syntax
Before running any program, it is crucial to be able to exit the program. To exit the shell, simply enter `exit`. Note that `exit` is enclosed inside a code block. The raw format of this code block is with these special quotation marks, called back-ticks \`\`. When you see these special quotations, it generally refers to snippets of executable code. In markdown, these back-ticks format the enclosed text inside these code blocks. If you see these back-ticks in the shell, they indicate for the shell to run the code inside the back-ticks.  

```
bash$ exit
```

In this manuscript, we will generally use back-ticks to indicate code blocks for examples of code, and when applicable, show the raw text form of back-ticks if they are part of the actual code to be run. We will also use single quotes '' to indicate characters and double quotes "" to indicate strings of text. If you are curious about how we distinguish between the function of the back-ticks, whether to display as \`\' or to create a `code block`, the answer lies in the escape character '\\', or backslash.  

In the above case, we actually used three back-ticks to make the code block display extend the entire width of the page. Some characters have special meanings, which will be ignored if a backslash is place in front. The backslash character itself is a special character, so to display the actual backslash, we will need to use a backslash to escape itself. We will also use `bash$ ` to delimit the start of lines in the terminal for the user to input commands, and lines without the `bash$ ` will indicate output.  

To find out what any particular command does, we can use the manual command `man`, followed by the name of the command. We to find out what the `man` command does, we can simply run the command `man man`. This opens up an interactive manual, which you can scroll using the arrow keys, the enter key, the cursor, or the other keybindings. To exit the manual, hit q.  

The simplest command in Linux is `false`. This command will always return false and fail with a non-zero exit code. This command is useful in case you want to test the results of conditionals in your code.  

```
bash$ false
bash$ 
```

The opposite of the `false` command, as one may expect, is the `true` command, which always returns true and succeeds, returning an exit status of 0. The exit status of a piece of code helps the operating system determine of the execution of the code succeeded.  

```
bash$ true
```

To verify the exit status of the latest command, we can use the special variable "?". To access the value of variables in the shell, we simply put a dollar sign, '$', in front of the variable. To echo out this value, we can use the `echo` command, which simply prints out whatever is passed into the command. In this case, we can use `echo $?` to see that `true` exits with status 0.  

```
bash$ echo $?
0
bash$ 
```

Since the last command before `echo $?` was `true`, the exit status is 0. Usually, we want to enclose the echo command's input string with double quotes "". If we want to treat the string literally as is, i.e. literally dollar-sign question-mark, we can use single quotes ''. This prevents evaluating variable values.  

```
bash$ echo "$?"
0
bash$ echo '$?'
$?
bash$ 
```

If we want to quote a quotation mark of the same type as the outer quotation marks, we can escape the quote with a backslash '\'. We can mix and match quotation marks, as long as we ensure we end the quotation with the same type of quote as the starting quote. We can also simply wrap the single quote inside double quotes instead.  

```
bash$ echo \"\'\"
"'"
bash$ echo '"'\''"'
"'"
bash$ echo '"'"'"'"'
"'"
bash$ 
```

By default, the `echo` command adds a newline, '\n', at the end of each line. We can suppress this behavior with the optional flag "-n", with `echo -n` in most shells. Notably, sh does not allow for this behavior with "-n".  

```
bash$ echo -n "hello world! "
hello world! bash$ 
```

Another common option for echo is to use the "-e" flag to use backslashes for special characters. Two of the most commonly used special characters are the newline character, '\n', and the tab character, '\t'. Note that we used 4 spaces for visualization purposes in markdown rather than tabs.   

```
bash$ echo -e "Dr. \nEggert"
Dr. 
Eggert
bash$ echo -e "Dr. \tEggert"
Dr. 	Eggert
bash$ 
```

Other special characters include backspace, '\b', and the '\c character, which suppresses newlines and terminates output. This causes the next terminal prompt to begin on the same line, rather than on a separate line.  

```
bash$ echo -e "Dr. \cEggert"
Dr. bash$ echo -e "Dr.  \bEggert" 
Dr. Eggert
bash$ 
```

The next few characters are a bit more intricate in their interactions. First, we have the vertical tab, '\v', and the form feed, '\f'. The form feed has different behavior depending on what type of machine. On printers, it loads a new page. On some terminals, it clears the page, while on others, it works the same as a vertical tab. Vertical tabs move the cursor to a new line, indenting the same number of characters as the end of the previous line.  

```
bash$ echo -e "Dr.\vEggert"
Dr.
   Eggert
bash$ 
```

While these special characters may seem a bit strange, they are in fact attempting to maintain backwards compatibility with typewriters. The bell, '\a', and carriage return, '\r', mimic the behavior that you would see and hear from typewriters. When the '\a' is read, it triggers an alert or bell sound. Traditionally, typewriters used this sound notification to alert the user that they were running out of space for characters on that line. This would suggest for the typist to either hyphenate a word or to move to a new line. Similarly, upon moving to the new line, the typewriter needs to perform a "carriage return", where the carriage, the part of the machine that inputs the text onto the document, is physically slid back to the beginning of the line. Thus, we can combine the behaviors of the bell, carriage return, and vertical tabs to perform intriguing text output.  

```
bash$ echo -e "Dr.\vEggert" 
Dr.
   Eggert
bash$ echo -e "Professor\vEggert\a\rDoctor" 
Professor
Doctor   Eggert
bash$ 
```

An alternative command to output strings is to use `print`, or `printf`. This allows behavior similar to the basic `echo` command, and printing format strings, commonly used in C/C++ languages. Some format options include strings, "%s", integers, "%d", characters, "%c", and floats, "%.#f", where # is the number of decimal points you would like to specify (optional).  

```
bash$ print "This string, %s, has length %d." foobar 6
This string, %s, has length %d. foobar 6
bash$ printf "This string, %s, has length %d.\n" foobar 6
This string, foobar, has length 6.
bash$ printf "The first char, %c, has length %.2f.\n" foobar 0.99999997 
The first char, f, has length 1.00.
bash$ 
```

If we want to output the text of a file, rather than just text we type in the terminal, we can use the `cat` command. Supposing we had a file "foobar.txt", with the words "cat", "mat", and "hat", ending the file with a newline '\n', as is standard, we can use the `cat` command to output the file.  

```
bash$ cat foobar.txt
cat
mat
hat
bash$ 
```

If we had also a file "fubar.txt" with the words "rat", "bat", and "sat", ending with a newline '\n', as is standard, we can concatenate the two files together. We can concatenate as many files as needed in the order we input the filenames to `cat`.  

```
bash$ cat foobar.txt fubar.txt
cat
mat
hat
rat
bat
sat
bash$ 
```

Other than echo and cat, for displaying variable values and file contents respectively, there are a few more commands for basic text output. The first example is `head`, which displays the first 10 lines of a file by default. You can specify the number of lines with the "-n" flag.  

```
bash$ head alphabet.txt
a
b
c
d
e
f
g
h
i
j
bash$ head -n 5 alphabet.txt
a
b
c
d
e
bash$ 
```

Inversely, the `tail` command displays the last 10 lines of a file by default, with the "-n" flag for specifying how many lines.  

```
bash$ tail alphabet.txt 
q
r
s
t
u
v
w
x
y
z
bash$ tail -n 5 alphabet.txt
v
w
x
y
z
bash$ 
```

If more flexibility is necessary, you can use the `more` and `less` commands, which allow you to scroll interactively through the files with arrow keys. To escape from these two commands, or interactive commands that show ':' at the bottom of the terminal, you can hit the 'q' key on the keyboard. These interactive formats make use of vi, or vim, keybindings. While these keybindings may be commonly used, the one and only keystroke that is both necessary and sufficient to know for these inferior text editors is the 'q' keybinding to escape out of the program.  


The `echo` command is often used for displaying environment variables, or variables in your current instance of the shell. The most notable environment variable is the PATH variable. This variable contains the order of the paths which the operating system looks for the location of the commands you use on your machine. These directory (folder) structures are similar to how you may call organize files in folders in a file cabinet. The current working directory is the current path, or location, you are at on your machine. The lowest level directory, or root directory, is simply a forward slash "/". All sub-directories inside any given directory are delimited, or separated, using a forward slash '/'. Directories are a special type of file that contains other directories and/or files. To go to the root directory, we can use the change directory command `cd`, followed by the path to the directory.  

```
bash$ cd /
bash$ 
```

To check your current working directory, or where you are in the operating system, you can print your current working directory with `pwd`.  

```
bash$ pwd
bash$ 
```

Your HOME directory is a where your current working directory will start out as when you open the terminal. Since HOME is a variable, you can view the home directory location using the echo command. The '~' character acts as a substitute for $HOME, and you can use it in place of $HOME. Interestingly, you can use `echo ~` to retrieve the value of $HOME, but otherwise, ~ is just normal character. If you change your mind after using cd and would like to return to the previous directory, you can use `cd -` to return.  

```
bash$ cd ~
bash$ cd -
bash$ pwd
bash$ 
```

To view the contents of a directory, you can use the list directory contents command `ls`. By default, this lists the contents of your current working directory, but you can specify a path instead. To find out where a command or executable is located, you can use the `which` command. To create a directory, we can make a directory with `mkdir`.  

```
bash$ cd ~
bash$ mkdir foobar; cd foobar
bash$ which pwd
pwd: shell built-in command
bash$ which ls
/bin/ls
bash$ 
```

Note that we use the `cd` command right after creating the directory. We can use ';' to terminate lines of commands and execute code afterwards. Inside our "empty" directory, we will actually have two hidden directories. Any file that begins with a '.' will be hidden by default. Every directory will always have two hidden paths: "." and "..", which are links to itself and it's parent directory, respectively. Note that the parent directory of the root directory is still the root directory. To view hidden files, we can use the "-a" option to view all files. To view more details, we can add the long option "-l" to our command. Note that we can sometimes add these shorthand notations together.  

```
bash$ ls -a
. ..
bash$  ls -la
total 0
drwxr-xr-x    2 foobar  staff    64 Aug 14 00:00 .
drwxr-xr-x+ 100 foobar  staff  2000 Aug 14 00:00 ..
bash$ 
```

Note that the 'd' in front represents the file is a directory. Normal files will have a '-' instead. The next three groups of three characters represent the file permissions from owner, group, and others. The owner is who owns the file. The group refers to any users in the same user group as the owner. The others refer to any other user besides the owner and group users. The three levels of permissions are read 'r', write 'w', and execute 'x'. Reading a file lets a user open the file, or otherwise look at its contents. Write permission allows the user to change the file's contents. If the file is an executable or program, execution permission allows the user to run the file.  

The + means the file has extended permissions, which are beyond the scope of this course. If you would like to see them anyways, you can use the "-e" flag or the `getfacl` command. The next number represents the number of hard links, or absolute path links to this file, which will be addressed shortly. The remaining values are the owner, the group, the number of bytes in the file, the modification date, and the name of the file. For a more human readable version, you can use the "-h" option.  

There are two types of paths: absolute paths and relative paths. A relative path is a path that begins relative to your current working directory. These will begin without a forward slash '/' in front. In contrast, an absolute path always starts from the root directory, begins with a forward slash '/'. To change a file's modification and access times, you can use the `touch` command, which updates both times to the time of running the command by default. If the file does not exists, touching a file will create an empty file of that name.  

```
bash$ touch foo
bash$ 
```

Each file on your machine has an unique inode number. A hard link refers to a specific file in memory, i.e. sharing the same inode number. You can look at the inode number with `ls -i`. In contrast, a soft link points to a path rather than a file. If the file at the path changes, or is removed, we may end up with a dangling soft link, or a link that goes nowhere. We use the `ln` command to create links, with the "-s" option for soft links.  

```
bash$ ln foo bar
bash$ ln -s foo baz
bash$ ls -lih
total 0
123406780 -rw-r--r--  2 foobar  staff     0B Aug 14 23:14 bar
123406781 lrwxr-xr-x  1 foobar  staff     3B Aug 14 23:15 baz -> foo
123406780 -rw-r--r--  2 foobar  staff     0B Aug 14 23:14 foo
bash$ 
```

As we can see, the inode numbers of the files "foo" and "bar" are the same, and their hard link count is 2, as there are exactly two files that refer to that location in memory. In contrast, "baz" is not a hard link but a soft link, with the 'l' indicating a soft link. At the end, you see "baz -> foo", indicating that this soft link "baz" is pointing to the relative path "foo". Note that you can use an absolute path instead in creating soft links.  

Along with `ls`, a common command to list files, including those in sub-directories, is the `find` command.  

```
bash$ mkdir fubar
bash$ touch fubar/fou.txt
bash$ find .
.
./foo
./baz
./bar
./fubar
./fubar/fou.txt
bash$ 
```

Sometimes, you will want to retrieve files from the internet. To retrieve the data from a web page by its URL, you can use the `curl` command. By default, this will output the web file into your terminal. You can use the "-o" option to output the result into a specific file name or path, similar to how you may use "-o" to specify the output executable after compiling some C or C++ code. Another option is to use the `wget` command, to download a file from its web URL. This will be saved, by default, by the last portion of the URL, delimited by the forward slashes. Finally, note that the file name extensions can be anything. It is good practice to have extensions that make sense, to help various applications infer what format the files belong to, but you can name the files anything you would like. For example, downloading "https://web.cs.ucla.edu/classes/spring22/cs35L/assign/assign1.html" will save the contents as an "html" file.  

## 1.3 Suspicious Summons
So far, we have covered several "safe" commands. That is, you will not be able to cause irreversible damage to your machine through moving around your file system and printing out files. Cautiously, we will begin exploring more advanced commands, some of which will cause persistent changes to your files. First of all, it is important to know how to copy files with the `cp` command. The syntax is `cp source destination`, where "source" is the path to the file you want to make a copy of, and "destination' is where you want to copy the file to.  

```
bash$ cp foo fu
bash$ ls
bar   baz    foo    fu    fubar
bash$ 
```

Next, it is important to know how to move or rename files. In Linux, this is done with the move `mv` command. Similarly to `cp`, mv has also requires moving from a source to destination, with the format `mv source destination`. It is important to note that you may end up overwriting files if the destination path already exists.  

```
bash$ mv fu fou
bash$ ls
bar    baz    foo    fou    fubar
bash$ 
```

Removing files and directories may require separate commands. If you have an empty directory, you can use the remove directory command `rmdir` to remove the empty directory. If the directory is not empty, then `rmdir` will fail.  

```
bash$ mkdir empty_dir
bash$ rmdir empty_dir
bash$ echo $?
0
bash$ rmdir fubar
rmdir: fubar: Directory not empty
bash$ echo $?
1
bash$ 
```

Instead, we will use the remove command `rm`. For any ordinary file, we can use the `rm` command to remove the file by specifying the path. For directories, we can recursively remove the contents with the "-r" option and force removal with the "-f" option.  

```
bash$ rm fou
bash$ ls
bar    baz    foo    fubar
bash$ rm -rf fubar
bash$ ls
bar    baz    foo
bash$ 
```

Critically, it is **VERY IMPORTANT** to be aware of wildcards in bash. The '\*' character represents a wildcard that fills in a sequence of characters. Thus, using * by accident may end up removing the entire contents of all sub-directories and files of a given path. Similarly, the '?' character acts as a single character wildcard that can fill in for any other character, and characters inside square brackets "[]" are treated as a set of wildcard characters. Under no circumstances should you attempt to use the command `rm -rf` command without knowing exactly what you are doing and any unintended consequences.  

So far, these commands have been in use sequentially with limited inter-process communication. One of the strengths of these commands is that many can be linked together by redirecting input and output. First, we will explore redirecting standard input, or stdin. To demonstrate this, it would be helpful to use a command that could read in standard input, such as `read`. The syntax is `read var_name`, where var_name is the name of a variable you intend to read the value into. Note that this would by default expect input from the keyboard as stdin. To terminate, or finish entering stdin, you can use the enter key, or use Ctrl + d to close the input.  

```
bash$ read foo
bar
bash$ echo $foo
bar
bash$ 
```

To redirect input, we can use the '<' character. For example, if we had a file hw.txt containing the text "Hello World!", we can read this value into a variable rather than typing the text from the keyboard.  

```
bash$ read line <hw.txt 
bash$ echo $line
Hello World!
bash$ 
```

By default, the standard output is being printed onto the terminal. We can redirect this output to a file with the '>' character, overwriting the file. Note that since the '!' character also has a special meaning, as the NOT boolean operator, we need to escape it with a backslash '\' if using double quotes. If we wanted to append to a file, rather than overwriting it, we can use ">>" to append to the end of a file.  

```
bash$ echo "Hello\!" >hw.txt
bash$ cat hw.txt
Hello!
bash$ echo 'Goodbye!' >>hw.txt
bash$ cat hw.txt
Hello!
Goodbye!
bash$ 
```

Similarly to standard output, standard error controls where the output of error messages will be sent. We can redirect standard error by putting a 2 in front of the redirection operators. Note that 0, 1, and 2 represent standard input, standard output, and standard error respectively. Only the 2 for standard error is necessary to be explicitly written out, as the others are used by default. To close standard input, you can use '<&-' to ensure the command is unable to take in any standard input, while to redirect both standard output and standard error, you can use the '&' character before the output redirection characters (e.g. &> and &>>).  

```
bash$ read foo <&-
bash$ ./foo     
bash: ./foo: Permission denied
bash$ ./foo 2> err.txt
bash$ cat err.txt 
bash: ./foo: Permission denied
bash$ 
```

Other than reading from and writing to files, it is often useful to redirect output from one shell command to the input of another. The pipe operator, '|', allows for passing data directly between commands. One useful command is the word, line, character, and byte count command `wc`. We can redirect the list of directory contents into this counter. The commands options are "-c", for bytes, "-l", for lines, "-m", for characters, and "-w", for words. The order of the outputs is line, word, and byte, and by default, wc will run with "-clw" options.  

```
bash$ ls | wc -l
       5
bash$ 
```

We can also sort inputs with the `sort` command and take the unique values of input with the `uniq` command. The `sort` command must be used before the `uniq` command, as `uniq` relies on removing duplicates only if they are adjacent.  

```
bash$ echo "foo\nbar\nbaz\nfu\nfoo\nbar" | sort | uniq
bar
baz
foo
fu
bash$ 
```

Another useful command is to translate characters with the `tr` command. You can enter stdin from the keyboard by default, or redirect input from elsewhere (e.g. from the echo command). The basic behavior relies on substituting characters from one set to the corresponding character in the second set. The "-c" flag can be used to take the compliment of the first set and replace them. Note that hitting enter would add a '\n' character, which will also get replaced if using "-c". You can use Ctrl + d to end the input instead. The "-s" command suppresses duplicate characters, and the "-d" command can be used to delete certain characters.  

```
bash$ tr o u 
foobar
fuubar
bash$ tr -c fbar u
foobar
fuubaru
bash$ tr -d z       
foobarz
foobar
bash$ tr -s u
fuubar
fubar
bash$ tr -s o u
foobar
fubar
bash$ tr -d z
foobarz
foobar
bash$ 
```

While these commands are useful for examining smaller pieces of text, larger selections of text are often difficult to analyze without searching for key words or phrases. For this purpose, it is easy to look for patterns of text, called regular expressions. Regular expressions are often shorted to "re", "regex", or "regexp". One command for looking at regular expressions is the `grep` command. The most simple regular expressions are simply the literal strings of text you wish to find.  

```
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "foo"
foo
foobar
bash$ 
```

To look at specific sequences of characters, you can use sets "[]", which are unordered, for sets of characters that could be used in that character's location, and groups "()", which are ordered strings of characters that must all be present. Note that by default, `grep` will be using basic regular expressions (BREs). Some features, such as groups, are considered extended regular expressions (EREs), and require either backslashes to obtain the special functionality, or the "-E" flag for extended regular expressions.  

```
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "f[ou]"
foo
fubar
foobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "\(oo\)"
foo
foobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "oo"  
foo
foobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "(oo)"
foo
foobar
bash$ 
```

It is also useful to use some shortcuts in your groups. Rather than listing the entire alphabet, you can use sequences of ASCII characters using a '-' in between. This is commonly used for, but not limited to, lowercase characters "a-z", uppercase characters "A-Z", and digits "0-9".  

```
bash$ echo "abc\nxYz\n123" | grep "[a-z]"
abc
xYz
bash$ echo "abc\nxYz\n123" | grep "[A-Z]"
xYz
bash$ echo "abc\nxYz\n123" | grep "[0-9]"
123
bash$ 
```

By default, `grep` will look for the regex in any part of the input line. You can use the anchors '^' and '$' to indicate the start and end of an expression, respectively.  

```
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "^bar"
bar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "foo$"
foo
bash$ 
```

If there are repeated patterns, you can specify specific quantities of these patterns. The characters '?', '\*', and '+' represent "0 or 1", "0 or more", and "1 or more" instances of the previous pattern. You can also use the '|' character to indicate OR between expressions.  

```
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "fu?" 
foo
fubar
foobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep "fu*"   
foo
fubar
foobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "fu+"
fubar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "f(oo)|u" 
foo
fubar
foobar
bash$ 
```

Finally, we can use curly brackets to indicate specific quantities or ranges of repeated expressions.  

```
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "f[ou]{1}b"
fubar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "f[ou]{2}b"
foobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | grep -E "f[ou]{1,2}b"
fubar
foobar
bash$ 
```

Another common command is `sed`, which is useful for editing strings using regular expressions, which has multiple uses. The `sed` command starts with a command option, a regular expression, a second regular expression, and then another option. One such use is for substituting text, using 's'. By default, this substitutes the first match, and you can set it to global with 'g'. You can also match groups using '\' before the group number.  

```
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | sed "s/o/u/"
fuo
bar
baz
fubar
fuobar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | sed "s/o/u/g"
fuu
bar
baz
fubar
fuubar
bash$ echo "foo\nbar\nbaz\nfubar\nfoobar" | sed -E "s/(oo)/\1\1/g"
foooo
bar
baz
fubar
foooobar
bash$ 
```

With these more advanced commands, some of which may be dangerous, it is useful to ensure that users have the correct permissions to the files. To alter the permissions, you can use the `chmod` command. The permissions binary permissions of read, write, and execute can be read as a base 8 integer. Thus, converting to base 8, you can then alter specific permissions for each of the groups of users.  

```
bash$ chmod 777 foo
bash$ ls -l
total 16
-rwxrwxrwx  2 foobar  staff   0 Aug 14 23:14 bar
lrwxr-xr-x  1 foobar  staff   3 Aug 14 23:15 baz -> foo
-rw-r--r--  1 foobar  staff  30 Aug 17 16:15 err.txt
-rwxrwxrwx  2 foobar  staff   0 Aug 14 23:14 foo
-rw-r--r--  1 foobar  staff  16 Aug 17 16:07 hw.txt
bash$ 
```

You can also specify group level permissions, adding or subtracting permissions with '+' and '-', using 'r', 'w', and 'x' for the permission levels. You can use 'a' to indicate all users, and have multiple permissions toggled at the same time.  

```
bash$ chmod go-xw foo
bash$ ls -l
total 16
-rwxr--r--  2 foobar  staff   0 Aug 14 23:14 bar
lrwxr-xr-x  1 foobar  staff   3 Aug 14 23:15 baz -> foo
-rw-r--r--  1 foobar  staff  30 Aug 17 16:15 err.txt
-rwxr--r--  2 foobar  staff   0 Aug 14 23:14 foo
-rw-r--r--  1 foobar  staff  16 Aug 17 16:07 hw.txt
bash$ chmod -w foo
bash$ ls -l
total 16
-r-xr--r--  2 foobar  staff   0 Aug 14 23:14 bar
lrwxr-xr-x  1 foobar  staff   3 Aug 14 23:15 baz -> foo
-rw-r--r--  1 foobar  staff  30 Aug 17 16:15 err.txt
-r-xr--r--  2 foobar  staff   0 Aug 14 23:14 foo
-rw-r--r--  1 foobar  staff  16 Aug 17 16:07 hw.txt
bash$ chmod a+x foo
bash$ ls -l
total 16
-r-xr-xr-x  2 foobar  staff   0 Aug 14 23:14 bar
lrwxr-xr-x  1 foobar  staff   3 Aug 14 23:15 baz -> foo
-rw-r--r--  1 foobar  staff  30 Aug 17 16:15 err.txt
-r-xr-xr-x  2 foobar  staff   0 Aug 14 23:14 foo
-rw-r--r--  1 foobar  staff  16 Aug 17 16:07 hw.txt
bash$ chmod u+rwx foo
bash$ ls -l
total 16
-rwxr-xr-x  2 foobar  staff   0 Aug 14 23:14 bar
lrwxr-xr-x  1 foobar  staff   3 Aug 14 23:15 baz -> foo
-rw-r--r--  1 foobar  staff  30 Aug 17 16:15 err.txt
-rwxr-xr-x  2 foobar  staff   0 Aug 14 23:14 foo
-rw-r--r--  1 foobar  staff  16 Aug 17 16:07 hw.txt
bash$ 
```

Some commands that alter more important system files will require the user to run as root, or use super user permissions. This should be used only if you know what you are doing, as the `sudo` command may allow destructive commands to irreversibly alter your machine. As such, on remote Linux servers, you are unlikely to have the `sudo` command. The `sudo` command should be avoided for general use, similar to `vi` or `vim` being not recommended for command line text editor usage. Instead, `emacs` is recommended as the most versatile and comprehensive text editor and integrated development environment (IDE), with custom functions, libraries, and superior keybindings.  

The files covered so far can easily be read by humans, using the Emacs text editor, or using commands such as `cat`, `head`, `tail`, `more`, and `less`. However, if you were to send these uncompressed text files to someone else, it would be an inefficient waste of memory and time. Thus, it is useful to compress files before sending them, such as for submitting a homework assignment. One commonly used compression command is `gzip`, which compresses a file using Lempel-Ziv coding. The original file will then be replaced by a compressed file, with ".gz" appended at the end of the original file name.  

```
bash$ gzip hw.txt
bash$ ls -l
total 16
-rwxr-xr-x  2 foobar  staff   0 Aug 14 23:14 bar
lrwxr-xr-x  1 foobar  staff   3 Aug 14 23:15 baz -> foo
-rw-r--r--  1 foobar  staff  30 Aug 17 16:15 err.txt
-rwxr-xr-x  2 foobar  staff   0 Aug 14 23:14 foo
-rw-r--r--  1 foobar  staff  16 Aug 17 16:08 hw.txt.gz
bash$ 
```

To take a sneak peak at the compressed file, you can use the `zcat` command.  

```
bash$ zcat hw.txt.gz
Hello!
Goodbye!
bash$ 
```

To unzip the compressed file, you can use `gunzip`, which replaces the compressed file with the uncompressed file, with the ".gz" file extension removed from the file name.  

```
bash$ gunzip hw.txt.gz
bash$ ls hw.txt.gz
ls: hw.txt.gz: No such file or directory
bash$ ls hw.txt
hw.txt
bash$ 
```

Finally, it is useful to know how to transfer files between your local machine and remote Linux servers, as well as how to log into remote Linux servers. To log into a server, you can use the `ssh` command. To copy a file to or from your machine and the remote server, you can use the `scp` command to send files by their paths. To send a directory, you will need to use the "-r" flag. Note that the `scp` command needs to be used in a terminal currently connected on your local machine.  

```
bash$ ssh foobar@lnxsrv12.seas.ucla.edu
foobar@lnxsrv12:~/$ logout
bash$ scp ./hw.txt foobar@lnxsrv12.seas.ucla.edu:/u/cs/ugrad/foobar/
bash$ scp foobar@lnxsrv12.seas.ucla.edu:/u/cs/ugrad/foobar/hw.txt .
bash$ cd ..
bash$ scp -r foobar foobar@lnxsrv12.seas.ucla.edu:/u/cs/ugrad/foobar/
bash$ scp -r foobar@lnxsrv12.seas.ucla.edu:/u/cs/ugrad/foobar/foobar .
```

## 1.4 Shell Scripting
So far, the commands we covered can all be done in a single command line. Bash, as a language, can be used more intricately used to tie together scripts in various languages through shell scripts, which are files that contain lines of code to be run through the command line. To begin each file, it is highly recommended to specify which version of bash you are using with the "#!" as the first line in the file.  

```
#!/usr/local/cs/bin/bash
```

On SEASnet, the user should have /usr/local/cs/bin prepended to your path. You can use the command `export PATH=/usr/local/cs/bin:$PATH` to make this change. Here, this is taking the variable $PATH, and setting the value to the string /usr/local/cs/bin:$PATH, where it is adding text in front of the current $PATH variable value. When the system is looking for commands, it will read the $PATH from left to right to search for the command's locations. The ':' serves as a delimiter between different available paths. To avoid needing to execute this command each time you log in, you can add the command to the end of your ~/.bashrc file, or equivalent, for the shell to execute the command upon starting up. Note that there should be no spaces around the '=' sign in variable assignments.  

Another notable feature of bash is that variables are not explicitly typed. At runtime, bash will figure out whether the variables are strings, integers, or so on. Accessing variables is very simple, with just a '$' in front of the variable name required. However, this raises an interesting issue: How does bash tell when the variable name ends? Bash will use variable name expansion, reading the variable name until it is no longer a variable name. To address this issue, you can use "\${}" to ensure your variable names do not get mixed up with the following text. This is considered best practice unless the variable name is very clear, unique, and unlikely to be mixed up with other text.  

```
bash$ foo=1
bash$ foobar=2
bash$ echo "$foo"
1
bash$ echo "$foobar"
2
bash$ echo "${foo}bar"
1bar
bash$ 
```

Having multiple lines to work with allows easier usage of loops. _While_ loops can be done in the command line, it is more difficult _for_ the user to keep track of the syntax. The simplest for loop is to loop over some files. A semi-colon ';' is sometimes used to put the "do" on the first line.  

```
for i in ./*; do
    echo $i
done
for i in ./*
do
    echo $i
done
for i in `ls`
do
    echo $i
done
```

Another type of loop is to loop over ranges. The seq command can generate a sequence from 1 to the input value, or between start and end, inclusive.  

```
for i in {1..5}
do
    echo $i
done
for i in `seq 3`
do
    echo $i
done
for i in `seq 3 1`
do
    echo $i
done
for i in `seq 2 4`
do
    echo $i
done
```

C-like loops are also possible.  

```
for ((i = 0; i < 10; i++))
do
    echo $i
done
```

`While` loops are also available, commonly used to iterate through lines of a file.  

```
cat hw.txt | while read line
do
    echo $line
done
while read line; do
    echo $line
done < hw.txt
```

More traditional `while` loops, with numerical limits, are also frequently used. Numerical calculations are done with double parentheses "$(())" while boolean comparisons use double square brackets "[[]]". Also note that there is a necessary space between the elements in the double square brackets "[[]]".  

```
i=0
while [[ $i -lt 10 ]]
do
    i=$((i+1))
    echo $i
done
```

Conditional statements are often used in conjunction with loops.  
```
i=10
while true
do
    i=$((i-1))
    if [[ $i -gt 0 ]]
    then
        if [[ `expr $i % 2` -eq 0 ]]
        then
            continue
        fi
        echo $i
        
    else
        echo "DONE!"
        exit
    fi
done
```

As seen above, `continue` can be used to let a loop skip to the next iteration, `exit` can be used to exit end an infinite loop, and `expr` can be used to evaluate mathematical expressions. For numerical boolean expressions, normal math operators are generally not allowed. Instead, use "-lt" for "less than", "-le" for "less than or equals", "-eq" for "equals", "-ge" for "greater than or equals", and "-gt" for "greater than". For strings, "==" is used for equality, "!=" is used for inequality, "-n" is used for empty string, and "-z" is used for non-empty string. For booleans, the usual boolean operators "&&", "||", and "!" are used to represent AND, OR, and NOT, respectively.  

It is also useful to load command line arguments. The value stored in `$#` contains the number of command line arguments, with `$i` storing the value of the ith command line argument, with `$0` storing the path of the script that was executed. If an argument is not passed in, e.g. an optional parameter, we can use parameter expansion to fill in the default values.  

#### demo.sh
```
#!/bin/bash

echo $#
echo $0
foo=$1
echo ${foo:=100}
```
#### terminal
```
bash$ ./demo.sh
0
./demo.sh
100
bash$ ./demo.sh 200
1
./demo.sh
200
bash$ 
```

Finally, it is useful to be able to use some basic data structures and write some basic functions. Bash arrays are very similar to ordinary variables. However, the implementation may depend on your shell language. In bash, arrays are zero indexed.  

```
bash$ my_array=(This is an array)
bash$ echo ${my_array[0]}
This
bash$ 
```

However, in some shell languages, such as zsh, arrays are 1-indexed.  

```
zsh% my_array=(This is an array)
zsh% echo ${my_array[1]}
This
zsh% 
```

Functions are fairly similar to functions in C-like languages. You can define a function using parentheses after a function name and enclose the code within curly braces. Functions and arrays are a bit beyond the scope of this course.  

```
bash$ greet() { echo "Hello World." }
bash$ greet
Hello World.
bash$ 
```

## 1.5 Succinct Summary
The Linux operating system is widely used and held in high regard by most developers. Understanding the ins and outs of the linux operating system is crucial for effective software construction. In this chapter, we introduced the linux operating system with some safe commands, before moving on to some more advanced and more dangerous commands. Later, we provided a precursory introduction to writing shell scripts, with the most common building blocks of any imperative programming language, using variables, loops, and conditionals. This chapter is not all encompassing, and there are various other topics to discuss later in this book. In particular, we will revisit linux in chapter 6 from the perspective of software construction with remote servers. For future reference, please use the [Bash Cheat Sheet](https://devhints.io/bash) for more detailed scripting syntax.  

#### [Return to Main Table of Contents](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/README.md#table-of-contents)
Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)  
