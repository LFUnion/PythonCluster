import socket

"""
Our simple client
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

def connect(host, port, message):
    
    finalString = ""
    
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (host, port)
    
    connection.connect(address)
    
    connection.sendall(str.encode(message))

    while True:
        get = connection.recv(8192)
        getDecoded = get.decode("UTF-8")
        if getDecoded != "":
            getDecoded = str(getDecoded)
            finalString += finalString + getDecoded
        else:
            break
    
    connection.close()
    
    return finalString
