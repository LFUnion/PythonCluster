import client, highValueClient, FileOperations

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

def clusterinit():
    
    ClusterCount = int(input("Please enter the amount of cluster servers in your network > "))

    counter = 1

    while counter <= ClusterCount:
        ip = input("Please enter the IP of server #" + str(counter) + " > ")
        ip = ip + " "
        cluster = FileOperations.readFile("clusterIndex.cli")
        FileOperations.writeFile("clusterIndex.cli", (cluster + ip))
        counter += 1

    print("Done!")

def clusterdelete():
    really = str(input("This will remove your whole Cluster configuration. Are you sure you will delete it? [y/n] > "))
    if(really == "y"):
        FileOperations.clearFile("clusterIndex.cli")
        print("Configuration removed")
    else: print("Aborted")

def clustercheck():

    success = True

    clusterIndexRaw = FileOperations.readFile("clusterIndex.cli")

    clusterIndex = clusterIndexRaw.split()

    ClusterCount = len(clusterIndex)

    counter = 0

    while counter < ClusterCount:

        try:

            get = client.connect(clusterIndex[counter], 10008, "1+1")

            if(get == "2"):
                print("Server " + clusterIndex[counter] + " OK")
                counter += 1

            else:
                print("Server " + clusterIndex[counter] + " FAIL")
                counter += 1
                success = False

        except Exception:

            print("Server " + clusterIndex[counter] + " FAIL (EXCEPTION IN CODE)")
            counter += 1
            success = False

    print("Done!")
    return success

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

    if(clusterComputer > clusterLenght):
        print("ERROR!")

    elif highValue == 1:
        get = highValueClient.connect(clusterIndex[(clusterComputer - 1)], 10008, command)
    else:
        get = client.connect(clusterIndex[(clusterComputer - 1)], 10008, command)
    return get
