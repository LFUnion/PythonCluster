import client, highValueClient
from modules.API import FileOperations

"""
The ClusterAPI
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

def getClusterLenght():

    get = ""

    clusterIndexRaw = FileOperations.readFile("clusterIndex.cli")

    clusterIndex = clusterIndexRaw.split()

    clusterLenght = len(clusterIndex)

    return clusterLenght

def execute(clusterComputer, command, highValue):

    clusterIndexRaw = FileOperations.readFile("clusterIndex.cli")

    clusterIndex = clusterIndexRaw.split()

    clusterLenght = len(clusterIndex)

    get = ""

    if(clusterComputer > clusterLenght):
        get = "ERROR!"

    elif highValue == 1:
        get = highValueClient.connect(clusterIndex[(clusterComputer - 1)], 10008, command)
    else:
        get = client.connect(clusterIndex[(clusterComputer - 1)], 10008, command)
    return get

def clustercheck():

    success = True

    clusterIndexRaw = FileOperations.readFile("clusterIndex.cli")
    clusterIndex = clusterIndexRaw.split()
    ClusterCount = len(clusterIndex)

    counter = 0

    while counter < ClusterCount:

        try:
            get = client.connect(clusterIndex[counter], 10008, "1+1")

            if(int(get) == 2):
                counter += 1
            else:
                counter += 1
                success = False

        except Exception:
            counter += 1
            success = False
    return success

def setCallmethod (clusterServer, callmethod):
    if callmethod == "c++":
        execute(clusterServer, "SETCALLMETHOD<C++>", 0)
    else:
        execute(clusterServer, "SETCALLMETHOD<PYTHON>", 0)

def setCallmethodAll (callmethod):
    for server in range(getClusterLenght()):
        if callmethod == "c++":
            execute(server, "SETCALLMETHOD<C++>", 0)
        else:
            execute(server, "SETCALLMETHOD<PYTHON>", 0)
