## StackMachine in Python
**Note:** The following commands are valid:
    * push # -- Pushes the number onto the stack.
    * pop -- Pops the top of the stack.
    * add -- Pops two values oﬀ the stack, adds them pushes the result.
    * sub -- Pops two, subtracts the second from the first, pushes result.
    * mul -- Pops two, multiples, pushes result.
    * div -- Pops two, divides the first by the second, pushes result.
    * mod -- Pops two, remainder of first divided by second, pushes result.
    * skip -- Pops two.
    * save # -- Pops one, saves that value for future retrieval.
    * get # -- Pops zero. Gets a previously saved value and pushes it on the stack.

#### Files included:
    Prog4_1.py:
        This file contains Tokenizer and Parser functions which run through an input line by line.
    Prog4_2.py:
        This file contains a StackMachine class that builds a virtual machine that can execute tokenized and parsed commands from prog4_1.py.
    Prog4_3.py:
        This is a driver program which combines prog4_1.py and prog4_2.py. It allows a file to be tokenized and parsed by prog4_1.py, whose output is then fed to prog4_2.py, executing the commands in that file. On flawless execution, the program prints "Program terminated correctly."

#### Example execution:
    python3  prog4_3.py <file>
**Note**: <> are not the part of the command

#### file contents:
    push 3
    foobar 3.14
    pop

#### Example run:
    Error on line 2: Unexpected token: foobar

#### file contents:
    push 3
    push 4
    add

#### Example run:
    7

Darpan Beri

darpanberi.99@gmail.com || dberi@sdsu.edu
