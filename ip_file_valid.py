# This file checks ip address file and content validity
import os.path
import sys

def ip_file_valid():
    ip_file=input("Enter thr filename of the Ip address file (C:/Users/Shweta/Desktop/Python/SSH App/Ip_file_valid) :")

    if (os.path.isfile(ip_file)==True):
        print("File is Valid !!" )

    else:
        print("File doesnt Exists!!")
        sys.exit()

    #open the filein read mode

    ip_file_op=open(ip_file,'r')

    # Set the position of file pointer to beginning of the file

    ip_file_op.seek(0)

    #Read the lines

    ip_list =ip_file_op.readlines()

    #close the file

    ip_file_op.close()

    return ip_list


        
        
    
