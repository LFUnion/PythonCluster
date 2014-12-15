import server

"""
Module "browserauth"
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

def auth():

    openServer = server.init(10001, 10)
    
    print("Waiting for browser to connect to: " + server.socket.gethostname() + " on port 80\n")

    while True:

        connection = server.acceptConnections(openServer)

        header = server.receive(connection)

        if(header[:3] == "GET"):

            return header

            connection.close()

            break
        
        else:
            
            connection.close()

    openServer.close
