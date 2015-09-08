from modules.API import FileOperations
from modules.API import ClusterAPI
import client
"""
The ClusterAPI interface
Copyright (C) 2015 Leon Schwalb and Fabian Stein

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

def com():
    return [["clusterinit", "ClusterHelper.clusterinitUI()"], ["clusterdelete", "ClusterHelper.clusterdeleteUI()"], ["clustercheck", "ClusterHelper.clustercheckUI()"], ["callmethods", "ClusterHelper.callmethodUI()"]]

def clusterinitUI():
    
    ClusterCount = int(input("Please enter the amount of cluster servers in your network > "))

    counter = 1

    while counter <= ClusterCount:
        ip = input("Please enter the IP of server #" + str(counter) + " > ")
        ip = ip + " "
        cluster = FileOperations.readFile("clusterIndex.cli")
        FileOperations.writeFile("clusterIndex.cli", (cluster + ip))
        counter += 1

    print("Done!")

def clusterdeleteUI():
    really = str(input("This will remove your whole Cluster configuration. Are you sure you will delete it? [y/n] > "))
    if(really == "y"):
        FileOperations.clearFile("clusterIndex.cli")
        print("Configuration removed")
    else: print("Aborted")

def clustercheckUI():

    success = True

    clusterIndexRaw = FileOperations.readFile("clusterIndex.cli")

    clusterIndex = clusterIndexRaw.split()

    ClusterCount = len(clusterIndex)

    counter = 0

    while counter < ClusterCount:

        try:

            get = client.connect(clusterIndex[counter], 10008, "1+1")

            if(int(float(get)) == 2):
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

def callmethodUI():
    print("Which nodes callmethod do you want to change? (0 = all)")
    node = int(input("> "))
    print("What callmethod should be used? (c++ / python)")
    method = input("> ")
    
    if node == 0:
        result = ClusterAPI.setCallmethodAll(method)
    elif node <= ClusterAPI.getClusterLenght() and node > 0:
        result = ClusterAPI.setCallmethod(node - 1, method)
    else:
        print("Invalid node")

    if result == True:
        print(">> Done")
    else:
        print(">> Error: Server denied")
        
