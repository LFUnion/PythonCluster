import sys, os, subprocess,server, primes, random

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

def getCodeDisallowement():
    if "--deny-c++" in sys.argv:
        return True
    else:
        return False

def otfcompile(formula):
    print("> Generating code ...")
    stdheader = "#include <iostream>\n#include <cmath>\n\nint main() {\nstd::cout << std::fixed << "
    stdfooter = " << std::endl;\nreturn 0;\n}"

    code = stdheader + get + stdfooter
    with open("/tmp/otfoutput.cpp", "w") as file:
        file.write (code)

    print("> Compiling ...")
    os.system("g++ /tmp/otfoutput.cpp -O3 -o /tmp/otfexec")
    os.system("chmod +x /tmp/otfexec")

    print("> Running executable ...")
    result = subprocess.check_output("/tmp/otfexec", shell=True)

    print("> Deleting OTF files ...")
    os.system("rm -rf /tmp/otfoutput.cpp /tmp/otfexec")

    print("> Casting result")
    return float(result)

port = 10008
pwd = input("Please enter a password to stop the server > ")

serv = server.init(port, 1)
callmethod = "python"

print("Server Name/IP:        '" + server.socket.gethostname() + "'")
print("On port:               '" + str(port) + "'")
print()

try:
    while True:
        print("Waiting for a connection...")
        connection = server.acceptConnections(serv)
        
        try:
            print()
            
            while True:
                get = server.receive(connection)
                result = ""
                if get != "":
                    print("> Received             '" + get + "'")
                if get[:4] == "close":
                    print("Client attempted to close server")
                    server.send(connection, "Use: close [password]", False)
                if get == "close" + str(pwd):
                    break
                    exit()
                if get:
                    if get == "SETCALLMETHOD<C++>":
                        if getCodeDisallowement():
                            print("> Denied switch to C++ callmethod")
                            result = "DENIED"
                        else:
                            print("> Set callmethod to C++")
                            callmethod = "c++"
                            result = "OK"
                    elif get == "SETCALLMETHOD<PYTHON>":
                        print("> Set callmethod to native Python")
                        callmethod = "python"
                        result = "OK"
                    elif callmethod == "c++":
                        result = otfcompile(get)
                    elif "pwd" not in get and ";" not in get and "os" not in get and "sys" not in get and "exec" not in get and "eval" not in get and "callmethod" not in get:
                        result = eval(get)
                    else:
                        print("> Denied call")
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
                print("[ SERVER ] Stopping the server ...")
                break
        except:
            print("[ SERVER ] ERROR!")
            
except KeyboardInterrupt:
    print("> Closing socket ...")
    serv.close()
    exit()
