import os

"""
Module "calculate.py"
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
    return [["calculate", "calculate.cal()"]]

def cal():

    os.system("clear")
    print("Calculate ALPHA 0.0.1")
    print("(c) ClusterAG 2014. All rights reserved.")
    print()

    formula = input("Please type in the formula > ")

    try:
        print("\nResult: " + str(eval(formula)) + "\n")
        input("Press enter to continue")
    
    except Exception:
        print("\nWhoops, can´t calculate your formula. Sorry :( \n")
        input("Press enter to continue")

    finally:
        os.system("clear")
