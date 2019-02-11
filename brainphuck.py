import sys

TAPE = [0]
TAPE_LEN = 1
TAPE_POINTER = 0

INPUT_STREAM = ""

CODE = ""
CODE_POINTER = 0

OPCODES = { '+':  lambda: plus(),
            '-':  lambda: minus(),
            '<':  lambda: less(),
            '>':  lambda: greater(),
            '[':  lambda: openSquare(),
            ']':  lambda: closedSquare(),
            '.':  lambda: dot(),
            ',':  lambda: comma(),
            '@':  lambda: at()
          }

# >
def greater():
    global TAPE, TAPE_LEN, TAPE_POINTER
    TAPE_POINTER += 1
    if TAPE_POINTER == TAPE_LEN:
        TAPE.append(0)
        TAPE_LEN += 1

# <
def less():
    global TAPE, TAPE_LEN, TAPE_POINTER
    TAPE_POINTER -= 1
    if TAPE_POINTER == -1:
        TAPE = [0] + TAPE
        TAPE_LEN += 1
        TAPE_POINTER = 0

# +
def plus():
    global TAPE, TAPE_LEN, TAPE_POINTER
    TAPE[TAPE_POINTER] += 1
    TAPE[TAPE_POINTER] %= 256

# -
def minus():
    global TAPE, TAPE_LEN, TAPE_POINTER
    TAPE[TAPE_POINTER] -= 1
    TAPE[TAPE_POINTER] %= 256

# .
def dot():
    global TAPE, TAPE_LEN, TAPE_POINTER
    print(chr(TAPE[TAPE_POINTER]), end='')

# ,
def comma():
    global TAPE, TAPE_LEN, TAPE_POINTER, INPUT_STREAM
    while len(INPUT_STREAM) == 0:
        INPUT_STREAM = input()
    TAPE[TAPE_POINTER] = ord(INPUT_STREAM[0])
    if len(INPUT_STREAM) == 1:
        INPUT_STREAM = ""
    else:
        INPUT_STREAM = INPUT_STREAM[1:]

# [
def openSquare():
    global TAPE, TAPE_LEN, TAPE_POINTER, CODE, CODE_POINTER
    if TAPE[TAPE_POINTER] == 0:
        openBrackets = 1
        while openBrackets:
            CODE_POINTER += 1
            if CODE[CODE_POINTER] == '[':
                openBrackets += 1
            elif CODE[CODE_POINTER] == ']':
                openBrackets -= 1

# ]
def closedSquare():
    global TAPE, TAPE_LEN, TAPE_POINTER, CODE, CODE_POINTER
    if TAPE[TAPE_POINTER] != 0:
        closedBrackets = 1
        while closedBrackets:
            CODE_POINTER -= 1
            if CODE[CODE_POINTER] == ']':
                closedBrackets += 1
            elif CODE[CODE_POINTER] == '[':
                closedBrackets -= 1

# @
def at():
    global TAPE, TAPE_LEN, TAPE_POINTER, CODE, CODE_POINTER
    assert CODE_POINTER != 0
    print()
    print("DEBUG - Memory dump")
    print("Breakpoint after instruction {0} {1}".format(CODE_POINTER-1, CODE[CODE_POINTER-1]))
    print("Index\tValue\tPointer")
    for i in range(TAPE_LEN):
        print("{0}\t{1}\t{2}".format(i, TAPE[i], ["<---" if i == TAPE_POINTER else ""][0]))
    input("Press enter to continue execution")

# ---------------------------------------------------- #

if len(sys.argv) < 2:
    print("Specify the file to execute as parameter")
    exit()

with open(sys.argv[1]) as program:
    CODE = list(filter(lambda ch: ch in "+-<>[].,@", program.read()))

codeLength = len(CODE)
while CODE_POINTER < codeLength:
    ch = CODE[CODE_POINTER]
    OPCODES[ch]()
    CODE_POINTER += 1
