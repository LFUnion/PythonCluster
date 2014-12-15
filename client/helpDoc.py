"""
ClusterShell, a program to control the Cluster
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

def help():
    print()
    print("Help")
    print()
    print("exit:        Exit the session")
    print("clear:       Clear screen")
    print("last:        Execute last command")
    print("calculate:   Type in a formula")
    print("load:        Load the network standart configuration")
    print("prime:       Calculate primes")
    print("clusterhelp: Special help for the cluster programs")

def clusterhelp():
    print()
    print("Cluster Help")
    print()
    print("clusterinit:     Initialize the cluster network")
    print("clustercheck:    Check the cluster servers")
    print("clustertestprog: Just a little test ;)")
    print()
