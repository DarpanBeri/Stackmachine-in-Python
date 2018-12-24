two_word_commands = ["push","save","get"]
one_word_commands = ["pop","add","sub","mul","div","mod","skip"]
tok_commands = ['pop','add','sub','mul','div','mod','skip','push','save','get']

def checkNum(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def Tokenize(str):
    """Takes in an input string and outputs a list of tokens if valid or ValueError if invalid"""

    l_tokens = str.split() # Input string split in a list

    for Tok in l_tokens:

        if Tok in tok_commands or checkNum(Tok): # all good
            pass
        else:
            raise ValueError("Unexpected Token: "+ Tok) # ERROR

    return l_tokens # all good return list

def Parse(token):
    """Checks if the commands follow syntatic grammar or not"""

    if(token[0] in one_word_commands and len(token) == 1): # one word check
        return True

    elif(token[0] in two_word_commands and len(token) == 2 and checkNum(token[1])):
        return True
    return False # check failed


"""Test
test_str = "pop"
print(Tokenize(test_str))
test_parse = Tokenize(test_str)
print(Parse(test_parse))"""
