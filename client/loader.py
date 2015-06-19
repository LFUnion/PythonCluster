from modules import *
from modules.API import ClusterAPI

global mods
mods = dir()

"""
Module "loader.py", responsible for module handling.
Copyright (C) 2015  Leon Schwalb and Fabian Stein

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

def load():

    global mods
    global commands
    global rawlist
    global failed
    
    commands = []
    rawlist = []
    failed = []
    
    for mod in mods:
        if("__" in mod):
            mods.remove(mod)

    for mod in mods:
        try:
            global coms
            coms = eval(mod + ".com()")
            rawlist += coms
        except:
            failed.append(mod)

    for raw in rawlist:
        commands += raw

def srch(inp):
    
    global commands
    global rawlist
    
    if(inp in commands):
        for raw in rawlist:
            for rawc in raw:
                if(rawc == inp):
                    exec(raw[1])
                    return True

def getlen():
    global rawlist
    return len(rawlist)

def showmodules():
    global rawlist
    global failes

    for module in rawlist:
        print("Loaded module "+ module[0])
