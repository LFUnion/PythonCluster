import math

"""
Module "primes", to calculate primes in a specified range.
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

def prime(maxNumbers):
	numbers = [0]
	maxMultiplikator = math.sqrt(maxNumbers)
	
	counter = 1
	
	while counter <= maxNumbers:
	    numbers.append(counter)
	    counter += 1
	
	
	counter = 1
	gestrichen = [0]
	
	while counter <= maxNumbers:
	    if(numbers[counter]%2 == 0):
	        gestrichen.append(counter)
	        counter += 1
	    else:
	        counter += 1
	
	counter = 2
	numberCount = 2
	primzahlen = []
	
	primzahlen.append(2)
	
	while counter <= maxNumbers:
	    if(counter in gestrichen):
	        counter += 1
	    else:
	        while numberCount <= maxMultiplikator:
	            gestrichen.append(counter*numberCount)
	            numberCount += 1
	        primzahlen.append(counter)
	        numberCount = 2
	        counter += 1
	
	return primzahlen
