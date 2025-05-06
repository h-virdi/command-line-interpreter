# Command-Line Interpreter

This is a command-line interpreter project built in Python. It supports basic commands like `cd`, `ls`, `clear` and `rm`.

## Features
- Navigate directories using `cd`
- List files and directories in the current working directory using `ls`
- Print the current working directory using `pwd`
- Clear previous commands using `clear`
- Remove files using `rm`

## Installation
Clone the repository and run this:
```bash
git clone https://github.com/h-virdi/command-line-interpreter.git
cd command-line-interpreter
python3 command.py

## Example Usage
(mycommand) > ls
command.py
empty
empty.py
README.md
.git
(mycommand) > mv empty.py empty
Moved from 'empty.py' to 'empty'
(mycommand) > cd empty
Changed directory to /Users/harnoor/command-line-interpreter/empty
(mycommand) > pwd
/Users/harnoor/command-line-interpreter/empty
(mycommand) > ls
empty.py
(mycommand) > rm empty.py
Removed file: empty.py
(mycommand) > ls
(mycommand) > cd ..
Changed directory to /Users/harnoor/command-line-interpreter
(mycommand) > ls
command.py
empty
README.md
.git
(mycommand) > quit
