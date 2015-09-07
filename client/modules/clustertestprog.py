import _thread
from modules.API import ClusterAPI

"""
Module "clustertestprog"
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

def com():
    return [["clustertestprog", "clustertestprog.start()"]]

def bfl(counter, x):
    multiplicator = 99
    #command = str(multiplicator) + " ** (" + str(multiplicator) + " + " + str(counter) + ")"
    #command = "pow(" + str(multiplicator) + ", " + str(multiplicator) + " + " + str(counter) + ")"
    command = "40 - 4.5"
    print(ClusterAPI.execute(counter, command, 1))
    print("\n")

def start():
    if(ClusterAPI.clustercheck != False):

        clusterLenght = ClusterAPI.getClusterLenght()

        counter = 1

        while counter <= clusterLenght:
            _thread.start_new_thread(bfl, (counter, "x"))
            counter += 1

        print("Calculating. Please wait.")

    else:

        print("Theres something wrong with your cluster configuration. Check it with *clustercheck*")
