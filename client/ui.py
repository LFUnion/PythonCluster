import loader, client, os, traceback, helpDoc
from modules import primes

"""
ClusterShell, a program to control the Cluster
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

# Load the configuration file
def load_cnfg():
    global port
    
    # Open the file
    file = open("conf")
    contents = file.readlines()
    file.close()

    # Read lines
    for i in contents:
        # If a important thing is in the line, save it
        
        # Take the port
        if i[:5] == "port=":
            port = int(i[5:])

# The copyright
def show_copyright():
    print("(c) ClusterAG 2015.")
    print("****************************************")
    print("ClusterShell is a simple program to")
    print("setup and control Clusters.")

# Auto load configuration
load_cnfg()
# Initialize modules
loader.load()
# Clear screen
os.system("clear")

# Header
print("Welcome to the ClusterShell")
print("***************************")
print("ClusterShell  Copyright (C) 2015  Leon Schwalb and Fabian Stein")
print()
print("This program comes with ABSOLUTELY NO WARRANTY; for details type 'warranty'.")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions; type 'conditions' for details.")
print()
print("Loaded " + str(loader.getlen()) + " module(s)")
print()

# The command
inp = ""
# The port (loaded by "load_cnfg()")
port = 0
# List of all commands
lastCommand = [""]
# Enable / Disable the debug mode
debugMode = False

# The mainloop
while inp != "exit":
    # Type in input
    inp = input("> ")

    # Exceptions
    try:
        # The "last" function
        if inp == "last":
	    # The very last command
            inp = lastCommand[len(lastCommand) - 1]
            # Print the command before you run it
            print("> " + inp)
            
        # Take another command
        elif inp[:4] == "last":
	    # Split input
            inputList = inp.split()
            # Print all history
            if inputList[1] == "history":
	        # Give out the list
                print(str(lastCommand))
                # Clear the input
                inp = ""
            # Else run an command
            else:
	        # Get command
                inp = lastCommand[len(lastCommand) - int(inputList[1])]
                # And run it. :D
                print("> " + inp)
        
        # Insert last command
        lastCommand.insert(1, str(inp))
        
        # The very basic commands, if you want to make yours, put it into modules.
        
        # Help
        if inp == "help":
	    # Call the helpdoc function
            helpDoc.help()
            
        # And the help of the real cluster
        elif inp == "clusterhelp":
	    # Call again...
            helpDoc.clusterhelp()
            
        # The "connect" command
        elif inp[:7] == "connect":
	    # Split input
            cnn = inp.split()
            
            # If the port is "default" then run this code:
            if port and cnn[2] == "default":
	        # And call the client.
                back = client.connect(cnn[1], port, cnn[3])
            # Else this:
            else:
	        # Call the client, too.
                back = client.connect(cnn[1], int(cnn[2]), cnn[3])
            # Print the output
            print(back)
            
        # Load the configuration
        elif inp == "load":
	    # Call this fuction:
            load_cnfg()
            
        # The "prime" function
        elif inp[:5] == "prime":
	    # Split again...
            cnn = inp.split()
            # Send to server:
            snd = "primes.prime(" + str(cnn[3]) + ")"
            
            # Again with "default" port :D
            if port and cnn[2] == "default":
	        # Connect to client and save back variable
                back = client.connect(cnn[1], port, snd)
            else:
	        # Connect to client and save back variable, too.
                back = client.connect(cnn[1], int(cnn[2]), snd)
            
            # You get back a LIST as a STRING, so this is really ****.
            back = back.replace("[", "")
            back = back.replace("]", "")
            back = back.replace(",", "")
            back = back.split()
            
            # Print "back" on screen (It's splitted)
            for i in back:
                print(i)
            
        # No comment
        elif inp == "clear":
            os.system("clear")
            
        # Copyright
        elif inp == "copyright":
            show_copyright()

        elif inp == "listmodules":
            loader.showmodules()
            
        # Enable / Disable the debug mode
        elif inp == "debug":
            if debugMode == False:
                debugMode = True
                print("Debug Mode ON")
            else:
                debugMode = False
                print("Debug Mode OFF")
                
        elif not loader.srch(inp) and inp != "exit":
            print("Unknown Command")

    # Exception stuff
    except ValueError:
        if(debugMode == False):
    	    print("Value error")
        else:
    	    print("Value error:")
    	    traceback.print_exc()
    
    except Exception:
        
    	if(debugMode == False):
    	    print("Internal Error")
    	else:
    	    print("Internal Error:")
    	    traceback.print_exc()
