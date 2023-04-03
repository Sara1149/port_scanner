# port_scanner

#I warn that this script is based only for scanning

#This script uses the argparse module to handle command-line arguments, so that you can specify the remote IP address and port numbers to be scanned when the script runs. For example, to scan ports 80, 443, and 8080 on the IP address 192.168.1.1

To run this script you have to do : Python port_scanner.py 192.168.1.1 80 443 8080

Install argparse 

pip install argparse

Install sockets

pip install sockets

will produce the sample output : 
Port 80 is open
Port 443 is closed
Port 8080 is closed
