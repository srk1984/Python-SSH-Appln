#Importing the necessary modules
import sys
from ip_file_valid import ip_file_valid
from ip_address_valid import ip_addr_valid
from ip_chk_ipreach import ip_reach
from Ip_SSh_connec import chk_cred
from Ip_SSh_connec import ssh_connection
from ip_thread import create_threads
#from create_threads import create_threads
 
#Saving the list of IP addresses in ip.txt to a variable

print("ip txt")
 
ip_list = ip_file_valid()
 
#Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
 
#Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

chk_cred()
#Calling threads creation function for one or multiple SSH connections
create_threads(ip_list, ssh_connection)
