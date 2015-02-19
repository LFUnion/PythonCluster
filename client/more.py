# more, the simple library for more commands

# Here you can import your program like:
# import program
import client, ClusterAPI, clustertestprog, massformula, egg

"""
Module "more.py", for easy program imports.
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

def more(inp):
    # Here you get 'inp' from 'ui.py'.
    # You can use your own commands here.
    # Example:
    
    if inp == "example":
        print("Example")
        return True
    elif inp == "browserauth":
        print(browserauth.auth() + "\n")
        return True
    elif inp == "clusterinit":
        ClusterAPI.clusterinit()
        return True
    elif inp == "clustercheck":
        ClusterAPI.clustercheck()
        return True
    elif inp == "clusterdelete":
        ClusterAPI.clusterdelete()
        return True
    elif inp == "clustertestprog":
        clustertestprog.start()
        return True
    elif inp == "formula":
        massformula.main()
        return True
    elif inp == "thedevs":
        egg.egg()
        return True
    else:
        return False
