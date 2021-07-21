#! /usr/bin/env python3

import sys

class Gaussian():
    """Gaussian input file (str) -> Gaussian()
    Gaussian is has an empty line to separate sections in the input file. We use 
    that to extract data from the input file to the Gaussian() class

    Input file structure
        keywords
        -[empty line 1]
        title
        -[empty line 2]
        spin + multiplicity
        -[empty line 2]
        coordination
        -[empty line 4]
        footer(atom-connectivity, custom basis set etc...)
        -[empty line 5]
    """
    def __init__(self, inputFile: str) -> None:
        self._inputFile   = []   # stores initial gaussian input file
        self._keywords    = []
        self._tittle      = ""
        self._spinMulti   = ""
        self._footer      = ""    
        self._coordinates = []
        self._blanklines  = [0]


        with open(inputFile, 'r') as gIn: self._inputFile = gIn.readlines()
        nLines = len(self._inputFile)

        # exit if the input file has less than 4 lines
        if nLines < 5:
            print('Error in the input file! Please check')
            sys.exit()

        # get all blank line indicies
        for n, line in enumerate(self._inputFile):    
            if len(line.split()) == 0:
                self._blanklines.append(n)
        # add last line + 1 to blank lines list
        if self._blanklines[-1] < nLines -1:
            self._inputFile.append("\n")
            self._blanklines.append(nLines)
        
        # Extract Gaussian data by looking at blank lines
        self._keywords     = self._inputFile[self._blanklines[0]:self._blanklines[1]]
        self._tittle       = self._inputFile[self._blanklines[1]+1:self._blanklines[2]]
        self._spinMulti    = self._inputFile[self._blanklines[2]+1:self._blanklines[2]+2]
        self._coordinates  = self._inputFile[self._blanklines[2]+2:self._blanklines[3]]
        self._footer       = self._inputFile[self._blanklines[3]+1:self._blanklines[-1]]

        
if __name__ == "__main__":
    pass