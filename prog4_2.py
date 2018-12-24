class StackMachine:
    def __init__(self):
        self.CurrentLine = 0
        self._data = []
        self._Memory = {}

    def Execute(self,tokens):
        self.CurrentLine += 1

        if(tokens[0] == "push"):
            self._data.append(int(tokens[1]))
            return

        elif(tokens[0] == "pop"):
            if(len(self._data) == 0):
                raise IndexError("Invalid Memory Access")
            else:
                return self._data.pop()

        elif(tokens[0] == "add"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _sum = first + second
                self._data.append(_sum)
                return

        elif(tokens[0] == "sub"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _dif = first - second
                self._data.append(_dif)
                return

        elif(tokens[0] == "mul"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _prod = first * second
                self._data.append(_prod)
                return

        elif(tokens[0] == "div"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _quo = first / second
                self._data.append(_quo)
                return

        elif(tokens[0] == "mod"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                _mod = first % second
                self._data.append(_mod)
                return

        elif(tokens[0] == "skip"):
            if(len(self._data) < 2):
                raise IndexError("Invalid Memory Access")
            else:
                first = self._data.pop()
                second = self._data.pop()
                if(first == 0):
                    self.CurrentLine += second
                return

        elif(tokens[0] == "save"):
            if(len(self._data) == 0):
                raise IndexError("Invalid Memory Access")
            else:
                saveVal = self._data.pop()
                loc = int(tokens[1])
                self._Memory[loc] = saveVal
                return

        elif(tokens[0] == "get"):
            loc = int(tokens[1])
            if(loc in self._Memory):
                saveVal = self._Memory[loc]
                self._data.append(saveVal)
                return
            else:
                raise IndexError("Invalid Memory Access")
