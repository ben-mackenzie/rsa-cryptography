'''
Created on Apr 12, 2018
with help from: https://gist.github.com/wings27/a7ffc67657d902e77f7d3ff688728efc
'''

class Scanner:
    def __init__(self, sourceFile):
        self.__file = open(sourceFile, "r")
        self.__file_split = [line.strip() for line in self.__file.readlines()]
        self.__line = None
        self.__line_split = None
        self.__pointer = None

    def _next_int(self):
        try:
            next_str = self._next_str()
            ret = int(next_str)
            return ret
        except ValueError:
            return None

    def _next_str(self):
        if not self.__line_split or self.__pointer >= len(self.__line_split):
            self.__line_split = self.__next_line().split()
            self.__pointer = 0

        if not self.__line_split:
            return ''

        next_one = self.__line_split[self.__pointer]
        self.__pointer += 1
        return str(next_one)
    
    
    def __next_line(self):
        if not self.__line:
            self.__line = 0
        line = self.__file_split[self.__line]
        self.__line += 1
        return line

