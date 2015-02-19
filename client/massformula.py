import ClusterAPI, _thread, os

"""
    Script "massformula"
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


formulas = []
results = []

def calc(clServer, formula):
    orig = clServer
    if(clServer > ClusterAPI.getClusterLenght()):
        clServer = ClusterAPI.getClusterLenght()
    result = ClusterAPI.execute(clServer, str(formula), 0)
    results[orig - 1] = result

def main():
    os.system("clear")

    print(" --------------------")
    print("| Mass Formula       |")
    print("| Cluster calculator |")
    print(" --------------------")
    print()
    number = int(input("How many formulas do you want to calculate? > "))
    counter = 0

    while counter < number:
        print()
        print("Formula #" + str(counter + 1))
        formulas.append(input(">"))
        results.append("NYC")
        counter += 1

    counter = 1

    for formula in formulas:
        _thread.start_new_thread(calc, (counter, formula))
        counter += 1

    os.system("clear")
    print("Calculating ...")

    finished = 0

    while finished == 0:
        calculated = []
        
        for result in results:
            if(result != "NYC"):
                calculated.append("RES")
        if(number == len(calculated)):
            finished = 1

    os.system("clear")
    print("Calculating finished")
     
    counter = 1
    for result in results:
        print()
        print("Result #" + str(counter) + "(" + str(formulas[counter-1]) + "):")
        print(str(result))
        counter += 1
