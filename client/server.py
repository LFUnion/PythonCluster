import socket

"""
"server.py", a simple API
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

def init(port, maxConnections):
    
    host = ""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(maxConnections)
    print("Server started")
    return server

def acceptConnections(openServer):

    while True:
        connection, adress = openServer.accept()
        return connection

def receive(connection):

    receivedData = connection.recv(1024)
    return receivedData.decode("UTF-8")

def send(connection, data, isEncoded):

    if(isEncoded == True):
        connection.sendall(data)
    else:
        connection.sendall(data.encode("UTF-8"))
