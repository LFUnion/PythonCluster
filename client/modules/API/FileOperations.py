"""
Module "FileOperations"
Copyright (C) 2014  Leon Schwalb and Fabian Stein

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def readFile(filename):
    file = open(str(filename), "r")
    fileContent = file.read()
    file.close()

    return fileContent

def writeFile(filename, fileContent):
    file = open(str(filename), "w")
    file.write(str(fileContent))
    file.close()

def clearFile(filename):
    file = open(str(filename), "w")
    file.truncate()
    file.close()

def checkIfFileExists(filename):

    try:
        file = open(str(filename), "r")
        file.close()
        return True
        
    except Exception:
        return False

