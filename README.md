# Brainphuck
A Python implementation of the Brainfuck esoteric programming language.

## How to use it

Write the program on a text file and then execute the script ```brainphuck.py``` in the Python 3 interpreter giving as command line parameter the created file. For example:
```
    python brainphuck.py hello.bf
```

## Implementation details

* The interpreter simulates the eight commands of the Brainfuck programming language, plus an extra character ```@``` which is used for debugging purposes. When executed, it suspends the program and prints on the command line the state of the machine.

* It is always possible to go left or right on the memory tape.

* Each memory cell can contain an integer between 0 and 255.

* An open (closed) square without a matching closed (open) square results in an undefined behaviour.