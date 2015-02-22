#Makefile for PythonCluster
#Copyright (C) 2014  Leon Schwalb and Fabian Stein
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

.SILENT:clean
.SILENT:dependand
.SILENT:standalone
.SILENT:gencode

NUITKA = nuitka

standalone:
	echo "Starting build ..."
	echo "Cleaning up ..."
	rm -rf build/
	echo "Creating directories ..."
	mkdir build
	cd build/; mkdir client
	cd build/; mkdir server
	echo "Compiling ..."
	echo "	-> Client"
	cd build/client/; $(NUITKA) --recurse-all --standalone ../../client/ui.py
	echo "	-> Server"
	cd build/server/; $(NUITKA) --recurse-all --standalone ../../server/startServer.py
	mv build/client/ui.dist/* build/client/
	mv build/server/startServer.dist/* build/server/
	echo "Removing auto-generated files ..."
	rm -r build/client/ui.build/
	rm -r build/server/startServer.build/
	rmdir build/client/ui.dist
	rmdir build/server/startServer.dist
	echo "Renaming ..."
	mv build/client/ui.exe build/client/client
	mv build/server/startServer.exe build/server/server
	echo "Copying needed files into build directory ..."
	cp client/conf build/client/conf
	cp client/clusterIndex.cli build/client/clusterIndex.cli
	echo "Done"

dependand:
	echo "Starting build ..."
	echo "Cleaning up ..."
	rm -rf build/
	echo "Creating directories ..."
	mkdir build
	cd build/; mkdir client
	cd build/; mkdir server
	echo "Compiling ..."
	echo "	-> Client"
	cd build/client/; $(NUITKA) --recurse-all ../../client/ui.py
	echo "	-> Server"
	cd build/server/; $(NUITKA) --recurse-all ../../server/startServer.py
	echo "Removing auto-generated files ..."
	rm -r build/client/ui.build/
	rm -r build/server/startServer.build/
	echo "Renaming ..."
	mv build/client/ui.exe build/client/client
	mv build/server/startServer.exe build/server/server
	echo "Copying needed files into build directory ..."
	cp client/conf build/client/conf
	cp client/clusterIndex.cli build/client/clusterIndex.cli
	echo "Done"

gencode:
	echo "Starting generation ..."
	echo "Cleaning up ..."
	rm -rf build/
	echo "Creating directories ..."
	mkdir build
	cd build/; mkdir client; mkdir client/ui.build
	cd build/; mkdir server; mkdir server/startServer.build
	echo "Generating C++ Code ..."
	echo "	-> Client"
	- cd build/client/; $(NUITKA) --recurse-all --generate-c++-only ../../client/ui.py
	echo "	-> Server"
	- cd build/server/; $(NUITKA) --recurse-all --generate-c++-only ../../server/startServer.py
	echo "Moving files into right directory ..."
	mv build/client/ui.build/* build/client/
	rmdir build/client/ui.build
	mv build/server/startServer.build/* build/server/
	rmdir build/server/startServer.build
	echo "Done"

clean:
	echo "Cleaning up ..."
	rm -rf build
	echo "Done"
