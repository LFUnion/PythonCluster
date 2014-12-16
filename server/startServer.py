import server, primes, random

"""
"startServer.py", to start a new cluster server
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

port = 10008
pwd = input("Please enter a password to stop the server > ")

serv = server.init(port, 1)

print("Server Name/IP:        '" + server.socket.gethostname() + "'")
print("On port:               '" + str(port) + "'")
print()

while True:
    print("Waiting for a connection...")
    connection = server.acceptConnections(serv)
    
    try:
        print()
        
        while True:
            get = server.receive(connection)
            if get != "":
                print("> Received             '" + get + "'")
            if get[:4] == "close":
                print("Client attempted to close server")
                server.send(connection, "Use: close [password]", False)
            if get == "close" + str(pwd):
                break
            if get:
                if "pwd" not in get and ";" not in get and "os" not in get and "sys" not in get:
                    result = eval(get)
                else:
                    result = str(random.randint(11111111, 99999999))
                result = str(result)
                print("> Send back            '" + result + "'")
                server.send(connection, result, False)
                connection.close()
                break
                
            else:
                print()
                break
        if get == "close" + str(pwd):
            server.send(connection, "Stop server...", False)
            print("[ SERVER ] Stop the server ...")
            break
    except:
        print("[ SERVER ] ERROR!")
