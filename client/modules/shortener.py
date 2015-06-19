import _thread
from modules.API import ClusterAPI

"""
Module "shortener"
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
    return [["shortener", "shortener.shorten()"]]

global ggt
ggt = 1

def threadfuction(clusterServer, to1, to2, nenner, zaehler):

    counter = to2

    while counter <= to1:
        nennermodulo = ClusterAPI.execute(clusterServer, str(nenner) + "%" + str(zaehler), 0)

def shorten(zaehler, nenner):

    clusterLenght =  ClusterAPI.getClusterLenght()

    counter = 1

    while counter <= clusterLenght:

        to1 = clusterLenght / counter
        to2 = clusterLenght / (counter - 1)
        _thread.start_new_thread(threadfunction, (clusterServer, to1, to2))
